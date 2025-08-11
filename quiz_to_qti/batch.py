from __future__ import annotations

import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

from .converter import convert_quizdown_files


@dataclass(slots=True)
class QuizGroup:
    key: str
    title: str
    files: List[Path]
    description: Optional[str]


def _sanitize_basename(name: str) -> str:
    norm = re.sub(r"\s+", " ", name).strip()
    underscored = norm.replace(" ", "_")
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", underscored)
    safe = re.sub(r"_+", "_", safe).strip("._-")
    return safe or "quiz"


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


def discover_quiz_groups(root: Path) -> List[QuizGroup]:
    """Discover quizzes under root, combining *_check and *_quiz pairs in 3d_printing."""
    groups: List[QuizGroup] = []
    for topic_dir in sorted([p for p in root.glob("*/") if p.is_dir()]):
        topic = topic_dir.name
        md_files = sorted(topic_dir.glob("*.md"))
        if topic == "3d_printing":
            by_base: Dict[str, Dict[str, Path]] = {}
            for f in md_files:
                base, suffix = _stem_key(f)
                by_base.setdefault(base, {})[suffix or "single"] = f
            for base, parts in by_base.items():
                files: List[Path]
                if "check" in parts and "quiz" in parts:
                    files = [parts["check"], parts["quiz"]]
                    title = _prettify_title(base)
                    desc = f"Auto-generated combined quiz from: {parts['check'].name}, {parts['quiz'].name}"
                    groups.append(
                        QuizGroup(
                            key=f"{topic}/{base}",
                            title=title,
                            files=files,
                            description=desc,
                        )
                    )
                else:
                    files = list(parts.values())
                    title = _prettify_title(Path(base).name)
                    desc = f"Auto-generated quiz from: {files[0].name}"
                    groups.append(
                        QuizGroup(
                            key=f"{topic}/{base}",
                            title=title,
                            files=files,
                            description=desc,
                        )
                    )
        else:
            for f in md_files:
                base, _ = _stem_key(f)
                title = _prettify_title(Path(base).name)
                desc = f"Auto-generated quiz from: {f.name}"
                groups.append(
                    QuizGroup(
                        key=f"{topic}/{base}", title=title, files=[f], description=desc
                    )
                )
    return groups


def build_groups(groups: Sequence[QuizGroup], out_dir: Path) -> List[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    produced: List[Path] = []
    t2qti = Path(sys.executable).with_name("text2qti")
    found = shutil.which("text2qti") if not t2qti.exists() else str(t2qti)
    if not t2qti.exists() and not found:
        raise SystemExit("text2qti not found in PATH or venv; please install it.")
    if not t2qti.exists() and found:
        t2qti = Path(found)

    for g in groups:
        converted = convert_quizdown_files(
            g.files,
            title=g.title,
            description=g.description,
            shuffle_answers=True,
            show_correct=True,
        )
        basename = _sanitize_basename(g.title)
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
            produced.append(zip_path)
    return produced


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Batch build QTI quizzes from docs/quizzes"
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("docs/quizzes"),
        help="Root directory containing quiz markdown",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("_quiz_build"),
        help="Output directory for QTI zips",
    )
    args = parser.parse_args()

    groups = discover_quiz_groups(args.root)
    build_groups(groups, args.out)


if __name__ == "__main__":
    main()
