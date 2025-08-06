"""
HTML processing utilities for RST to HTML conversion
"""

from __future__ import annotations

import re


class HTMLProcessor:
    """Handles HTML post-processing tasks"""

    @staticmethod
    def clean_system_messages(html_content: str) -> str:
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

    @staticmethod
    def normalize_code_elements(html_content: str) -> str:
        """Ensure code spans are properly formatted"""
        # Convert docutils literal spans to proper code elements
        html_content = re.sub(
            r'<span class="docutils literal[^"]*">([^<]*)</span>',
            r'<code class="docutils literal">\1</code>',
            html_content,
        )

        return html_content

    @staticmethod
    def process_ref_links(html_content: str) -> str:
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

    @staticmethod
    def wrap_tables(html_content: str) -> str:
        """Wrap tables in centering divs for better layout"""
        # Find tables and wrap them
        html_content = re.sub(
            r'(<table[^>]*class="docutils"[^>]*>.*?</table>)',
            r'<div class="table-wrapper">\1</div>',
            html_content,
            flags=re.DOTALL,
        )

        return html_content

    @classmethod
    def process_html(cls, html_content: str) -> str:
        """Apply all HTML processing steps"""
        html_content = cls.clean_system_messages(html_content)
        html_content = cls.normalize_code_elements(html_content)
        html_content = cls.process_ref_links(html_content)
        html_content = cls.wrap_tables(html_content)

        return html_content
