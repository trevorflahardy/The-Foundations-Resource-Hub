#!/usr/bin/env python3
"""
RST to HTML Converter CLI

A clean, modular command-line interface for converting RST files to HTML
with CSS inlining and Canvas LMS compatibility.
"""

import sys
from pathlib import Path

import click

from . import RSTConverter, Config


@click.command()
@click.option(
    "--source-dir",
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    default=Path("docs"),
    help="Source directory containing RST files (default: docs)",
)
@click.option(
    "--output-dir",
    type=click.Path(path_type=Path),
    default=Path("docs/_build_raw/html"),
    help="Output directory for HTML files (default: docs/_build_raw/html)",
)
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option("--no-canvas", is_flag=True, help="Disable Canvas LMS compatibility mode")
@click.version_option(version="1.0.0", prog_name="rst-to-html")
def main(
    source_dir: Path,
    output_dir: Path,
    verbose: bool,
    no_canvas: bool,
) -> None:
    """
    Convert RST files to HTML with inlined CSS and Canvas LMS compatibility.

    This tool converts all RST files in the source directory to standalone HTML
    files with inlined CSS, making them suitable for upload to Canvas LMS or
    other platforms that don't support external stylesheets.

    Examples:

        # Convert with default settings
        python -m rst_to_html

        # Convert with custom directories and verbose output
        python -m rst_to_html --source-dir my_docs --output-dir build/html -v

        # Convert without Canvas LMS compatibility
        python -m rst_to_html --no-canvas
    """

    try:
        # Create configuration
        config = Config.from_args(
            source_dir=source_dir,
            output_dir=output_dir,
            verbose=verbose,
            canvas_mode=not no_canvas,
        )

        if verbose:
            click.echo("🔧 Configuration:")
            click.echo(f"   Source: {config.source_dir}")
            click.echo(f"   Output: {config.output_dir}")
            click.echo(f"   Canvas Mode: {config.canvas_mode}")
            click.echo("")

        # Initialize converter
        converter = RSTConverter(config)

        # Perform conversion
        click.echo("🚀 Starting conversion...")
        success_count, total_files = converter.convert_all_files()

        # Display results
        click.echo("")
        summary = converter.get_conversion_summary(success_count, total_files)
        click.echo(summary)

        # Exit with appropriate code
        if success_count == total_files:
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        if verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
