"""
Sphinx directive handling for RST to HTML conversion
"""

from __future__ import annotations

import re
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class AdmonitionDirective(Directive):
    """Handle admonition directives like note, tip, warning as styled blockquotes"""

    has_content: bool = True
    optional_arguments: int = 1
    final_argument_whitespace: bool = True
    option_spec: dict[str, object] = {}

    def run(self) -> list[nodes.Node]:
        """Create blockquote with inline styles for Canvas compatibility"""
        admonition_type = self.name.lower()

        # Create a blockquote container with inline styles
        blockquote = nodes.block_quote()

        # Define styles for different admonition types
        style_map = {
            "note": "background-color: #e7f3ff; border-left: 4px solid #007bff; color: #004085;",
            "tip": "background-color: #e8f5e8; border-left: 4px solid #28a745; color: #155724;",
            "warning": "background-color: #fff8e1; border-left: 4px solid #ffc107; color: #856404;",
            "caution": "background-color: #fef2e7; border-left: 4px solid #fd7e14; color: #7a3b0e;",
            "danger": "background-color: #fce8e8; border-left: 4px solid #dc3545; color: #721c24;",
            "important": "background-color: #f0e8ff; border-left: 4px solid #6610f2; color: #3a0845;",
            "seealso": "background-color: #e8f7fa; border-left: 4px solid #17a2b8; color: #0c5460;",
            "attention": "background-color: #fef2e7; border-left: 4px solid #fd7e14; color: #7a3b0e;",
            "hint": "background-color: #e8f7fa; border-left: 4px solid #17a2b8; color: #0c5460;",
            "error": "background-color: #fce8e8; border-left: 4px solid #dc3545; color: #721c24;",
        }

        base_style = "margin: 1em 0; padding: 12px; border-radius: 4px; font-family: Arial, sans-serif;"
        admonition_style = base_style + style_map.get(
            admonition_type,
            "background-color: #f8f9fa; border-left: 4px solid #6c757d; color: #495057;",
        )

        # Add the style attribute to the blockquote
        blockquote.attributes["style"] = admonition_style

        # Create title mapping
        title_map = {
            "note": "Note",
            "tip": "Tip",
            "warning": "Warning",
            "caution": "Caution",
            "danger": "Danger",
            "important": "Important",
            "seealso": "See Also",
            "attention": "Attention",
            "hint": "Hint",
            "error": "Error",
        }

        title_text = title_map.get(admonition_type, admonition_type.title())

        # Create the first paragraph with bold title
        title_para = nodes.paragraph()
        title_para.attributes["style"] = "margin: 0 0 8px 0; font-weight: bold;"
        title_strong = nodes.strong()
        title_strong += nodes.Text(f"{title_text}:")
        title_para += title_strong

        # Add the title paragraph to blockquote
        blockquote += title_para

        # If we have content, parse and add it as separate paragraphs
        if self.content:
            # Parse the content into a temporary container
            content_container = nodes.container()
            self.state.nested_parse(
                self.content, self.content_offset, content_container
            )

            # Add all content as separate nodes
            for content_node in content_container.children:
                blockquote += content_node

        return [blockquote]


class SilentDirective(Directive):
    """A directive that silently handles unknown Sphinx directives"""

    has_content: bool = True
    optional_arguments: int = 10
    final_argument_whitespace: bool = True
    option_spec: dict[str, object] = {}

    def run(self) -> list[nodes.Node]:
        """Return the content as raw text in a paragraph"""
        if self.content:
            text = "\n".join(self.content)
            para = nodes.paragraph()
            para += nodes.Text(text)
            return [para]
        return []


def ref_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """Handle :ref: role by extracting and formatting the link text"""
    if options is None:
        options = {}
    if content is None:
        content = []

    # Parse :ref:`Link Text <target>` or :ref:`target`
    ref_pattern = r"^([^<>]*?)(?:\s*<([^<>]+)>)?$"
    match = re.match(ref_pattern, text.strip())

    if match:
        link_text = match.group(1).strip()
        target = match.group(2)

        # If no explicit link text, use the target
        if not link_text and target:
            link_text = target.replace("_", " ").title()
        elif not link_text:
            link_text = text

        # Create a strong (bold) node for the reference
        strong_node = nodes.strong()
        strong_node += nodes.Text(link_text)
        return [strong_node], []
    else:
        # Fallback: just make it bold
        strong_node = nodes.strong()
        strong_node += nodes.Text(text)
        return [strong_node], []


class WholeCodeBlockDirective(Directive):
    """Handle whole-code-block directive with green border and explanatory text"""

    has_content: bool = True
    required_arguments: int = 1
    optional_arguments: int = 0
    final_argument_whitespace: bool = False
    option_spec: dict[str, object] = {}

    def run(self) -> list[nodes.Node]:
        """Create a code block with green border and explanatory text"""
        # Get the language from the first argument
        language = self.arguments[0] if self.arguments else "text"

        # Create the container div for the whole code block
        container = nodes.container()
        container.attributes["style"] = (
            "border: 2px solid #22c55e; "
            "border-radius: 6px; "
            "margin: 1em 0; "
            "overflow: hidden; "
            "background-color: white;"
        )

        # Create the code block
        code_content = "\n".join(self.content)

        # Create a literal block (code block)
        code_block = nodes.literal_block()
        code_block.attributes["classes"] = ["code", language]
        code_block.attributes["xml:space"] = "preserve"
        code_block += nodes.Text(code_content)

        # Add some styling to the code block to remove default margins
        code_block.attributes["style"] = (
            "margin: 0; " "border-radius: 0; " "border: none;"
        )

        container.append(code_block)

        # Create the explanatory text div
        explanation_div = nodes.container()
        explanation_div.attributes["style"] = (
            "background-color: #dcfce7; "
            "color: #166534; "
            "padding: 0.5em 1em; "
            "border-top: 1px solid #22c55e; "
            "font-size: 0.9em; "
            "font-family: Arial, sans-serif;"
        )

        # Add the explanatory text
        explanation_text = nodes.paragraph()
        explanation_text.attributes["style"] = "margin: 0;"
        explanation_text += nodes.Text(
            "This is a whole code block. It can be copy pasted by itself in your Arduino IDE."
        )

        explanation_div.append(explanation_text)
        container.append(explanation_div)

        return [container]


def register_sphinx_directives() -> None:
    """Register handlers for common Sphinx directives and roles"""

    # Register admonition directives
    admonition_directives = [
        "note",
        "tip",
        "warning",
        "caution",
        "danger",
        "important",
        "seealso",
        "attention",
        "hint",
        "error",
    ]

    for directive_name in admonition_directives:
        directives.register_directive(directive_name, AdmonitionDirective)

    # Register the whole-code-block directive
    directives.register_directive("whole-code-block", WholeCodeBlockDirective)

    # Register the ref role
    from docutils.parsers.rst import roles

    roles.register_local_role("ref", ref_role)

    # Register silent directives for other Sphinx-specific directives
    sphinx_directives = [
        # Cross-referencing (non-role)
        "doc",
        "download",
        "numref",
        "eq",
        "term",
        "abbr",
        # UI elements
        "guilabel",
        "menuselection",
        "kbd",
        "command",
        "option",
        "envvar",
        "file",
        "samp",
        "dfn",
        # Content organization
        "index",
        "centered",
        "hlist",
        "glossary",
        "productionlist",
        "tabularcolumns",
        "rubric",
        # Code documentation
        "currentmodule",
        "automodule",
        "autoclass",
        "autofunction",
        "autodata",
        "automethod",
        "autoattribute",
        "autoexception",
        # Version and metadata
        "deprecated",
        "versionadded",
        "versionchanged",
        "sectionauthor",
        "codeauthor",
        # Conditional content
        "only",
        "ifconfig",
        # Task management
        "todo",
        "todolist",
        # Custom directives
        "quizdown",
    ]

    for directive_name in sphinx_directives:
        directives.register_directive(directive_name, SilentDirective)
