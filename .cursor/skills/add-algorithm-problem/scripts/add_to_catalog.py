#!/usr/bin/env python3
"""Incrementally register one function/class into catalog/ handbook."""

from __future__ import annotations

import argparse
import ast
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT_DIR = ROOT / "catalog"
DATA_JS = OUT_DIR / "problems-data.js"
INDEX_HTML = OUT_DIR / "index.html"

PY_KEYWORDS = {
    "and", "as", "assert", "async", "await", "break", "class", "continue", "def",
    "del", "elif", "else", "except", "False", "finally", "for", "from", "global",
    "if", "import", "in", "is", "lambda", "None", "nonlocal", "not", "or", "pass",
    "raise", "return", "True", "try", "while", "with", "yield",
}

CATEGORY_RULES = [
    ("patterns/two_pointers", "two-pointers", "双指针"),
    ("patterns/sliding_window", "sliding-window", "滑动窗口"),
    ("patterns/prefix_sum", "prefix-sum", "前缀和"),
    ("patterns/graph", "graph", "图论"),
    ("patterns/binary_search", "binary-search", "二分查找"),
    ("patterns", "patterns", "解题模式"),
    ("data_structures/array", "array", "数组"),
    ("data_structures/matrix", "matrix", "矩阵"),
    ("data_structures/linked_list", "linked-list", "链表"),
    ("data_structures/tree", "tree", "二叉树"),
    ("data_structures/stack_queue", "stack-queue", "栈与队列"),
    ("data_structures/hash_map", "hash-map", "哈希表"),
    ("data_structures/trie", "trie", "字典树"),
    ("paradigms/backtracking", "backtracking", "回溯"),
    ("paradigms/greedy", "greedy", "贪心"),
    ("paradigms/dynamic_programming", "dp", "动态规划"),
    ("foundations", "foundations", "基础算法"),
    ("strings", "strings", "字符串"),
    ("common", "common", "公共工具"),
]


def category_for(rel: str) -> tuple[str, str]:
    posix = rel.replace("\\", "/")
    folder = str(Path(posix).parent).replace("\\", "/")
    for prefix, slug, label in CATEGORY_RULES:
        if folder == prefix or folder.startswith(prefix + "/"):
            return slug, label
    return "patterns", "解题模式"


def make_id(lc_no: str, name: str) -> str:
    raw = f"lc-{lc_no}-{name}" if lc_no else f"fn-{name}"
    return re.sub(r"[^a-z0-9]+", "-", raw.lower()).strip("-") or "item"


def highlight_python_line(line: str) -> str:
    escaped = html.escape(line)
    placeholders: list[str] = []

    def stash(match: re.Match[str]) -> str:
        placeholders.append(match.group(0))
        return f"\x00{len(placeholders) - 1}\x00"

    escaped = re.sub(r'("(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\')', stash, escaped)
    escaped = re.sub(r"(#.*)$", stash, escaped)
    for kw in sorted(PY_KEYWORDS, key=len, reverse=True):
        escaped = re.sub(
            rf"(?<![A-Za-z0-9_])({re.escape(kw)})(?![A-Za-z0-9_])",
            r'<span data-h="kw">\1</span>',
            escaped,
        )
    escaped = re.sub(
        r"(?<![A-Za-z0-9.])(\d+)(?![A-Za-z0-9_])",
        r'<span data-h="num">\1</span>',
        escaped,
    )
    for i, text in enumerate(placeholders):
        wrapped = (
            f'<span data-h="com">{text}</span>'
            if text.startswith("#")
            else f'<span data-h="str">{text}</span>'
        )
        escaped = escaped.replace(f"\x00{i}\x00", wrapped)
    return escaped


def render_code_block(code: str) -> str:
    if not code.strip():
        return '<p class="muted">（暂无代码）</p>'
    rows = []
    for i, line in enumerate(code.split("\n"), 1):
        body = highlight_python_line(line) if line else "&nbsp;"
        rows.append(f'<tr><td class="ln">{i}</td><td class="lc">{body}</td></tr>')
    return f'<div class="code-scroll"><table class="code-table"><tbody>{"".join(rows)}</tbody></table></div>'


def extract_source(path: Path, name: str) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    tree = ast.parse(text)
    lines = text.splitlines(keepends=True)
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name == name:
            src = "".join(lines[node.lineno - 1 : node.end_lineno]).strip()
            doc = ast.get_docstring(node) or ""
            return src, doc
    raise SystemExit(f"cannot find {name!r} in {path}")


def load_problems() -> dict:
    raw = DATA_JS.read_text(encoding="utf-8")
    match = re.search(r"window\.__PROBLEMS__\s*=\s*(\{.*\})\s*;\s*$", raw, re.S)
    if not match:
        raise SystemExit("cannot parse problems-data.js")
    return json.loads(match.group(1))


def save_problems(data: dict) -> None:
    DATA_JS.write_text(
        "window.__PROBLEMS__ = " + json.dumps(data, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )


def parse_doc_title(doc: str) -> tuple[str, str]:
    if not doc:
        return "", ""
    first = doc.strip().split("\n")[0]
    m = re.match(r"(\d+)\.\s*(.+)", first)
    if m:
        return m.group(1), m.group(2).strip()
    return "", first.strip()


def render_card(item: dict) -> str:
    item_id = html.escape(item["id"])
    tags = []
    if item.get("pattern"):
        tags.append(f'<span class="tag">{html.escape(item["pattern"])}</span>')
    if item.get("difficulty"):
        diff = html.escape(item["difficulty"])
        tags.append(f'<span class="tag tag-diff tag-{diff.lower()}">{diff}</span>')
    if item.get("variant"):
        tags.append(f'<span class="tag tag-variant">变体 · {html.escape(item["variant"])}</span>')

    link_html = ""
    if not item.get("non_lc"):
        if item.get("slug"):
            url = f"https://leetcode.cn/problems/{item['slug']}/"
            link_html = (
                f'<a class="lc-link" href="{html.escape(url)}" target="_blank" rel="noopener">LeetCode</a>'
            )
        elif item.get("lc_no"):
            url = f"https://leetcode.cn/problemset/?search={item['lc_no']}"
            link_html = (
                f'<a class="lc-link" href="{html.escape(url)}" target="_blank" rel="noopener">LeetCode</a>'
            )

    diff_attr = html.escape(item.get("difficulty") or "unset")
    return f"""
        <details class="card" id="{item_id}" data-id="{item_id}" data-title="{html.escape(item['title'].lower())}" data-lc="{html.escape(item['lc_no'])}" data-fn="{html.escape(item['name'].lower())}" data-difficulty="{diff_attr}">
          <summary class="card-header">
            <div class="title-row">
              <h3>{html.escape(item['display_title'])}</h3>
              {''.join(tags)}
            </div>
            <div class="meta">
              <code class="fn-name">{html.escape(item['name'])}()</code>
              <span class="file-path">{html.escape(item['file'])}</span>
              {link_html}
              <span class="expand-hint">展开</span>
            </div>
          </summary>
          <div class="card-body"><p class="muted">加载中…</p></div>
        </details>"""


def upsert_card(html_text: str, section_id: str, card_html: str, item_id: str) -> str:
    # remove existing card with same id
    html_text = re.sub(
        rf'\s*<details class="card" id="{re.escape(item_id)}"[\s\S]*?</details>',
        "",
        html_text,
        count=1,
    )
    pattern = rf'(<section class="section" id="{re.escape(section_id)}"[\s\S]*?<div class="cards">)'
    match = re.search(pattern, html_text)
    if not match:
        raise SystemExit(f"section id={section_id!r} not found in index.html")
    insert_at = match.end()
    return html_text[:insert_at] + card_html + html_text[insert_at:]


def refresh_counts(html_text: str) -> str:
    def section_count(section_html: str) -> int:
        return len(re.findall(r'<details class="card"', section_html))

    def repl_section(m: re.Match[str]) -> str:
        block = m.group(0)
        n = section_count(block)
        block = re.sub(
            r'(<span class="section-count">)\d+ 题(</span>)',
            rf"\g<1>{n} 题\2",
            block,
            count=1,
        )
        return block

    html_text = re.sub(
        r'<section class="section" id="[^"]+"[\s\S]*?</section>',
        repl_section,
        html_text,
    )

    # nav badges
    for m in re.finditer(r'<section class="section" id="([^"]+)"[\s\S]*?</section>', html_text):
        sid, block = m.group(1), m.group(0)
        n = section_count(block)
        html_text = re.sub(
            rf'(<a class="nav-link" href="#{re.escape(sid)}">[^<]*)<span>\d+</span>',
            rf"\1<span>{n}</span>",
            html_text,
            count=1,
        )

    total = len(re.findall(r'<details class="card"', html_text))
    html_text = re.sub(
        r"(共 )\d+( 题 · 更新于 )",
        rf"\g<1>{total}\2",
        html_text,
        count=1,
    )
    return html_text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", required=True, help="solution file relative to repo root")
    parser.add_argument("--name", required=True, help="function or class name")
    parser.add_argument("--info", help="path to info JSON")
    parser.add_argument("--info-stdin", action="store_true", help="read info JSON from stdin")
    args = parser.parse_args()

    if args.info_stdin:
        info = json.load(sys.stdin)
    elif args.info:
        info = json.loads(Path(args.info).read_text(encoding="utf-8-sig"))
    else:
        info = {}

    rel = Path(args.file).as_posix()
    path = ROOT / rel
    if not path.exists():
        raise SystemExit(f"file not found: {rel}")

    code, doc = extract_source(path, args.name)
    doc_no, doc_title = parse_doc_title(doc)

    lc_no = str(info.get("no") or doc_no or "")
    title = str(info.get("title") or doc_title or args.name)
    non_lc = bool(info.get("non_lc"))
    if non_lc or not lc_no:
        display_title = title
    else:
        display_title = f"LeetCode {lc_no} · {title}"

    item_id = make_id(lc_no, args.name)
    section_id, default_pattern = category_for(rel)
    pattern = info.get("pattern") or default_pattern
    difficulty = info.get("difficulty") or ""

    statement = info.get("statement") or doc.strip() or title
    examples = info.get("examples") or []
    steps = info.get("steps") or []
    code_notes = info.get("code_notes") or info.get("codeNotes") or []
    complexity = info.get("complexity") or ""

    problems = load_problems()
    problems[item_id] = {
        "statement": statement,
        "examples": examples,
        "steps": steps,
        "codeNotes": code_notes,
        "complexity": complexity,
        "codeHtml": render_code_block(code),
        "codeText": code,
    }
    save_problems(problems)

    card = render_card(
        {
            "id": item_id,
            "name": args.name,
            "file": rel,
            "lc_no": lc_no,
            "title": display_title,
            "display_title": display_title,
            "pattern": pattern,
            "difficulty": difficulty,
            "variant": info.get("variant") or "",
            "slug": info.get("slug") or "",
            "non_lc": non_lc or not lc_no,
        }
    )
    html_text = INDEX_HTML.read_text(encoding="utf-8")
    html_text = upsert_card(html_text, section_id, card, item_id)
    html_text = refresh_counts(html_text)
    INDEX_HTML.write_text(html_text, encoding="utf-8")

    print(f"upserted {item_id} -> section #{section_id} ({rel}::{args.name})")
    print(f"catalog now has {len(problems)} data entries")


if __name__ == "__main__":
    main()
