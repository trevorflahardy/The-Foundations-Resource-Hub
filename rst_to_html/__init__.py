"""
RST to HTML Converter Package

A modular package for converting RST files to HTML with CSS inlining
and Canvas LMS compatibility.
"""

__version__ = "1.0.0"
__author__ = "Arduino Guide Team"

from .converter import RSTConverter
from .config import Config

__all__ = ["RSTConverter", "Config"]
