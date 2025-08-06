"""
File system utilities for RST to HTML conversion
"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import List


class FileUtils:
    """File system operations for the converter"""

    @staticmethod
    def find_rst_files(source_dir: Path) -> List[Path]:
        """Find all RST files in the source directory, excluding build directories"""
        rst_files = []

        for rst_file in source_dir.rglob("*.rst"):
            # Skip files in _build directories
            if "_build" not in rst_file.parts:
                rst_files.append(rst_file)

        return rst_files

    @staticmethod
    def create_output_structure(
        source_dir: Path, output_dir: Path, static_dirs: List[str]
    ) -> None:
        """Create output directory structure and copy static files"""
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        # Copy static directories
        for static_dir in static_dirs:
            src_static = source_dir / static_dir
            dst_static = output_dir / static_dir

            if src_static.exists():
                if dst_static.exists():
                    shutil.rmtree(dst_static)
                shutil.copytree(src_static, dst_static)
                print(f"Copied {static_dir} to output directory")

    @staticmethod
    def get_css_files(css_dir: Path, custom_css_files: List[str]) -> List[Path]:
        """Find available custom CSS files"""
        css_files = []

        if css_dir.exists():
            for css_name in custom_css_files:
                css_path = css_dir / css_name
                if css_path.exists():
                    css_files.append(css_path)

        return css_files

    @staticmethod
    def ensure_output_dir(output_file: Path) -> None:
        """Ensure the output directory exists for a file"""
        output_file.parent.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def calculate_relative_path(
        source_file: Path, source_dir: Path, output_dir: Path
    ) -> Path:
        """Calculate the output path for a source file"""
        rel_path = source_file.relative_to(source_dir)
        return output_dir / rel_path.with_suffix(".html")
