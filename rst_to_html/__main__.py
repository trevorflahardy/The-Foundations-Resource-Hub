#!/usr/bin/env python3
"""
RST to HTML Converter CLI

A clean, modular command-line interface for converting RST files to HTML
with CSS inlining and Canvas LMS compatibility.
"""

if __name__ == "__main__":
    from .cli import main

    main()
