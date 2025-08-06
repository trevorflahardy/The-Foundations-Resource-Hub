"""
CSS management and styling for RST to HTML conversion
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import List


class CSSManager:
    """Manages CSS generation, inlining, and Canvas LMS compatibility"""

    def __init__(self, source_dir: Path | None = None, canvas_mode: bool = True):
        self.source_dir = source_dir
        self.canvas_mode = canvas_mode

    def get_base_css(self) -> str:
        """Generate base CSS for proper table and code formatting"""
        return """
/* Custom Table Styling */
table.docutils {
    border-collapse: collapse !important;
    border: 1px solid #ccc !important;
    margin: 1em auto !important;
    width: auto !important;
    max-width: 100% !important;
}

table.docutils th,
table.docutils td {
    border: 1px solid #ccc !important;
    padding: 8px 12px !important;
    text-align: left !important;
    vertical-align: top !important;
}

table.docutils th {
    font-weight: bold !important;
}

table.docutils tr:nth-child(even) {
    background-color: #f9f9f9 !important;
}

table.docutils tr:nth-child(odd) {
    background-color: transparent !important;
}

/* Code block styling */
.highlight,
pre.code {
    border: 1px solid #ddd !important;
    padding: 10px !important;
    margin: 1em 0 !important;
    overflow-x: auto !important;
    background-color: #f8f8f8 !important;
    font-family: 'Courier New', Consolas, Monaco, 'Liberation Mono', monospace !important;
    font-size: 14px !important;
    line-height: 1.4 !important;
}

pre {
    margin: 0 !important;
    white-space: pre-wrap !important;
    word-wrap: break-word !important;
    font-family: 'Courier New', Consolas, Monaco, 'Liberation Mono', monospace !important;
}

/* Inline code styling */
code.docutils.literal {
    background-color: #f5f5f5 !important;
    border: 1px solid #ddd !important;
    border-radius: 3px !important;
    padding: 2px 4px !important;
    font-family: 'Courier New', Consolas, Monaco, 'Liberation Mono', monospace !important;
    font-size: 90% !important;
    color: #333 !important;
}

code {
    font-family: 'Courier New', Consolas, Monaco, 'Liberation Mono', monospace !important;
    font-size: 90% !important;
    background-color: #f5f5f5 !important;
    padding: 2px 4px !important;
    border-radius: 3px !important;
    border: 1px solid #ddd !important;
}

/* Basic syntax highlighting */
.highlight .c,
.highlight .c1 { color: #8f5902 !important; font-style: italic !important; }
.highlight .k,
.highlight .kd,
.highlight .kt { color: #204a87 !important; font-weight: bold !important; }
.highlight .s,
.highlight .s2 { color: #4e9a06 !important; }
.highlight .n { color: #000000 !important; }
.highlight .o { color: #ce5c00 !important; font-weight: bold !important; }
.highlight .p { color: #000000 !important; font-weight: bold !important; }
.highlight .mi,
.highlight .m { color: #0000cf !important; font-weight: bold !important; }
.highlight .nc { color: #000000 !important; }
.highlight .nf { color: #000000 !important; }
.highlight .w { color: #f8f8f8 !important; }

/* Text formatting preservation */
strong, b {
    font-weight: bold !important;
}

em, i {
    font-style: italic !important;
}

/* Remove conflicting backgrounds */
body, html, div, p, span {
    background-color: transparent !important;
}

/* Table centering */
.table-wrapper {
    text-align: center !important;
    margin: 1em 0 !important;
}

.table-wrapper table {
    margin: 0 auto !important;
    display: inline-table !important;
}

.highlight .highlight {
    background: transparent !important;
}

/* Blockquote styling for Canvas compatibility */
blockquote {
    margin: 1em 0 !important;
    padding: 0 0 0 1em !important;
    border-left: 4px solid #ccc !important;
    font-style: normal !important;
    background-color: transparent !important;
}

blockquote p {
    margin: 0.5em 0 !important;
}

blockquote p:last-child {
    margin-bottom: 0 !important;
}
"""

    def get_canvas_override_css(self) -> str:
        """Generate aggressive Canvas LMS override CSS"""
        if not self.canvas_mode:
            return ""

        return """
/* Canvas LMS Override Styles - High Specificity */
div.highlight pre.code.cpp.literal-block code,
pre.code.cpp.literal-block code,
.highlight pre code,
.highlight code {
    font-family: 'Courier New', Consolas, Monaco, 'Liberation Mono', monospace !important;
    font-size: 14px !important;
    line-height: 1.4 !important;
    background-color: #f8f8f8 !important;
    padding: 0 !important;
    border: none !important;
    border-radius: 0 !important;
}

/* High-specificity syntax highlighting */
div.highlight span.k,
pre.code.cpp.literal-block code span.k,
.highlight .k { color: #204a87 !important; font-weight: bold !important; }

div.highlight span.kt,
pre.code.cpp.literal-block code span.kt,
.highlight .kt { color: #204a87 !important; font-weight: bold !important; }

div.highlight span.kd,
pre.code.cpp.literal-block code span.kd,
.highlight .kd { color: #204a87 !important; font-weight: bold !important; }

div.highlight span.c1,
pre.code.cpp.literal-block code span.c1,
.highlight .c1 { color: #8f5902 !important; font-style: italic !important; }

div.highlight span.c,
pre.code.cpp.literal-block code span.c,
.highlight .c { color: #8f5902 !important; font-style: italic !important; }

div.highlight span.s,
pre.code.cpp.literal-block code span.s,
.highlight .s { color: #4e9a06 !important; }

div.highlight span.s2,
pre.code.cpp.literal-block code span.s2,
.highlight .s2 { color: #4e9a06 !important; }

div.highlight span.mi,
pre.code.cpp.literal-block code span.mi,
.highlight .mi { color: #0000cf !important; font-weight: bold !important; }

div.highlight span.m,
pre.code.cpp.literal-block code span.m,
.highlight .m { color: #0000cf !important; font-weight: bold !important; }

div.highlight span.o,
pre.code.cpp.literal-block code span.o,
.highlight .o { color: #ce5c00 !important; font-weight: bold !important; }

div.highlight span.p,
pre.code.cpp.literal-block code span.p,
.highlight .p { color: #000000 !important; font-weight: bold !important; }

div.highlight span.n,
pre.code.cpp.literal-block code span.n,
.highlight .n { color: #000000 !important; }

div.highlight span.nc,
pre.code.cpp.literal-block code span.nc,
.highlight .nc { color: #000000 !important; }

div.highlight span.nf,
pre.code.cpp.literal-block code span.nf,
.highlight .nf { color: #000000 !important; }
"""

    def get_pygments_css_from_build(self) -> str:
        """Extract Pygments CSS from existing Sphinx build"""
        if not self.source_dir:
            return ""

        build_dir = self.source_dir / "_build" / "html"
        css_content = ""

        if build_dir.exists():
            static_dir = build_dir / "_static"
            if static_dir.exists():
                pygments_css = static_dir / "pygments.css"
                if pygments_css.exists():
                    try:
                        with open(pygments_css, "r", encoding="utf-8") as f:
                            content = f.read()
                            css_content = f"\n/* From pygments.css */\n{content}\n"
                    except Exception as e:
                        print(f"Warning: Could not read {pygments_css}: {e}")

        return css_content

    def load_custom_css_files(self, css_paths: List[Path]) -> str:
        """Load and combine custom CSS files"""
        combined_css = ""

        for css_path in css_paths:
            if css_path.exists():
                try:
                    with open(css_path, "r", encoding="utf-8") as f:
                        css_content = f.read()
                        combined_css += f"\n/* From {css_path.name} */\n{css_content}\n"
                except Exception as e:
                    print(f"Warning: Could not read CSS file {css_path}: {e}")

        return combined_css

    def generate_complete_css(self, custom_css_paths: List[Path] | None = None) -> str:
        """Generate complete CSS combining all sources"""
        css_parts = [
            self.get_base_css(),
            self.get_pygments_css_from_build(),
        ]

        if custom_css_paths:
            css_parts.append(self.load_custom_css_files(custom_css_paths))

        if self.canvas_mode:
            css_parts.append(self.get_canvas_override_css())

        return "\n".join(filter(None, css_parts))

    def remove_external_css_links(self, html_content: str) -> tuple[str, int]:
        """Remove external CSS links from HTML content"""
        css_link_pattern = r"<link[^>]*stylesheet[^>]*\.css[^>]*/?>"

        original_links = len(
            re.findall(css_link_pattern, html_content, flags=re.IGNORECASE)
        )

        html_content = re.sub(css_link_pattern, "", html_content, flags=re.IGNORECASE)

        remaining_links = len(
            re.findall(css_link_pattern, html_content, flags=re.IGNORECASE)
        )

        return html_content, original_links - remaining_links

    def inject_css_into_html(self, html_content: str, css_content: str) -> str:
        """Inject CSS content into HTML head section"""
        if not css_content:
            return html_content

        style_tag = f"<style>\n{css_content}\n</style>"

        # Insert before closing </head> tag
        if "</head>" in html_content:
            html_content = html_content.replace("</head>", f"{style_tag}\n</head>")
        else:
            # Fallback: add after <head> tag
            html_content = html_content.replace("<head>", f"<head>\n{style_tag}")

        return html_content
