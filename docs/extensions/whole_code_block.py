"""
MIT License

Copyright (c) 2019-present Luc1412

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import annotations


from docutils.nodes import Element, Node, TextElement
from sphinx.application import Sphinx
from sphinx.directives.code import CodeBlock, LiteralInclude
from sphinx.writers.html5 import HTML5Translator


class WholeCodeBlockNode(Element):
    # The parent node, holds the code block and the warning.
    pass


# Visits the whole code block node
def visit_whole_code_block_node(
    self: HTML5Translator, node: WholeCodeBlockNode
) -> None:
    # Returns the opening div tag for the whole code block
    self.body.append(self.starttag(node, "div", CLASS="whole-code-block"))


def depart_whole_code_block_node(
    self: HTML5Translator, node: WholeCodeBlockNode
) -> None:
    # Returns the closing div tag for the whole code block
    self.body.append("</div>")


class WholeCodeBlockWarning(Element):
    # Holds the warning at the bottom of the code block.
    ...


def visit_whole_code_block_warning(
    self: HTML5Translator, node: WholeCodeBlockWarning
) -> None:
    # Returns the div that actually holds the warning
    # Create some attributes so that the background is dc2626
    self.body.append(self.starttag(node, "div", CLASS="whole-code-block-warning"))


def depart_whole_code_block_warning(
    self: HTML5Translator, node: WholeCodeBlockWarning
) -> None:
    # Returns the closing div tag for the warning
    self.body.append("</div>")


class WholeCodeBlockWarningText(TextElement):
    # Holds the warning text.
    ...


def visit_whole_code_block_warning_text(
    self: HTML5Translator, node: WholeCodeBlockWarningText
) -> None:
    # Returns the opening p tag for the warning text
    self.body.append(self.starttag(node, "div", CLASS="whole-code-block-warning-text"))


def depart_whole_code_block_warning_text(
    self: HTML5Translator, node: WholeCodeBlockWarningText
) -> None:
    # Returns the closing p tag for the warning text
    self.body.append("</div>")


class WholeCodeBlock(CodeBlock):
    """A custom Sphinx directive that aims to add a warning to code blocks
    that to not work by themselves.

    .. whole-code-block:: <language>

        <code block>

    Generates the following HTML:

    <div class="whole-code-block"> # Holds the entire whole warning
        <pre class="literal-block /> # Holds the actual code block
        <div class="whole-code-block-warning"> # Holds the Warning
            <p>[Warning Text]</p> # The text of the warning. Notifies *when* the code block was last working.
        </div>
    </div>
    """

    has_content = True
    required_arguments = 1

    def run(self) -> list[Node]:
        # Create the main node that holds the code block and warning
        root = WholeCodeBlockNode()

        code_block: list[Node] = super().run()
        root += code_block

        # Create the underlying warning node
        warning = WholeCodeBlockWarning()
        root.append(warning)

        # The underlying warning text
        notification_text_raw = "This is a whole code block. It can be used by itself."
        warning_text = WholeCodeBlockWarningText(
            notification_text_raw, notification_text_raw
        )
        warning.append(warning_text)

        return [root]


class WholeLiteralInclude(LiteralInclude):
    """A custom Sphinx directive that acts the same as WholeCodeBlock except
    this is a literal include. This is such that an example can be included
    and still circled with the notification that it is a whole code block.
    """

    has_content = True
    required_arguments = 1

    def run(self) -> list[Node]:
        # Create the main node that holds the code block and warning
        root = WholeCodeBlockNode()

        code_block: list[Node] = super().run()
        root += code_block

        # Create the underlying warning node
        warning = WholeCodeBlockWarning()
        root.append(warning)

        # The underlying warning text
        notification_text_raw = "This is a whole code block. It can be used by itself."
        warning_text = WholeCodeBlockWarningText(
            notification_text_raw, notification_text_raw
        )
        warning.append(warning_text)

        return [root]


# The setup function for the extension
def setup(app: Sphinx):
    app.add_node(
        WholeCodeBlockNode,
        html=(visit_whole_code_block_node, depart_whole_code_block_node),
    )  # type: ignore
    app.add_node(
        WholeCodeBlockWarning,
        html=(visit_whole_code_block_warning, depart_whole_code_block_warning),
    )  # type: ignore
    app.add_node(  # type: ignore
        WholeCodeBlockWarningText,
        html=(
            visit_whole_code_block_warning_text,
            depart_whole_code_block_warning_text,
        ),
    )

    app.add_directive("whole-code-block", WholeCodeBlock)
    app.add_directive("whole-literal-include", WholeLiteralInclude)

    # Tell sphinx that it is okay for the exception hierarchy to be used in parallel
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
