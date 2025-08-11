"""
Sphinx directive handling for RST to HTML conversion
"""

from __future__ import annotations

import re
from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import ViewList


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


def term_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """Handle :term: role by outputting bold text without links.

    Supports both forms:
    - :term:`Display Text <target>` -> strong(Display Text)
    - :term:`target` -> strong(target)
    """
    if options is None:
        options = {}
    if content is None:
        content = []

    # Parse `Display Text <target>` or `target`
    match = re.match(r"^([^<>]*?)(?:\s*<([^<>]+)>)?$", text.strip())
    if match:
        display = match.group(1).strip()
        target = match.group(2)
        if not display:
            display = target if target else text

        strong_node = nodes.strong()
        strong_node += nodes.Text(display)
        return [strong_node], []
    # Fallback
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


class WholeLiteralIncludeDirective(Directive):
    """Handle whole-literal-include directive to include external file content as a whole code block"""

    has_content: bool = (
        False  # This directive doesn't have content, it includes external files
    )
    required_arguments: int = 1  # The file path argument is required
    optional_arguments: int = 0
    final_argument_whitespace: bool = True
    option_spec: dict[str, object] = {
        "language": directives.unchanged,  # Language for syntax highlighting
        "encoding": directives.encoding,  # File encoding
    }

    def run(self) -> list[nodes.Node]:
        """Read external file and create a whole code block with its content"""
        from pathlib import Path

        # Get the file path from the first argument
        include_file_path = self.arguments[0]

        # Get options
        language = self.options.get("language", "text")
        encoding = self.options.get("encoding", "utf-8")

        # Resolve the file path relative to the current document's directory
        # The source is available in self.state.document.settings.env.srcdir for Sphinx,
        # but we're using docutils directly, so we need to get it differently
        source_dir = Path(self.state.document.attributes.get("source", ".")).parent
        file_path = source_dir / include_file_path

        try:
            # Read the file content
            with open(file_path, "r", encoding=encoding) as f:
                file_content = f.read()

            # Create the container div for the whole code block
            container = nodes.container()
            container.attributes["style"] = (
                "border: 2px solid #22c55e; "
                "border-radius: 6px; "
                "margin: 1em 0; "
                "overflow: hidden; "
                "background-color: white;"
            )

            # Create a literal block (code block) with the file content
            code_block = nodes.literal_block()
            code_block.attributes["classes"] = ["code", language]
            code_block.attributes["xml:space"] = "preserve"
            code_block += nodes.Text(file_content)

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

        except FileNotFoundError:
            # If file not found, create an error message
            error_msg = f"File not found: {include_file_path}"
            error_para = nodes.paragraph()
            error_para.attributes["style"] = "color: red; font-weight: bold;"
            error_para += nodes.Text(error_msg)
            return [error_para]

        except UnicodeDecodeError as e:
            # If file encoding error, create an error message
            error_msg = f"Encoding error reading {include_file_path}: {str(e)}"
            error_para = nodes.paragraph()
            error_para.attributes["style"] = "color: red; font-weight: bold;"
            error_para += nodes.Text(error_msg)
            return [error_para]

        except Exception as e:
            # For any other error, create a general error message
            error_msg = f"Error including {include_file_path}: {str(e)}"
            error_para = nodes.paragraph()
            error_para.attributes["style"] = "color: red; font-weight: bold;"
            error_para += nodes.Text(error_msg)
            return [error_para]


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

    # Register the whole-literal-include directive
    directives.register_directive("whole-literal-include", WholeLiteralIncludeDirective)

    # Register the ref and term roles
    from docutils.parsers.rst import roles

    roles.register_local_role("ref", ref_role)
    roles.register_local_role("term", term_role)

    # Register silent directives for other Sphinx-specific directives
    sphinx_directives = [
        # Cross-referencing (non-role)
        "doc",
        "download",
        "numref",
        "eq",
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

    # Register a custom glossary directive to render a styled grid of terms
    directives.register_directive("glossary", GlossaryDirective)


class GlossaryDirective(Directive):
    """Render a beautiful glossary as a grid of term cards (Canvas-friendly).

    Expected content format (typical Sphinx glossary):

    Term One
      Definition paragraph 1

    Term Two
      Definition paragraph...
    """

    has_content: bool = True
    optional_arguments: int = 0
    final_argument_whitespace: bool = False
    option_spec: dict[str, object] = {}

    def run(self) -> list[nodes.Node]:
        # Outer grid container
        grid = nodes.container(
            classes=["glossary-grid"]
        )  # class retained for possible future hooks
        grid.attributes["style"] = (
            "display: grid; "
            "grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); "
            "gap: 12px; "
            "margin: 1em 0;"
        )

        lines = list(self.content)
        i = 0
        n = len(lines)

        def is_term_line(s: str) -> bool:
            return bool(s.strip()) and not s.startswith(" ") and not s.startswith("\t")

        # Parse term/definition blocks
        while i < n:
            # Skip blank lines
            while i < n and not lines[i].strip():
                i += 1
            if i >= n:
                break

            if not is_term_line(lines[i]):
                # If malformed, skip this line
                i += 1
                continue

            term_text = lines[i].strip()
            i += 1

            # Collect indented definition lines until next term
            def_lines: list[str] = []
            while i < n and (
                not lines[i].strip()
                or lines[i].startswith(" ")
                or lines[i].startswith("\t")
            ):
                def_lines.append(lines[i])
                i += 1

            # Build the card
            card = nodes.container(classes=["glossary-item"])
            card.attributes["style"] = (
                "border: 1px solid #e2e8f0; "
                "border-radius: 8px; "
                "background-color: white; "
                "overflow: hidden;"
            )

            # Term header
            header = nodes.paragraph()
            header.attributes["style"] = (
                "margin: 0; padding: 8px 12px; "
                "background-color: #f8fafc; "
                "border-bottom: 1px solid #e2e8f0; "
                "font-weight: 700;"
            )
            strong = nodes.strong()
            strong += nodes.Text(term_text)
            header += strong
            card += header

            # Definition body
            body = nodes.container()
            body.attributes["style"] = (
                "padding: 8px 12px; margin: 0; background-color: white;"
            )

            # Dedent up to 2 leading spaces (typical glossary formatting)
            vl = ViewList()
            for raw in def_lines:
                if raw.startswith("  "):
                    vl.append(raw[2:], source="<glossary>")
                elif raw.startswith("\t"):
                    vl.append(raw[1:], source="<glossary>")
                else:
                    vl.append(raw, source="<glossary>")

            if len(vl) == 0:
                # Ensure there's at least an empty paragraph to keep layout consistent
                para = nodes.paragraph()
                para += nodes.Text("")
                body += para
            else:
                self.state.nested_parse(vl, self.content_offset, body)

            card += body
            grid += card

        return [grid]
