from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable, List, Optional, Sequence, Tuple


@dataclass(slots=True)
class QuizdownQuestion:
    """In-memory representation of a parsed Quizdown-style question.

    Attributes
    - prompt_md: The Markdown for the question stem.
    - choices: List of (is_correct, choice_md, choice_feedback_md) tuples. Multiple
      correct choices imply a multiple-answers question.
    - general_feedback_md: Optional Markdown feedback for the question.
    - title: Optional plain-text title. Treated as plain text in text2qti.
    - points: Optional point value (int or half-integer as text2qti supports).
    """

    prompt_md: str
    choices: List[Tuple[bool, str, Optional[str]]]
    general_feedback_md: Optional[str] = None
    title: Optional[str] = None
    points: Optional[float] = None


@dataclass(slots=True)
class ConvertedQuiz:
    """The fully converted quiz text2qti plaintext ready for writing to disk."""

    title: str
    description: Optional[str]
    body: str


QUIZDOWN_Q_BLOCK_RE = re.compile(
    r"^###\s+(?P<prompt>.+?)\n(.*?)$(?=^###|\Z)", re.M | re.S
)
# Choices are GitHub-style checklist items with optional feedback blocks below.
CHOICE_RE = re.compile(r"^\s*1?\.?\s*\[(?P<mark> |x|X)\]\s+(?P<text>.*)$", re.M)
FEEDBACK_RE = re.compile(r"^\s*>\s+(?P<fb>.+)$", re.M)


def parse_quizdown(md: str) -> List[QuizdownQuestion]:
    """Parse a Quizdown-style Markdown quiz into questions.

    A question begins with a top-level heading line starting with '### '.
    Choices are GitHub task list items `[ ]` or `[x]` (case-insensitive).
    Per-choice feedback uses blockquote lines (`>`), immediately following
    a choice. A leading blockquote block before the first choice is treated
    as general feedback for the question.
    """
    questions: List[QuizdownQuestion] = []

    lines = md.splitlines()
    i = 0
    n = len(lines)

    def is_heading(idx: int) -> bool:
        return idx < n and re.match(r"^\s*###\s+", lines[idx]) is not None

    while i < n:
        if not is_heading(i):
            i += 1
            continue
        # Extract prompt from heading line
        prompt = re.sub(r"^\s*###\s+", "", lines[i]).strip()
        i += 1
        # Collect block until next heading or EOF
        start = i
        while i < n and not is_heading(i):
            i += 1
        block = "\n".join(lines[start:i]).strip()

        # General feedback: consecutive leading blockquote lines
        general_fb: Optional[str] = None
        body = block
        m_fb = re.match(r"^(?:\s*>\s*.+\n?)+", body, flags=re.M)
        if m_fb:
            fb_block = m_fb.group(0)
            general_fb = re.sub(r"^\s*>\s?", "", fb_block, flags=re.M).strip()
            body = body[len(fb_block) :].lstrip()

        # Choices: find all checklist items and their trailing feedback segments
        choices: List[Tuple[bool, str, Optional[str]]] = []
        matches = list(re.finditer(CHOICE_RE, body))
        for j, m in enumerate(matches):
            start_pos = m.start()
            end_pos = matches[j + 1].start() if j + 1 < len(matches) else len(body)
            chunk = body[start_pos:end_pos]
            # Choice line text
            is_correct = m.group("mark").lower() == "x"
            choice_text = m.group("text").strip()
            # Per-choice feedback from blockquote lines in the chunk (after first line)
            nl = chunk.find("\n")
            rest = chunk[nl + 1 :] if nl != -1 else ""
            fb_lines = [mm.group(1) for mm in re.finditer(r"^\s*>\s+(.+)$", rest, re.M)]
            per_choice_fb = "\n".join(fb_lines).strip() if fb_lines else None
            choices.append((is_correct, choice_text, per_choice_fb))

        if not choices:
            q = QuizdownQuestion(
                prompt_md=prompt, choices=[], general_feedback_md=general_fb
            )
        else:
            q = QuizdownQuestion(
                prompt_md=prompt, choices=choices, general_feedback_md=general_fb
            )
        questions.append(q)

    return questions


def _to_text2qti_question(q: QuizdownQuestion, idx: int) -> str:
    """Convert one question into text2qti plaintext.

    This supports:
    - multiple-choice (single correct)
    - multiple-answers (multiple correct) using [*] syntax
    - essay if no choices
    - attaches general and per-choice feedback
    """
    lines: List[str] = []
    # Optional title line could be added; we keep implicit numbering
    if q.points is not None:
        lines.append(f"Points: {q.points:g}")
    lines.append(f"{idx}.  {q.prompt_md}")
    if q.general_feedback_md:
        for fb_line in q.general_feedback_md.splitlines():
            lines.append(f"... {fb_line}")

    if not q.choices:
        # Essay: underscore fence
        lines.append("____")
        return "\n".join(lines) + "\n"

    multiple_correct = sum(1 for c in q.choices if c[0]) > 1
    if multiple_correct:
        # text2qti multiple-answers with [ ] / [*]
        for is_correct, text, fb in q.choices:
            mark = "[*]" if is_correct else "[ ]"
            lines.append(f"{mark} {text}")
            if fb:
                for line in fb.splitlines():
                    lines.append(f"... {line}")
    else:
        # Standard multiple choice a)/b)/c) with * marker
        letter = ord("a")
        for is_correct, text, fb in q.choices:
            prefix = f"{chr(letter)})"
            if is_correct:
                prefix = "*" + prefix
            lines.append(f"{prefix}  {text}")
            if fb:
                for line in fb.splitlines():
                    lines.append(f"... {line}")
            letter += 1

    return "\n".join(lines) + "\n"


def to_text2qti_plaintext(
    questions: Sequence[QuizdownQuestion],
    *,
    title: str,
    description: Optional[str],
    shuffle_answers: bool,
    show_correct: bool,
) -> ConvertedQuiz:
    """Render questions into a text2qti plaintext string with quiz options.

    text2qti header supports:
      Quiz title: <title>
      Quiz description: <desc>
      shuffle answers: true|false
      show correct answers: true|false
    """
    header: List[str] = [f"Quiz title: {title}"]
    if description:
        header.append(f"Quiz description: {description}")
    header.append(f"shuffle answers: {'true' if shuffle_answers else 'false'}")
    header.append(f"show correct answers: {'true' if show_correct else 'false'}")

    body_parts = ["\n".join(header), ""]
    for i, q in enumerate(questions, start=1):
        body_parts.append(_to_text2qti_question(q, i))

    body = "\n".join(body_parts).strip() + "\n"
    return ConvertedQuiz(title=title, description=description, body=body)


def convert_quizdown_files(
    files: Iterable[Path],
    *,
    title: str,
    description: Optional[str] = None,
    shuffle_answers: bool = True,
    show_correct: bool = True,
) -> ConvertedQuiz:
    """Parse and merge multiple Quizdown Markdown files into one text2qti quiz.

    The questions from each file are appended in order. Title/description apply
    to the combined quiz. Feedback comments are preserved.
    """
    all_questions: List[QuizdownQuestion] = []
    for fp in files:
        text = fp.read_text(encoding="utf-8")
        qs = parse_quizdown(text)
        all_questions.extend(qs)
    return to_text2qti_plaintext(
        all_questions,
        title=title,
        description=description,
        shuffle_answers=shuffle_answers,
        show_correct=show_correct,
    )
