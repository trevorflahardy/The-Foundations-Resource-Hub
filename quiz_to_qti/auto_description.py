from __future__ import annotations

from pathlib import Path
import json
import re
import os
import urllib.request
import urllib.error
from typing import Iterable, List, Optional, Tuple


# Lightweight keywording to support fallback summarization
_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "for",
    "if",
    "in",
    "into",
    "is",
    "it",
    "no",
    "not",
    "of",
    "on",
    "or",
    "such",
    "that",
    "the",
    "their",
    "then",
    "there",
    "these",
    "they",
    "this",
    "to",
    "was",
    "with",
    "you",
    "your",
    "we",
    "our",
}

_WORD_RE = re.compile(r"[A-Za-z][A-Za-z0-9_\-]+")


def _tokenize(text: str) -> List[str]:
    toks = [t.lower() for t in _WORD_RE.findall(text)]
    return [t for t in toks if t not in _STOPWORDS and len(t) > 2]


def _read_text_safe(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        try:
            return p.read_text(errors="ignore")
        except Exception:
            return ""


def _score_overlap(doc_text: str, ref_tokens: set[str]) -> int:
    toks = set(_tokenize(doc_text))
    return len(toks & ref_tokens)


def _doc_title_from_path(p: Path) -> str:
    name = p.stem.replace("_", " ").replace("-", " ")
    title = re.sub(r"\s+", " ", name).strip().title()
    return title or p.stem


def _collect_quiz_seed(files: Iterable[Path]) -> Tuple[str, List[str]]:
    texts: List[str] = []
    headings: List[str] = []
    for f in files:
        t = _read_text_safe(Path(f))
        texts.append(t)
        headings.extend(
            [m.group(1).strip() for m in re.finditer(r"^###\s+(.+)$", t, re.M)]
        )
    combined = "\n\n".join(texts)
    seed = "\n".join(headings) if headings else combined
    return seed, headings


def _build_docs_context(
    docs_root: Optional[Path], seed_tokens: List[str], *, char_budget: int = 12000
) -> Tuple[str, List[str]]:
    if not docs_root or not docs_root.exists():
        return "", []
    ref = set(seed_tokens)
    scored: List[Tuple[int, Path]] = []
    for p in docs_root.rglob("*.rst"):
        text = _read_text_safe(p)
        if not text:
            continue
        s = _score_overlap(text, ref)
        if s:
            scored.append((s, p))
    scored.sort(key=lambda x: x[0], reverse=True)
    chosen: List[str] = []
    titles: List[str] = []
    remaining = char_budget
    for _, p in scored[:8]:
        text = _read_text_safe(p)
        title = _doc_title_from_path(p)
        snippet = text.strip()
        if len(snippet) > 1500:
            snippet = snippet[:1500]
        block = f"\n\n# {title}\n{snippet}\n"
        if remaining - len(block) < 0:
            break
        chosen.append(block)
        titles.append(title)
        remaining -= len(block)
    return "".join(chosen), titles


def _ollama_generate(
    prompt: str,
    *,
    base_url: str = None,
    model: str = None,
    timeout: int = 60,
) -> Optional[str]:
    # Use environment variables if provided, otherwise use defaults
    base_url = base_url or os.environ.get("OLLAMA_URL", "http://localhost:11434")
    model = model or os.environ.get("OLLAMA_MODEL", "llama3.2")

    url = base_url.rstrip("/") + "/api/generate"
    # Optimized payload for better performance
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 100  # Allow more tokens for complete descriptions
        },
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=data, headers={"Content-Type": "application/json"}, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            out = json.loads(resp.read().decode("utf-8"))
            response = out.get("response", "").strip() or None
            return response
    except (
        urllib.error.URLError,
        urllib.error.HTTPError,
        TimeoutError,
        json.JSONDecodeError,
    ) as e:
        return None


def _compose_prompt(
    title: str, quiz_seed: str, docs_ctx: str, *, max_chars: int, question_count: int = 0
) -> str:
    instructions = (
        "You are helping generate a concise Canvas quiz description. "
        "Write 2-3 sentences summarizing the quiz focus and its content. "
        "Mention that the quiz contains %d questions. "
        "Be specific, avoid markdown, no lists, no quotes, no headings."
    ) % question_count

    # Truncate seed and docs context to reduce prompt size
    # Use only the first 2000 chars of quiz seed
    truncated_seed = quiz_seed[:2000] if len(quiz_seed) > 2000 else quiz_seed

    # Use only the first 3000 chars of docs
    truncated_docs = docs_ctx[:3000] if len(docs_ctx) > 3000 else docs_ctx

    # Simplify the prompt structure
    return (
        f"Title: {title}\n\n"
        f"Quiz content highlights:\n{truncated_seed}\n\n"
        f"{instructions}\n\n"
        "Return only the description."
    )
def auto_generate_description(
    files: Iterable[Path],
    *,
    title: str,
    docs_root: Optional[Path] = None,
    ollama_url: str = "http://localhost:11434",
    ollama_model: str = "llama3.2",
    max_chars: int = 500,  # Increased from 240 to allow fuller descriptions
) -> str:
    """Generate a quiz description using Ollama only.

    Fails if Ollama is unavailable or returns no response.
    """
    # Count questions in files for inclusion in description
    question_count = 0
    for file in files:
        text = _read_text_safe(file)
        # Count question markers (1., 2., etc.)
        question_matches = re.findall(r'^\d+\.\s+', text, re.MULTILINE)
        question_count += len(question_matches)

    # Generate description
    seed_text, _ = _collect_quiz_seed(files)
    tokens = _tokenize(seed_text)
    docs_ctx, _ = _build_docs_context(docs_root, tokens)
    prompt = _compose_prompt(
        title,
        seed_text,
        docs_ctx,
        max_chars=max_chars,
        question_count=question_count
    )

    # Attempt to generate description
    ai = _ollama_generate(prompt, base_url=ollama_url, model=ollama_model)
    if ai:
        # Return the entire response without truncation, just clean it up
        return ai.strip().replace("\n", " ")

    # Try with a simplified prompt if the first attempt fails
    simple_prompt = f"Write a description for a quiz titled '{title}' that contains {question_count} questions."
    ai = _ollama_generate(simple_prompt, base_url=ollama_url, model=ollama_model, timeout=30)

    if ai:
        return ai.strip().replace("\n", " ")

    # If all else fails, return a simple description
    return f"Quiz on {title} containing {question_count} questions."