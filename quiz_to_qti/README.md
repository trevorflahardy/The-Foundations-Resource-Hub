# quiz_to_qti

A strictly typed CLI that converts Quizdown-style Markdown quizzes into
[text2qti](https://github.com/gpoore/text2qti) plaintext and invokes text2qti
to produce a Canvas-importable QTI .zip.

- Input: One or more Markdown files using the “checklist with feedback” quiz
  pattern (see docs/quizzes examples).
- Output: QTI .zip ready for Canvas import, with answer shuffling enabled by
  default and “show correct answers” enabled by default.
- Preserves: General question feedback and per-choice feedback (blockquote
  lines `>` below a choice).

## Install runtime deps

Requires Python 3.8+. Install dependencies into your environment:

- click
- text2qti

## Usage

From the repo root:

```bash
python -m quiz_to_qti.cli \
  --title "3D Printing: Design for Printing Check" \
  --description "Formative check on file formats." \
  docs/quizzes/3d_printing/design_for_printing_check.md
```

Options:

- --title: Required quiz title.
- --description: Optional quiz description.
- --no-shuffle: Disable shuffle answers (enabled by default).
- --hide-correct: Disable show correct answers (enabled by default).
- --out: Working/output directory (default ./quiz_build).
- --pandoc-mathml: Pass-through to text2qti to render LaTeX as MathML.

## Methodology

1. Parse Quizdown Markdown into an AST capturing questions, choices, and
   feedback. Questions are recognized by `###` headings; choices by GitHub
   task items `[ ]`/`[x]`; feedback lines are blockquotes (`>`) either before
   choices (general) or under each choice (per-choice).
2. Render to text2qti plaintext with header options:
   - Quiz title / description
   - shuffle answers: true/false
   - show correct answers: true/false
3. Write the plaintext to an intermediate file and call `text2qti` to produce
   the QTI .zip.

## Notes and limitations

- Batch builder: `python -m quiz_to_qti.batch --root docs/quizzes --out _quiz_build`
  - Combines 3d_printing pairs like `<name>_check.md` and `<name>_quiz.md` into one Canvas quiz.
  - Other topics build one quiz per file.
  - Outputs .txt and .zip into `_quiz_build` and overwrites on changes.
- Multiple correct choices produce a multiple-answers question using text2qti
  `[ ]` / `[*]` syntax. A single correct choice produces standard multiple
  choice using `a)` lines with the correct one marked by a leading `*`.
- If a question has no choices, it is treated as an essay question.
- Titles and points per question can be added later if needed; support is
  implemented but not inferred from Quizdown at this time.
- Always preview imported quizzes in Canvas.

## Development

- Code is annotated and designed for strict type checking (use mypy/pyright).
- Keep parsing routines resilient but explicit—prefer clear regex and
  small, testable helpers.
