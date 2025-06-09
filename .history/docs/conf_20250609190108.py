# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os

sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("extensions"))

# Append the examples directory (in the parent of this one) such that the
# examples can be included in the documentation.
examples_path = os.path.abspath("../examples")
sys.path.append(examples_path)

project = "The Arduino Guide"
copyright = "2025, Trevor Flahardy"
author = "Trevor Flahardy"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "whole_code_block",
    "sphinxcontrib.quizdown",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
]

# -- Quizdown integration -------------------------------------------------
html_css_files = [
    "whole_code_block.css",
]

# Global configuration for sphinxcontrib-quizdown
quizdown_config = {
    "start_on_load": True,
    "shuffle_answers": True,
    "shuffle_questions": False,
    "primary_color": "#FF851B",
    "secondary_color": "#DDDDDD",
    "text_color": "black",
}

templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_experimental_html5_writer = True

html_theme = "furo"
html_theme_options = {
    "navigation_with_keys": True,
    "light_css_variables": {
        "color-brand-primary": "#006747",
        "color-brand-content": "006747",
    },
    "dark_css_variables": {
        "color-brand-primary": "#009374",
        "color-brand-content": "#009374",
    },
    "sidebar_hide_name": True,
}

html_extra_path = [examples_path]

html_logo = "_static/the_arduino_guide.png"

html_static_path = ["_static", "images"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "The Arduino Guide"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Arduino Guide"


html_favicon = "_static/favicon.ico"

# Changes the default pygments style to Arduino style
arduino_style = "arduino"

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        "index",
        "arduino_tutorial.tex",
        "The Arduino Guide",
        "Arduino Tutorial",
        "manual",
    ),
]


nitpicky = True
