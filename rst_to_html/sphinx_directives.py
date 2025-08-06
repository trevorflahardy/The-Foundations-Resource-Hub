"""
Sphinx directive handling for RST to HTML conversion
"""

from __future__ import annotations

import re
from docutils import nodes
from docutils.parsers.rst import Directive, directives


class AdmonitionDirective(Directive):
    """Handle admonition directives like note, tip, warning as blockquotes"""

    has_content: bool = True
    optional_arguments: int = 1
    final_argument_whitespace: bool = True
    option_spec: dict[str, object] = {}

    def run(self) -> list[nodes.Node]:
        """Create blockquote with bold title for Canvas compatibility"""
        admonition_type = self.name.lower()

        # Create a blockquote container
        blockquote = nodes.block_quote()

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
        if self.arguments:
            title_text = self.arguments[0]

        # Create the first paragraph with bold title
        title_para = nodes.paragraph()
        title_strong = nodes.strong()
        title_strong += nodes.Text(f"{title_text}: ")
        title_para += title_strong

        # If we have content, parse and add it
        if self.content:
            # Parse the content into a temporary container
            content_container = nodes.container()
            self.state.nested_parse(
                self.content, self.content_offset, content_container
            )

            # If there's content, merge it properly
            if content_container.children:
                first_content = content_container.children[0]

                # If the first content is a paragraph, merge with title
                if isinstance(first_content, nodes.paragraph):
                    # Add the content of the first paragraph to our title paragraph
                    for child in first_content.children:
                        title_para += child

                    # Add the merged paragraph to blockquote
                    blockquote += title_para

                    # Add any remaining paragraphs/content
                    for remaining in content_container.children[1:]:
                        blockquote += remaining
                else:
                    # If first content is not a paragraph, add title paragraph first
                    blockquote += title_para
                    # Then add all content
                    for content_node in content_container.children:
                        blockquote += content_node
            else:
                # No content, just add the title
                blockquote += title_para
        else:
            # No content, just add the title
            blockquote += title_para

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
