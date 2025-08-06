"""
HTML processing utilities for RST to HTML conversion
"""

from __future__ import annotations

import re

from .pygments_processor import create_pygments_processor


class HTMLProcessor:
    """Handles HTML post-processing tasks"""

    def __init__(self):
        self.pygments_processor = create_pygments_processor()

    def process_code_highlighting(self, html_content: str) -> str:
        """Apply Pygments highlighting to code blocks"""
        return self.pygments_processor.process_html_code_blocks(html_content)

    def clean_system_messages(self, html_content: str) -> str:
        """Remove docutils system messages from HTML content"""
        # Remove system message divs
        html_content = re.sub(
            r'<div class="system-message".*?</div>', "", html_content, flags=re.DOTALL
        )

        # Remove problematic class references but preserve content
        html_content = re.sub(
            r'<div class="problematic"[^>]*>(.*?)</div>', r"\1", html_content
        )

        return html_content

    def normalize_code_elements(self, html_content: str) -> str:
        """Ensure code spans are properly formatted"""
        # Convert docutils literal spans to proper code elements
        html_content = re.sub(
            r'<span class="docutils literal[^"]*">([^<]*)</span>',
            r'<code class="docutils literal">\1</code>',
            html_content,
        )

        return html_content

    def process_ref_links(self, html_content: str) -> str:
        """Convert remaining :ref: patterns to bold text"""
        # Pattern 1: :ref:`Link Text <target>`
        html_content = re.sub(
            r":ref:`([^<>`]+)\s*<[^<>`]*>`", r"<strong>\1</strong>", html_content
        )

        # Pattern 2: :ref:`target` (no explicit text)
        html_content = re.sub(
            r":ref:`([^<>`]+)`",
            lambda m: f'<strong>{m.group(1).replace("_", " ").title()}</strong>',
            html_content,
        )

        return html_content

    def wrap_tables(self, html_content: str) -> str:
        """Wrap tables in centering divs for better layout"""
        # Find tables and wrap them
        html_content = re.sub(
            r'(<table[^>]*class="docutils"[^>]*>.*?</table>)',
            r'<div class="table-wrapper">\1</div>',
            html_content,
            flags=re.DOTALL,
        )

        return html_content

    def style_admonitions(self, html_content: str) -> str:
        """Convert blockquote admonitions to proper div admonitions with inline styling"""
        import re

        def convert_blockquote_admonition(match):
            blockquote_content = match.group(1)

            # Extract the title from the strong tag - it should be the first word before the colon
            title_match = re.search(r"<strong>([^:]+):", blockquote_content)
            if not title_match:
                return match.group(0)  # Return unchanged if no title found

            title = title_match.group(1).strip()
            title_lower = title.lower()

            # Define styles for different admonition types using Canvas-compatible inline styles
            # Now using separate colors for title background and border
            style_map = {
                "note": {
                    "border_color": "#007bff",
                    "title_background": "#e7f3ff",
                    "title_color": "#004085",
                },
                "tip": {
                    "border_color": "#28a745",
                    "title_background": "#e8f5e8",
                    "title_color": "#155724",
                },
                "warning": {
                    "border_color": "#ffc107",
                    "title_background": "#fff8e1",
                    "title_color": "#856404",
                },
                "caution": {
                    "border_color": "#fd7e14",
                    "title_background": "#fef2e7",
                    "title_color": "#7a3b0e",
                },
                "danger": {
                    "border_color": "#dc3545",
                    "title_background": "#fce8e8",
                    "title_color": "#721c24",
                },
                "important": {
                    "border_color": "#6610f2",
                    "title_background": "#f0e8ff",
                    "title_color": "#3a0845",
                },
                "see also": {
                    "border_color": "#17a2b8",
                    "title_background": "#e8f7fa",
                    "title_color": "#0c5460",
                },
                "attention": {
                    "border_color": "#fd7e14",
                    "title_background": "#fef2e7",
                    "title_color": "#7a3b0e",
                },
                "hint": {
                    "border_color": "#17a2b8",
                    "title_background": "#e8f7fa",
                    "title_color": "#0c5460",
                },
                "error": {
                    "border_color": "#dc3545",
                    "title_background": "#fce8e8",
                    "title_color": "#721c24",
                },
            }

            # Get styles for this admonition type
            styles = style_map.get(
                title_lower,
                {
                    "border_color": "#6c757d",
                    "title_background": "#f8f9fa",
                    "title_color": "#495057",
                },
            )

            # Build the admonition div with inline styles - white background with colored border
            admonition_style = (
                f"background-color: white; "
                f"border: 1px solid {styles['border_color']}; "
                f"border-left: 4px solid {styles['border_color']}; "
                f"color: #333333; "
                f"margin: 1em 0; "
                f"padding: 0; "
                f"border-radius: 4px; "
                f"font-family: Arial, sans-serif; "
                f"overflow: hidden;"
            )

            # Title banner with colored background
            title_style = (
                f"background-color: {styles['title_background']}; "
                f"color: {styles['title_color']}; "
                f"font-weight: bold; "
                f"margin: 0; "
                f"padding: 0.5em 1em; "
                f"font-size: 1em; "
                f"line-height: 1.2; "
                f"border-bottom: 1px solid {styles['border_color']};"
            )

            # Content area styling
            content_style = (
                "padding: 0.5em 1em; " "margin: 0; " "background-color: white;"
            )

            # Remove the strong tag from the content and extract the title
            content_without_title = re.sub(
                r"<p[^>]*><strong>[^:]+:[^<]*</strong>([^<]*)</p>",
                lambda m: f"<p>{m.group(1).strip()}</p>" if m.group(1).strip() else "",
                blockquote_content,
            )

            # Clean up any empty paragraphs
            content_without_title = re.sub(r"<p>\s*</p>", "", content_without_title)

            # Remove any remaining content from the first paragraph that was part of the title line
            first_p_match = re.search(
                r"<p[^>]*><strong>[^:]+:[^<]*</strong>([^<]*)</p>(.*)",
                blockquote_content,
                re.DOTALL,
            )
            if first_p_match:
                remaining_first_p_content = first_p_match.group(1).strip()
                rest_of_content = first_p_match.group(2)

                if remaining_first_p_content:
                    content_without_title = (
                        f"<p>{remaining_first_p_content}</p>{rest_of_content}"
                    )
                else:
                    content_without_title = rest_of_content

            return (
                f'<div class="admonition {title_lower}" style="{admonition_style}">'
                f'<p class="admonition-title" style="{title_style}">{title}</p>'
                f'<div class="admonition-content" style="{content_style}">'
                f"{content_without_title}"
                f"</div>"
                f"</div>"
            )

        # Find blockquotes with strong titles (our admonitions)
        pattern = r"<blockquote[^>]*>(.*?)</blockquote>"

        def check_and_convert(match):
            content = match.group(1)
            # Only convert if it starts with a strong tag containing a colon (admonition pattern)
            if re.search(r"<p[^>]*><strong>[^<]+:", content):
                return convert_blockquote_admonition(match)
            return match.group(0)

        html_content = re.sub(pattern, check_and_convert, html_content, flags=re.DOTALL)

        return html_content

    def style_whole_code_blocks(self, html_content: str) -> str:
        """Style whole code blocks with green border and explanatory text"""
        import re

        # Look for the pattern: outer container div with inner highlight div and explanation div
        pattern = r'<div class="docutils container">(.*?)<div class="docutils container">\s*<p>([^<]*whole code block[^<]*)</p>\s*</div>\s*</div>'

        def convert_whole_code_block(match):
            code_content = match.group(1).strip()
            explanation_text = match.group(2).strip()

            # Create the styled whole code block
            styled_html = (
                f'<div class="whole-code-block" style="'
                f"border: 2px solid #22c55e; "
                f"border-radius: 6px; "
                f"margin: 1em 0; "
                f"overflow: hidden; "
                f'background-color: white;">'
                f"{code_content}"
                f'<div class="whole-code-block-explanation" style="'
                f"background-color: #dcfce7; "
                f"color: #166534; "
                f"padding: 0.5em 1em; "
                f"border-top: 1px solid #22c55e; "
                f"font-size: 0.9em; "
                f"font-family: Arial, sans-serif; "
                f'margin: 0;">'
                f'<p style="margin: 0;">{explanation_text}</p>'
                f"</div>"
                f"</div>"
            )

            return styled_html

        html_content = re.sub(
            pattern, convert_whole_code_block, html_content, flags=re.DOTALL
        )

        return html_content

    def process_html(self, html_content: str) -> str:
        """Apply all HTML processing steps"""
        html_content = self.clean_system_messages(html_content)
        html_content = self.normalize_code_elements(html_content)
        html_content = self.process_code_highlighting(html_content)
        html_content = self.process_ref_links(html_content)
        html_content = self.style_admonitions(html_content)
        html_content = self.style_whole_code_blocks(html_content)
        html_content = self.wrap_tables(html_content)

        return html_content
