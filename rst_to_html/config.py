"""
Configuration management for RST to HTML converter
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Config:
    """Configuration settings for RST to HTML conversion"""

    # Input/Output paths
    source_dir: Path = Path("docs")
    output_dir: Path = Path("docs/_build_raw/html")

    # Conversion settings
    input_encoding: str = "utf-8"
    output_encoding: str = "utf-8"
    initial_header_level: int = 1
    syntax_highlight: str = "short"

    # Behavior flags
    verbose: bool = False
    embed_stylesheet: bool = False
    file_insertion_enabled: bool = True
    raw_enabled: bool = True

    # Error handling
    report_level: int = 5  # Suppress all warning messages
    halt_level: int = 5  # Don't halt on warnings

    # Canvas LMS compatibility
    canvas_mode: bool = True
    aggressive_css_override: bool = True

    # Static directories to copy
    static_dirs: list[str] = None

    # Custom CSS files to include
    custom_css_files: list[str] = None

    def __post_init__(self) -> None:
        """Initialize default values for mutable fields"""
        if self.static_dirs is None:
            self.static_dirs = ["_static", "images"]

        if self.custom_css_files is None:
            self.custom_css_files = [
                "whole_code_block.css",
                "custom.css",
            ]

    @property
    def docutils_settings(self) -> dict[str, Any]:
        """Get docutils settings dictionary"""
        return {
            "input_encoding": self.input_encoding,
            "output_encoding": self.output_encoding,
            "embed_stylesheet": self.embed_stylesheet,
            "xml_declaration": False,
            "doctype_declaration": True,
            "initial_header_level": self.initial_header_level,
            "file_insertion_enabled": self.file_insertion_enabled,
            "raw_enabled": self.raw_enabled,
            "report_level": self.report_level,
            "halt_level": self.halt_level,
            "warning_stream": None,
            "syntax_highlight": self.syntax_highlight,
        }

    def validate(self) -> None:
        """Validate configuration settings"""
        if not self.source_dir.exists():
            raise ValueError(f"Source directory does not exist: {self.source_dir}")

        # Ensure paths are Path objects
        self.source_dir = Path(self.source_dir)
        self.output_dir = Path(self.output_dir)

    @classmethod
    def from_args(
        cls,
        source_dir: Path | str | None = None,
        output_dir: Path | str | None = None,
        verbose: bool = False,
        canvas_mode: bool = True,
    ) -> Config:
        """Create configuration from command line arguments"""
        config = cls(
            verbose=verbose,
            canvas_mode=canvas_mode,
        )

        if source_dir:
            config.source_dir = Path(source_dir)
        if output_dir:
            config.output_dir = Path(output_dir)

        config.validate()
        return config
