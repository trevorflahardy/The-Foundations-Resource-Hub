from __future__ import annotations

import subprocess
from pathlib import Path
import sys
import os
import shutil
from typing import Iterable, Optional, Dict, List, Tuple
import re

import click

from .converter import convert_quizdown_files
from .auto_description import auto_generate_description


def _sanitize_basename(title: str) -> str:
    """Make a safe filesystem basename from a title.

    - Normalize whitespace to single spaces; convert spaces to underscores
    - Replace any character not in [A-Za-z0-9._-] with underscore
    - Collapse multiple underscores and trim
    """
    norm = re.sub(r"\s+", " ", title).strip()
    underscored = norm.replace(" ", "_")
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", underscored)
    safe = re.sub(r"_+", "_", safe).strip("._-")
    return safe or "quiz"


def _write_temp_text2qti(content: str, dest_dir: Path, quiz_basename: str) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    path = dest_dir / f"{quiz_basename}.txt"
    path.write_text(content, encoding="utf-8")
    return path


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option()
def cli() -> None:
    """quiz_to_qti: Convert Quizdown-style Markdown into Canvas QTI.

    Subcommands:
    - convert: convert specific files into one quiz
    - batch: discover and build all quizzes under docs/quizzes
    """


@cli.command(name="convert")
@click.argument(
    "inputs",
    nargs=-1,
    type=click.Path(path_type=Path, exists=True, dir_okay=False),
    required=True,
)
@click.option("--title", "title_", required=True, help="Quiz title to embed in QTI.")
@click.option("--description", default=None, help="Optional quiz description.")
@click.option(
    "--auto-desc",
    is_flag=True,
    help="Auto-generate description using local Ollama (required).",
)
@click.option(
    "--ollama-url",
    default="http://localhost:11434",
    show_default=True,
    help="Ollama base URL.",
)
@click.option(
    "--ollama-model", default="llama3.2", show_default=True, help="Ollama model name."
)
@click.option(
    "--docs-root",
    type=click.Path(path_type=Path, file_okay=False, exists=True),
    default=Path("docs"),
    show_default=True,
    help="Root of Sphinx docs to use as context for auto description.",
)
@click.option(
    "--no-shuffle",
    is_flag=True,
    help="Disable shuffling of answers (enabled by default).",
)
@click.option(
    "--hide-correct",
    is_flag=True,
    help="Disable 'show correct answers' (enabled by default).",
)
@click.option(
    "--out",
    "out_dir",
    type=click.Path(path_type=Path, file_okay=False),
    default=Path("./_quiz_build"),
    show_default=True,
    help="Working/output directory for intermediate files and final QTI zip.",
)
@click.option(
    "--pandoc-mathml",
    is_flag=True,
    help="Pass through to text2qti to convert LaTeX to MathML via Pandoc.",
)
def convert_cmd(
    inputs: Iterable[Path],
    title_: str,
    description: Optional[str],
    auto_desc: bool,
    ollama_url: str,
    ollama_model: str,
    docs_root: Path,
    no_shuffle: bool,
    hide_correct: bool,
    out_dir: Path,
    pandoc_mathml: bool,
) -> None:
    """Convert Quizdown-style Markdown quizzes to a Canvas-importable QTI zip.

    Multiple INPUTS may be provided; they are merged into a single quiz.
    Feedback comments are preserved.
    """
    # Description selection
    final_desc = description
    if auto_desc or not description:
        final_desc = auto_generate_description(
            inputs,
            title=title_,
            docs_root=docs_root,
            ollama_url=ollama_url,
            ollama_model=ollama_model,
        )

    quiz = convert_quizdown_files(
        inputs,
        title=title_,
        description=final_desc,
        shuffle_answers=not no_shuffle,
        show_correct=not hide_correct,
    )

    # Write text2qti plain text to a temp working path
    quiz_basename = _sanitize_basename(title_)
    txt_path = _write_temp_text2qti(
        quiz.body, Path(out_dir), quiz_basename=quiz_basename
    )

    # Call text2qti to produce the QTI zip in same folder
    t2qti = Path(sys.executable).with_name("text2qti")
    if not t2qti.exists():
        found = shutil.which("text2qti")
        if found:
            t2qti = Path(found)
        else:
            raise SystemExit(
                "Cannot find 'text2qti' console script. Ensure the text2qti package is installed in your environment."
            )
    cmd = [str(t2qti)]
    if pandoc_mathml:
        cmd.append("--pandoc-mathml")
    # Run from the output directory and pass only the filename so relative paths work
    cmd.append(str(Path(txt_path.name)))
    try:
        # Send a newline to accept default LaTeX URL on first run
        subprocess.run(cmd, cwd=str(out_dir), check=True, text=True, input="\n")
    except subprocess.CalledProcessError as e:
        raise SystemExit(f"text2qti failed with exit code {e.returncode}") from e

    click.echo(f"Wrote text2qti input: {txt_path}")
    zip_path = Path(out_dir) / f"{quiz_basename}.zip"
    if zip_path.exists():
        click.echo(f"QTI zip ready for Canvas import: {zip_path}")
    else:
        click.echo("text2qti did not produce a zip file. Check above for errors.")


############################
# Batch builder subcommand #
############################


def _prettify_title(s: str) -> str:
    s = s.replace("_", " ").replace("-", " ")
    return re.sub(r"\s+", " ", s).strip().title()


def _stem_key(p: Path) -> Tuple[str, str]:
    """Return (base, suffix) where suffix is one of '', 'check', 'quiz'."""
    stem = p.stem.lower()
    m = re.match(r"^(.*?)(?:[_-](check|quiz))?$", stem)
    if m:
        base = m.group(1) or stem
        suffix = m.group(2) or ""
        return base, suffix
    return stem, ""


def _discover_quiz_groups(
    root: Path,
) -> List[Tuple[str, str, List[Path], Optional[str]]]:
    """Find all quiz files recursively and group them appropriately."""
    groups: List[Tuple[str, str, List[Path], Optional[str]]] = []

    # Find all directories recursively
    all_dirs = [root]  # Start with root
    for p in root.glob("**/"):
        if p.is_dir() and p != root:
            all_dirs.append(p)

    for topic_dir in sorted(all_dirs):
        # Extract the relative path from root as topic
        rel_path = topic_dir.relative_to(root.parent) if root.parent in topic_dir.parents else topic_dir.relative_to(root)
        topic = str(rel_path).replace('\\', '/')
        md_files = sorted(topic_dir.glob("*.md"))

        # Skip if no markdown files
        if not md_files:
            continue

        # Special handling for 3d_printing folder - combine check and quiz files
        if "3d_printing" in str(topic_dir):
            by_base: Dict[str, Dict[str, Path]] = {}
            for f in md_files:
                base, suffix = _stem_key(f)
                by_base.setdefault(base, {})[suffix or "single"] = f
            for base, parts in by_base.items():
                if "check" in parts and "quiz" in parts:
                    files = [parts["check"], parts["quiz"]]
                    title = _prettify_title(base)
                    desc = None  # Let auto-description handle it
                    groups.append((f"{topic}/{base}", title, files, desc))
                else:
                    files = list(parts.values())
                    title = _prettify_title(Path(base).name)
                    desc = None  # Let auto-description handle it
                    groups.append((f"{topic}/{base}", title, files, desc))
        else:
            for f in md_files:
                base, _ = _stem_key(f)
                title = _prettify_title(Path(base).name)
                desc = None  # Let auto-description handle it
                groups.append((f"{topic}/{base}", title, [f], desc))

    return groups


@cli.command(name="batch")
@click.option(
    "--root",
    type=click.Path(path_type=Path, file_okay=False, exists=True),
    default=Path("docs/quizzes"),
    show_default=True,
    help="Root directory containing quiz markdown",
)
@click.option(
    "--out",
    "out_dir",
    type=click.Path(path_type=Path, file_okay=False),
    default=Path("_quiz_build"),
    show_default=True,
    help="Output directory for QTI zips",
)
@click.option(
    "--auto-desc",
    is_flag=True,
    help="Auto-generate descriptions using local Ollama (required).",
)
@click.option(
    "--ollama-url",
    default="http://localhost:11434",
    show_default=True,
    help="Ollama base URL.",
)
@click.option(
    "--ollama-model", default="llama3.2", show_default=True, help="Ollama model name."
)
@click.option(
    "--docs-root",
    type=click.Path(path_type=Path, file_okay=False, exists=True),
    default=Path("docs"),
    show_default=True,
    help="Root of Sphinx docs to use as context for auto description.",
)
def batch_cmd(
    root: Path,
    out_dir: Path,
    auto_desc: bool,
    ollama_url: str,
    ollama_model: str,
    docs_root: Path,
) -> None:
    """Discover and convert all quizzes under ROOT into OUT directory.

    In 3d_printing, pairs like <base>_check.md and <base>_quiz.md are combined.
    Automatically finds all quiz files in subdirectories.
    """
    click.echo(f"Discovering quiz files in {root}...")
    groups = _discover_quiz_groups(root)
    click.echo(f"Found {len(groups)} quiz groups to process")

    # Locate text2qti
    t2qti = Path(sys.executable).with_name("text2qti")
    found = shutil.which("text2qti") if not t2qti.exists() else str(t2qti)
    if not t2qti.exists() and not found:
        raise SystemExit("text2qti not found in PATH or venv; please install it.")
    if not t2qti.exists() and found:
        t2qti = Path(found)

    out_dir.mkdir(parents=True, exist_ok=True)

    # First, generate all descriptions serially to avoid overloading Ollama
    descriptions = {}
    if auto_desc:
        click.echo("Generating descriptions using Ollama...")
        for i, (key, title, files, _) in enumerate(groups, 1):
            try:
                click.echo(f"[{i}/{len(groups)}] Generating description for {title}")
                desc = auto_generate_description(
                    files,
                    title=title,
                    docs_root=docs_root,
                    ollama_url=ollama_url,
                    ollama_model=ollama_model,
                )
                descriptions[key] = desc
            except Exception as e:
                click.echo(f"[{i}/{len(groups)}] Failed to generate description for {title}")
                descriptions[key] = f"Quiz on {title}"  # Simple fallback

    # Build in parallel (now descriptions are already generated)
    from concurrent.futures import ThreadPoolExecutor, as_completed

    def build_one(_key: str, title: str, files: List[Path], desc: Optional[str]) -> str:
        # Use the pre-generated description or fallback to the original
        final_desc = descriptions.get(_key) if auto_desc else desc

        converted = convert_quizdown_files(
            files,
            title=title,
            description=final_desc,
            shuffle_answers=True,
            show_correct=True,
        )
        basename = _sanitize_basename(title)
        txt_path = out_dir / f"{basename}.txt"
        txt_path.write_text(converted.body, encoding="utf-8")
        cmd = [str(t2qti), txt_path.name]
        subprocess.run(cmd, cwd=str(out_dir), check=True, text=True, input="\n")
        return str(out_dir / f"{basename}.zip")

    results: List[str] = []
    errors: List[str] = []
    click.echo(f"Building {len(groups)} quizzes in parallel...")
    with ThreadPoolExecutor(max_workers=min(8, max(2, len(groups)))) as ex:
        futures = {ex.submit(build_one, k, t, f, d): (k, t) for (k, t, f, d) in groups}
        completed = 0
        for fut in as_completed(futures):
            key, title = futures[fut]
            completed += 1
            try:
                zip_path = fut.result()
                results.append(zip_path)
                click.echo(f"[{completed}/{len(groups)}] Built {Path(zip_path).name}")
            except subprocess.CalledProcessError as e:
                errors.append(f"{title}: text2qti failed with exit code {e.returncode}")
                click.echo(f"[{completed}/{len(groups)}] Failed to build {title}")
            except Exception as e:
                errors.append(f"{title}: {e}")
                click.echo(f"[{completed}/{len(groups)}] Failed to build {title}")

    # Summary
    click.echo(f"\nSummary: Successfully built {len(results)} of {len(groups)} quizzes")
    if errors:
        click.echo(f"Failed to build {len(errors)} quizzes:")
        for error in errors:
            click.echo(f"  - {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    cli()
