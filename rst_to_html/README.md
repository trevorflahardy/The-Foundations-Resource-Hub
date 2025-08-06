# RST to HTML Converter

A clean, modular Python package for converting RST (reStructuredText) files to HTML with CSS inlining and Canvas LMS compatibility.

## Features

- **Clean modular architecture** - Well-organized code split into logical modules
- **Canvas LMS compatibility** - Aggressive CSS overrides to ensure styling works in Canvas
- **Syntax highlighting** - Preserves code block syntax highlighting with Pygments
- **CSS inlining** - Embeds all CSS directly into HTML for portability
- **Batch conversion** - Converts entire directory trees of RST files
- **Static file handling** - Automatically copies images and other static assets
- **Configurable** - Flexible configuration system with sensible defaults

## Architecture

The package is organized into several clean modules:

```
rst_to_html/
├── __init__.py           # Package exports and version info
├── __main__.py           # Package entry point
├── cli.py                # Command-line interface
├── config.py             # Configuration management
├── converter.py          # Main conversion logic
├── css_manager.py        # CSS generation and inlining
├── html_processor.py     # HTML post-processing utilities
├── sphinx_directives.py  # Sphinx directive handling
├── file_utils.py         # File system utilities
└── README.md            # This file
```

## Usage

### Command Line

```bash
# Basic usage with defaults
python -m rst_to_html

# Custom directories with verbose output
python -m rst_to_html --source-dir my_docs --output-dir build/html -v

# Disable Canvas LMS compatibility
python -m rst_to_html --no-canvas

# Show help
python -m rst_to_html --help
```

### Programmatic Usage

```python
from rst_to_html import RSTConverter, Config

# Create configuration
config = Config.from_args(
    source_dir="docs",
    output_dir="build/html",
    verbose=True,
    canvas_mode=True
)

# Initialize and run converter
converter = RSTConverter(config)
success_count, total_files = converter.convert_all_files()

print(converter.get_conversion_summary(success_count, total_files))
```

## Configuration

The `Config` class provides flexible configuration options:

- **Paths**: `source_dir`, `output_dir`, `css_dir`
- **Behavior**: `verbose`, `canvas_mode`, `aggressive_css_override`
- **Docutils settings**: Encoding, header levels, syntax highlighting
- **Static files**: Which directories to copy, which CSS files to include

## Canvas LMS Compatibility

When `canvas_mode=True` (default), the converter applies aggressive CSS overrides to ensure styling works properly in Canvas LMS:

- High-specificity selectors to override Canvas defaults
- `!important` declarations on critical styles
- Canvas-compatible font families and colors
- Preserved syntax highlighting even when Canvas strips external CSS

## Dependencies

- **docutils** - RST parsing and HTML generation
- **click** - Command-line interface
- **pathlib** - Modern path handling (built-in)

## Development

The modular architecture makes the code easy to extend and maintain:

- **Separation of concerns** - Each module has a single responsibility
- **Type hints** - Full type annotation for better IDE support
- **Error handling** - Comprehensive error handling and reporting
- **Testable** - Clean interfaces make unit testing straightforward

## License

This package is part of The Arduino Guide curriculum project.
