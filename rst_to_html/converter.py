"""
Main RST to HTML converter class
"""

from __future__ import annotations

from pathlib import Path

from docutils.core import publish_file
from docutils.parsers.rst import Parser
from docutils.writers.html5_polyglot import Writer

from .config import Config
from .css_manager import CSSManager
from .file_utils import FileUtils
from .html_processor import HTMLProcessor
from .sphinx_directives import register_sphinx_directives


class RSTConverter:
    """Main converter class for RST to HTML conversion"""

    def __init__(self, config: Config):
        self.config = config
        self.css_manager = CSSManager(
            source_dir=config.source_dir, canvas_mode=config.canvas_mode
        )
        self.file_utils = FileUtils()
        self.html_processor = HTMLProcessor()

        # Register Sphinx directives
        register_sphinx_directives()

        if self.config.verbose:
            print(f"Initialized converter with config: {config}")

    def convert_single_file(self, input_file: Path, output_file: Path) -> bool:
        """Convert a single RST file to HTML"""
        try:
            if self.config.verbose:
                print(f"Converting: {input_file} -> {output_file}")

            # Ensure output directory exists
            self.file_utils.ensure_output_dir(output_file)

            # Convert RST to HTML using docutils
            with open(input_file, "r", encoding="utf-8") as input_f:
                html_output = publish_file(
                    source=input_f,
                    destination=None,
                    writer=Writer(),
                    parser=Parser(),
                    settings_overrides=self.config.docutils_settings,
                )

            # Decode if bytes
            if isinstance(html_output, bytes):
                html_output = html_output.decode("utf-8")

            # Process HTML content
            html_output = self.html_processor.process_html(html_output)

            # Apply CSS inlining
            html_output = self._apply_css_styling(html_output)

            # Write final HTML
            with open(output_file, "w", encoding="utf-8") as output_f:
                output_f.write(html_output)

            if self.config.verbose:
                print(f"Successfully converted: {input_file.name}")

            return True

        except Exception as e:
            print(f"Error converting {input_file}: {e}")
            return False

    def _apply_css_styling(self, html_content: str) -> str:
        """Apply CSS styling to HTML content"""
        # Get available CSS files
        css_files = self.file_utils.get_css_files(
            self.config.css_dir, self.config.custom_css_files
        )

        # Generate complete CSS
        css_content = self.css_manager.generate_complete_css(css_files)

        # Remove external CSS links
        html_content, removed_links = self.css_manager.remove_external_css_links(
            html_content
        )

        if self.config.verbose:
            print(f"DEBUG: Removed {removed_links} external CSS links")

        # Inject CSS into HTML
        html_content = self.css_manager.inject_css_into_html(html_content, css_content)

        if self.config.verbose and css_content:
            print("DEBUG: Added inlined CSS to HTML")

        return html_content

    def convert_all_files(self) -> tuple[int, int]:
        """Convert all RST files in the source directory"""
        # Find all RST files
        rst_files = self.file_utils.find_rst_files(self.config.source_dir)

        if not rst_files:
            print(f"No RST files found in {self.config.source_dir}")
            return 0, 0

        # Create output structure
        self.file_utils.create_output_structure(
            self.config.source_dir, self.config.output_dir, self.config.static_dirs
        )

        success_count = 0
        total_files = len(rst_files)

        print(f"Found {total_files} RST files to convert")

        # Convert each file
        for rst_file in rst_files:
            output_file = self.file_utils.calculate_relative_path(
                rst_file, self.config.source_dir, self.config.output_dir
            )

            if self.convert_single_file(rst_file, output_file):
                success_count += 1

        return success_count, total_files

    def get_conversion_summary(self, success_count: int, total_files: int) -> str:
        """Generate a summary of the conversion results"""
        if success_count == total_files:
            return (
                f"✅ All {total_files} files converted successfully!\n"
                f"Output directory: {self.config.output_dir}"
            )
        else:
            return (
                f"⚠️  Conversion completed: {success_count}/{total_files} files successful\n"
                f"Output directory: {self.config.output_dir}"
            )
