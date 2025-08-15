"""quiz_to_qti package.

Strictly typed CLI tool to convert Quizdown-style Markdown quizzes into
text2qti-compatible plain text, then invoke text2qti to produce a Canvas QTI zip.

Expose only stable, minimal surface under this package; consumers should use the CLI.
"""

from __future__ import annotations

__all__ = [
    "__version__",
]

__version__: str = "0.1.0"
