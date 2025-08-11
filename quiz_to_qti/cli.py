from __future__ import annotations

import subprocess
from pathlib import Path
import sys
import shutil
from typing import Iterable, Optional, Dict, List, Tuple
import re

import click

from .converter import convert_quizdown_files


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
    no_shuffle: bool,
    hide_correct: bool,
    out_dir: Path,
    pandoc_mathml: bool,
) -> None:
    """Convert Quizdown-style Markdown quizzes to a Canvas-importable QTI zip.

    Multiple INPUTS may be provided; they are merged into a single quiz.
    Feedback comments are preserved.
    """
    quiz = convert_quizdown_files(
        inputs,
        title=title_,
        description=description,
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
    groups: List[Tuple[str, str, List[Path], Optional[str]]] = []
    for topic_dir in sorted([p for p in root.glob("*/") if p.is_dir()]):
        topic = topic_dir.name
        md_files = sorted(topic_dir.glob("*.md"))
        if topic == "3d_printing":
            by_base: Dict[str, Dict[str, Path]] = {}
            for f in md_files:
                base, suffix = _stem_key(f)
                by_base.setdefault(base, {})[suffix or "single"] = f
            for base, parts in by_base.items():
                if "check" in parts and "quiz" in parts:
                    files = [parts["check"], parts["quiz"]]
                    title = _prettify_title(base)
                    desc = f"Auto-generated combined quiz from: {parts['check'].name}, {parts['quiz'].name}"
                    groups.append((f"{topic}/{base}", title, files, desc))
                else:
                    files = list(parts.values())
                    title = _prettify_title(Path(base).name)
                    desc = f"Auto-generated quiz from: {files[0].name}"
                    groups.append((f"{topic}/{base}", title, files, desc))
        else:
            for f in md_files:
                base, _ = _stem_key(f)
                title = _prettify_title(Path(base).name)
                desc = f"Auto-generated quiz from: {f.name}"
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
def batch_cmd(root: Path, out_dir: Path) -> None:
    """Discover and convert all quizzes under ROOT into OUT directory.

    In 3d_printing, pairs like <base>_check.md and <base>_quiz.md are combined.
    """
    groups = _discover_quiz_groups(root)

    # Locate text2qti
    t2qti = Path(sys.executable).with_name("text2qti")
    found = shutil.which("text2qti") if not t2qti.exists() else str(t2qti)
    if not t2qti.exists() and not found:
        raise SystemExit("text2qti not found in PATH or venv; please install it.")
    if not t2qti.exists() and found:
        t2qti = Path(found)

    out_dir.mkdir(parents=True, exist_ok=True)
    for _key, title, files, desc in groups:
        converted = convert_quizdown_files(
            files,
            title=title,
            description=desc,
            shuffle_answers=True,
            show_correct=True,
        )
        basename = _sanitize_basename(title)
        txt_path = out_dir / f"{basename}.txt"
        txt_path.write_text(converted.body, encoding="utf-8")

        cmd = [str(t2qti), txt_path.name]
        try:
            subprocess.run(cmd, cwd=str(out_dir), check=True, text=True, input="\n")
        except subprocess.CalledProcessError as e:
            raise SystemExit(
                f"text2qti failed for {txt_path.name} with exit code {e.returncode}"
            ) from e

        zip_path = out_dir / f"{basename}.zip"
        if zip_path.exists():
            click.echo(f"Built {zip_path}")


if __name__ == "__main__":
    cli()
