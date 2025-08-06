"""
Pygments-based code highlighting processor for inline styles
"""

from __future__ import annotations

import re

try:
    from pygments import highlight
    from pygments.lexers import get_lexer_by_name
    from pygments.formatters import HtmlFormatter
    from pygments.util import ClassNotFound

    PYGMENTS_AVAILABLE = True
except ImportError:
    PYGMENTS_AVAILABLE = False


class PygmentsProcessor:
    """Process code blocks with Pygments for inline styling"""

    def __init__(self, style: str = "xcode", line_numbers: bool = False):
        self.style = style
        self.line_numbers = line_numbers
        self.formatter = None

        if PYGMENTS_AVAILABLE:
            self.formatter = HtmlFormatter(
                style=self.style,
                linenos=False,  # Disable line numbers
                cssclass="highlight",
                wrapcode=True,
                noclasses=True,  # This generates inline styles
                nobackground=False,
                anchorlinenos=False,
            )

    def process_html_code_blocks(self, html_content: str) -> str:
        """Process all code blocks in HTML content with Pygments highlighting"""
        if not PYGMENTS_AVAILABLE or not self.formatter:
            return html_content

        # Pattern to match code blocks with language class
        code_pattern = r'<pre class="code ([^"]+) literal-block"[^>]*><code[^>]*>(.*?)</code></pre>'

        def replace_code_block(match):
            language = match.group(1).strip()
            code_content = match.group(2)

            # Decode HTML entities in code content
            code_content = self._decode_html_entities(code_content)

            # Remove any existing HTML tags from code content
            code_content = re.sub(r"<[^>]+>", "", code_content)

            try:
                # Get lexer for the language
                if language.lower() in ["cpp", "c++", "arduino"]:
                    lexer = get_lexer_by_name("cpp", stripall=True)
                elif language.lower() in ["c"]:
                    lexer = get_lexer_by_name("c", stripall=True)
                elif language.lower() in ["python", "py"]:
                    lexer = get_lexer_by_name("python", stripall=True)
                elif language.lower() in ["javascript", "js"]:
                    lexer = get_lexer_by_name("javascript", stripall=True)
                elif language.lower() in ["html"]:
                    lexer = get_lexer_by_name("html", stripall=True)
                elif language.lower() in ["css"]:
                    lexer = get_lexer_by_name("css", stripall=True)
                else:
                    # Try to guess the lexer or fall back to text
                    try:
                        lexer = get_lexer_by_name(language, stripall=True)
                    except ClassNotFound:
                        lexer = get_lexer_by_name("text", stripall=True)

                # Highlight the code
                highlighted = highlight(code_content, lexer, self.formatter)

                # Apply additional styling to match hilite.me style
                highlighted = self._apply_hilite_style(highlighted)

                return highlighted

            except Exception:
                # If highlighting fails, return original content with basic styling
                return self._create_fallback_code_block(code_content)

        # Replace all code blocks
        processed_html = re.sub(
            code_pattern, replace_code_block, html_content, flags=re.DOTALL
        )

        return processed_html

    def _decode_html_entities(self, html_text: str) -> str:
        """Decode common HTML entities"""
        html_text = html_text.replace("&lt;", "<")
        html_text = html_text.replace("&gt;", ">")
        html_text = html_text.replace("&amp;", "&")
        html_text = html_text.replace("&quot;", '"')
        html_text = html_text.replace("&#39;", "'")
        return html_text

    def _apply_hilite_style(self, highlighted_html: str) -> str:
        """Apply hilite.me-like styling to the highlighted code"""
        # Wrap in a styled div similar to hilite.me output
        styled_html = highlighted_html.replace(
            '<div class="highlight">',
            '<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">',
        )

        # Ensure line numbers table has proper styling
        if 'class="linenos"' in styled_html:
            styled_html = styled_html.replace(
                'class="linenos"',
                'style="background-color: #f0f0f0; padding-right: 10px; text-align: right; user-select: none;"',
            )

        return styled_html

    def _create_fallback_code_block(self, code_content: str) -> str:
        """Create a fallback styled code block when Pygments fails"""
        escaped_code = (
            code_content.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
        )

        lines = escaped_code.split("\n")
        line_numbers = "\n".join(str(i + 1) for i in range(len(lines)))
        code_lines = "\n".join(f"<span></span>{line}" for line in lines)

        return f"""<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
<table><tr>
<td><pre style="margin: 0; line-height: 125%; background-color: #f0f0f0; padding-right: 10px; text-align: right; user-select: none;">{line_numbers}</pre></td>
<td><pre style="margin: 0; line-height: 125%;">{code_lines}</pre></td>
</tr></table>
</div>"""


def create_pygments_processor() -> PygmentsProcessor:
    """Factory function to create a PygmentsProcessor"""
    return PygmentsProcessor(style="xcode", line_numbers=False)
