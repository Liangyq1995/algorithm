"""Generate algorithm/catalog.html with problem descriptions and solutions."""

from __future__ import annotations

import ast
import html
import re
from datetime import datetime
from pathlib import Path

from catalog_meta import get_problem_info

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "catalog.html"

SKIP_FILES = {"__init__.py", "generate_catalog.py", "catalog_meta.py"}
SKIP_PREFIX = "_"
DESIGN_CLASSES = {"MonotonicQueue", "QueueUsingStack", "StackUsingQueue", "MinStack", "LRUCache", "Trie", "MedianFinder", "Codec"}
SKIP_CLASSES = {"ListNode", "TreeNode", "GraphNode", "RandomListNode", "ConnectNode"}
PLAIN_METHOD_CLASSES = {"BackTracking"}

PY_KEYWORDS = {
    "and", "as", "assert", "async", "await", "break", "class", "continue", "def",
    "del", "elif", "else", "except", "False", "finally", "for", "from", "global",
    "if", "import", "in", "is", "lambda", "None", "nonlocal", "not", "or", "pass",
    "raise", "return", "True", "try", "while", "with", "yield",
}

CATEGORY_MAP = {
    "common": "公共工具",
    "foundations": "基础算法",
    "patterns/two_pointers": "双指针",
    "patterns/sliding_window": "滑动窗口",
    "patterns/prefix_sum": "前缀和",
    "patterns/graph": "图论",
    "patterns/binary_search": "二分查找",
    "patterns": "解题模式",
    "data_structures/array": "数组",
    "data_structures/matrix": "矩阵",
    "data_structures/linked_list": "链表",
    "data_structures/tree": "二叉树",
    "data_structures/stack_queue": "栈与队列",
    "data_structures/hash_map": "哈希表",
    "data_structures/trie": "字典树",
    "data_structures": "数据结构",
    "paradigms/backtracking": "回溯",
    "paradigms/greedy": "贪心",
    "paradigms/dynamic_programming": "动态规划",
    "paradigms": "算法范式",
    "strings": "字符串",
}


def category_for(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    parts = rel.split("/")
    if len(parts) >= 2:
        key = "/".join(parts[:-1])
        if key in CATEGORY_MAP:
            return CATEGORY_MAP[key]
    if parts[0] in CATEGORY_MAP:
        return CATEGORY_MAP[parts[0]]
    return parts[0]


def get_source(lines: list[str], node: ast.AST) -> str:
    if not hasattr(node, "lineno"):
        return ""
    start = node.lineno - 1
    end = getattr(node, "end_lineno", node.lineno)
    return "".join(lines[start:end]).strip()


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
        if text.startswith("#"):
            wrapped = f'<span data-h="com">{text}</span>'
        else:
            wrapped = f'<span data-h="str">{text}</span>'
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


def render_statement(statement: str) -> str:
    if not statement:
        return '<p class="muted">（暂无详细描述）</p>'
    paras = [p.strip() for p in statement.split("\n\n") if p.strip()]
    if len(paras) > 1:
        return "".join(f"<p>{html.escape(p)}</p>" for p in paras)
    return f"<p>{html.escape(statement)}</p>"


def extract_items(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    tree = ast.parse(text)
    rel = path.relative_to(ROOT).as_posix()
    category = category_for(path)
    items: list[dict] = []

    def add_item(node: ast.AST, name: str) -> None:
        if name.startswith(SKIP_PREFIX):
            return
        doc = ast.get_docstring(node) or ""
        meta = get_problem_info(rel, name, doc)
        lc_no = meta.get("no", "")
        title = meta.get("title", name)
        display_title = f"LeetCode {lc_no} · {title}" if lc_no else title
        items.append(
            {
                "category": category,
                "file": rel,
                "name": name,
                "lc_no": lc_no,
                "title": display_title,
                "statement": meta.get("statement", ""),
                "examples": meta.get("examples", []),
                "steps": meta.get("steps", []),
                "code_notes": meta.get("code_notes", []),
                "complexity": meta.get("complexity", ""),
                "pattern": meta.get("pattern", category),
                "code": get_source(lines, node),
            }
        )

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            add_item(node, node.name)
        elif isinstance(node, ast.ClassDef):
            if node.name in SKIP_CLASSES:
                continue
            for child in node.body:
                if isinstance(child, ast.FunctionDef) and not child.name.startswith(SKIP_PREFIX):
                    if node.name in PLAIN_METHOD_CLASSES:
                        add_item(child, child.name)
                    elif node.name in DESIGN_CLASSES:
                        add_item(child, f"{node.name}.{child.name}")

    return items


def render_card(item: dict, cat_id: str) -> str:
    anchor = html.escape(f"{cat_id}-{item['name']}")
    pattern_html = ""
    if item.get("pattern"):
        pattern_html = f'<span class="tag">{html.escape(item["pattern"])}</span>'

    examples_html = ""
    if item["examples"]:
        lis = "".join(f"<li>{html.escape(ex)}</li>" for ex in item["examples"])
        examples_html = f"""
          <div class="panel panel-examples">
            <div class="panel-head"><span class="panel-icon">📋</span><h4>示例</h4></div>
            <div class="panel-body"><ul class="example-list">{lis}</ul></div>
          </div>"""

    approach_html = ""
    if item["steps"]:
        lis = "".join(f"<li>{html.escape(step)}</li>" for step in item["steps"])
        approach_html = f"""
          <div class="panel panel-approach">
            <div class="panel-head"><span class="panel-icon">💡</span><h4>解题思路</h4></div>
            <div class="panel-body"><ol class="step-list">{lis}</ol></div>
          </div>"""

    code_notes_html = ""
    if item.get("code_notes"):
        notes = "".join(
            f'<li><span class="note-idx">{i}</span>{html.escape(note)}</li>'
            for i, note in enumerate(item["code_notes"], 1)
        )
        code_notes_html = f"""
            <div class="code-notes">
              <div class="code-notes-head">代码说明</div>
              <ol class="note-list">{notes}</ol>
            </div>"""

    complexity_html = ""
    if item.get("complexity"):
        complexity_html = f'<div class="complexity">复杂度：{html.escape(item["complexity"])}</div>'

    return f"""
        <article class="card" id="{anchor}" data-title="{html.escape(item['title'].lower())}" data-lc="{html.escape(item['lc_no'])}">
          <header class="card-header">
            <div class="title-row">
              <h3>{html.escape(item['title'])}</h3>
              {pattern_html}
            </div>
            <div class="meta">
              <code class="fn-name">{html.escape(item['name'])}()</code>
              <span class="file-path">{html.escape(item['file'])}</span>
            </div>
          </header>
          <div class="panel panel-problem">
            <div class="panel-head"><span class="panel-icon">📖</span><h4>题目描述</h4></div>
            <div class="panel-body problem-body">{render_statement(item['statement'])}</div>
          </div>
          {examples_html}
          {approach_html}
          <div class="panel panel-code">
            <div class="panel-head"><span class="panel-icon">🐍</span><h4>Python 实现</h4></div>
            <div class="panel-body">
              {render_code_block(item['code'])}
              {code_notes_html}
              {complexity_html}
            </div>
          </div>
        </article>"""


def build_html(all_items: list[dict]) -> str:
    grouped: dict[str, list[dict]] = {}
    for item in all_items:
        grouped.setdefault(item["category"], []).append(item)

    category_order = [
        "公共工具", "基础算法", "双指针", "滑动窗口", "前缀和", "图论", "二分查找", "解题模式",
        "数组", "矩阵", "链表", "二叉树", "栈与队列", "哈希表", "字典树",
        "回溯", "贪心", "动态规划", "字符串",
    ]
    ordered = [c for c in category_order if c in grouped] + sorted(set(grouped) - set(category_order))

    nav_parts = ['<input type="search" id="search" placeholder="搜索题号、标题、函数名…" autocomplete="off" />']
    body_parts = []
    total = len(all_items)

    for cat in ordered:
        items = sorted(
            grouped[cat],
            key=lambda x: (not x["lc_no"], int(x["lc_no"]) if x["lc_no"].isdigit() else 9999, x["title"]),
        )
        cat_id = html.escape(cat.replace(" ", "-"))
        nav_parts.append(f'<a class="nav-link" href="#{cat_id}">{html.escape(cat)}<span>{len(items)}</span></a>')
        cards = "".join(render_card(item, cat_id) for item in items)
        body_parts.append(
            f"""
      <section class="section" id="{cat_id}">
        <div class="section-head">
          <h2>{html.escape(cat)}</h2>
          <span class="section-count">{len(items)} 题</span>
        </div>
        <div class="cards">{cards}</div>
      </section>"""
        )

    generated = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Algorithm 题目手册</title>
  <style>
    :root {{
      --bg: #0b0f14;
      --bg2: #111820;
      --panel: #151c26;
      --panel2: #1a2330;
      --border: #2a3544;
      --border-light: #364556;
      --text: #e8eef5;
      --muted: #8fa3b8;
      --accent: #6cb6ff;
      --accent-dim: rgba(108,182,255,.12);
      --green: #56d364;
      --green-dim: rgba(86,211,100,.1);
      --amber: #e3b341;
      --amber-dim: rgba(227,179,65,.1);
      --purple: #bc8cff;
      --purple-dim: rgba(188,140,255,.1);
      --code-bg: #0d1117;
      --radius: 12px;
      --shadow: 0 4px 24px rgba(0,0,0,.35);
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      font-family: "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.7;
      font-size: 15px;
    }}
    .layout {{
      display: grid;
      grid-template-columns: 260px minmax(0, 1fr);
      min-height: 100vh;
    }}
    nav {{
      position: sticky;
      top: 0;
      height: 100vh;
      overflow-y: auto;
      padding: 1.5rem 1rem;
      background: var(--bg2);
      border-right: 1px solid var(--border);
    }}
    nav h1 {{
      font-size: 1.1rem;
      font-weight: 700;
      margin: 0 0 .25rem;
      background: linear-gradient(135deg, var(--accent), var(--purple));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }}
    nav .sub {{ color: var(--muted); font-size: .8rem; margin-bottom: 1rem; }}
    #search {{
      width: 100%;
      padding: .55rem .75rem;
      margin-bottom: .85rem;
      border: 1px solid var(--border);
      border-radius: 8px;
      background: var(--panel);
      color: var(--text);
      font-size: .88rem;
      outline: none;
      transition: border-color .2s;
    }}
    #search:focus {{ border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-dim); }}
    .nav-link {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: var(--muted);
      text-decoration: none;
      padding: .4rem .55rem;
      border-radius: 8px;
      font-size: .86rem;
      margin-bottom: 2px;
      transition: background .15s, color .15s;
    }}
    .nav-link:hover {{ background: var(--panel); color: var(--text); }}
    .nav-link span {{
      font-size: .75rem;
      color: var(--accent);
      background: var(--accent-dim);
      padding: .1rem .45rem;
      border-radius: 999px;
      min-width: 1.6rem;
      text-align: center;
    }}
    main {{
      padding: 2rem 2.5rem 4rem;
      max-width: 920px;
    }}
    .hero {{
      margin-bottom: 2.5rem;
      padding: 1.5rem 1.75rem;
      background: linear-gradient(135deg, var(--panel) 0%, var(--panel2) 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
    }}
    .hero h2 {{ margin: 0 0 .5rem; font-size: 1.5rem; font-weight: 700; }}
    .hero p {{ color: var(--muted); margin: 0; font-size: .92rem; }}
    .hero strong {{ color: var(--accent); font-weight: 600; }}
    .section {{ margin-bottom: 3rem; scroll-margin-top: 1rem; }}
    .section-head {{
      display: flex;
      align-items: baseline;
      gap: .75rem;
      margin-bottom: 1.25rem;
      padding-bottom: .65rem;
      border-bottom: 1px solid var(--border);
    }}
    .section-head h2 {{
      margin: 0;
      font-size: 1.35rem;
      font-weight: 700;
    }}
    .section-count {{ color: var(--muted); font-size: .85rem; }}
    .cards {{ display: flex; flex-direction: column; gap: 1.5rem; }}
    .card {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      overflow: hidden;
      box-shadow: var(--shadow);
      transition: border-color .2s;
    }}
    .card:hover {{ border-color: var(--border-light); }}
    .card.hidden {{ display: none; }}
    .card-header {{
      padding: 1.15rem 1.4rem .85rem;
      border-bottom: 1px solid var(--border);
      background: var(--panel2);
    }}
    .title-row {{
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: .55rem;
      margin-bottom: .4rem;
    }}
    .card h3 {{
      margin: 0;
      font-size: 1.08rem;
      font-weight: 650;
      color: var(--green);
    }}
    .tag {{
      font-size: .72rem;
      font-weight: 600;
      background: var(--accent-dim);
      color: var(--accent);
      padding: .15rem .55rem;
      border-radius: 999px;
      border: 1px solid rgba(108,182,255,.25);
    }}
    .meta {{
      font-size: .82rem;
      color: var(--muted);
      display: flex;
      gap: .85rem;
      flex-wrap: wrap;
      align-items: center;
    }}
    .fn-name {{
      background: var(--amber-dim);
      color: var(--amber);
      padding: .12rem .5rem;
      border-radius: 6px;
      font-size: .8rem;
      border: 1px solid rgba(227,179,65,.2);
    }}
    .file-path {{ opacity: .85; }}
    .panel {{ border-bottom: 1px solid var(--border); }}
    .panel:last-child {{ border-bottom: none; }}
    .panel-head {{
      display: flex;
      align-items: center;
      gap: .45rem;
      padding: .65rem 1.4rem;
      font-size: .78rem;
      font-weight: 700;
      letter-spacing: .06em;
      text-transform: uppercase;
    }}
    .panel-icon {{ font-size: .95rem; line-height: 1; }}
    .panel-head h4 {{ margin: 0; font-size: inherit; font-weight: inherit; }}
    .panel-body {{ padding: 0 1.4rem 1.15rem; }}
    .panel-problem .panel-head {{ background: var(--accent-dim); color: var(--accent); }}
    .panel-examples .panel-head {{ background: var(--amber-dim); color: var(--amber); }}
    .panel-approach .panel-head {{ background: var(--green-dim); color: var(--green); }}
    .panel-code .panel-head {{ background: var(--purple-dim); color: var(--purple); }}
    .problem-body p {{ margin: 0 0 .65rem; color: var(--text); }}
    .problem-body p:last-child {{ margin-bottom: 0; }}
    .example-list {{
      margin: 0;
      padding: 0;
      list-style: none;
    }}
    .example-list li {{
      padding: .55rem .75rem;
      margin-bottom: .4rem;
      background: var(--bg2);
      border-radius: 8px;
      border-left: 3px solid var(--amber);
      font-size: .9rem;
      color: #d4dde8;
    }}
    .example-list li:last-child {{ margin-bottom: 0; }}
    .step-list {{
      margin: 0;
      padding: 0;
      list-style: none;
      counter-reset: step;
    }}
    .step-list li {{
      position: relative;
      padding: .6rem .75rem .6rem 2.6rem;
      margin-bottom: .45rem;
      background: var(--bg2);
      border-radius: 8px;
      font-size: .92rem;
      color: #c8d8ea;
      line-height: 1.65;
    }}
    .step-list li:last-child {{ margin-bottom: 0; }}
    .step-list li::before {{
      counter-increment: step;
      content: counter(step);
      position: absolute;
      left: .65rem;
      top: .55rem;
      width: 1.35rem;
      height: 1.35rem;
      display: flex;
      align-items: center;
      justify-content: center;
      background: var(--green-dim);
      color: var(--green);
      border-radius: 50%;
      font-size: .72rem;
      font-weight: 700;
    }}
    .code-scroll {{
      border-radius: 8px;
      overflow: auto;
      border: 1px solid var(--border);
      background: var(--code-bg);
    }}
    .code-table {{
      width: 100%;
      border-collapse: collapse;
      font-family: "Cascadia Code", "Fira Code", "JetBrains Mono", Consolas, monospace;
      font-size: .82rem;
      line-height: 1.55;
    }}
    .code-table .ln {{
      width: 2.8rem;
      padding: 0 .65rem 0 .5rem;
      text-align: right;
      color: #484f58;
      user-select: none;
      vertical-align: top;
      border-right: 1px solid var(--border);
      background: rgba(255,255,255,.02);
    }}
    .code-table .lc {{
      padding: 0 .85rem;
      white-space: pre;
      color: #c9d1d9;
    }}
    .code-table tr:hover .lc {{ background: rgba(108,182,255,.04); }}
    .tok-kw, [data-h="kw"] {{ color: #ff7b72; }}
    .tok-str, [data-h="str"] {{ color: #a5d6ff; }}
    .tok-com, [data-h="com"] {{ color: #8b949e; font-style: italic; }}
    .tok-num, [data-h="num"] {{ color: #79c0ff; }}
    .code-notes {{
      margin-top: 1rem;
      padding: .85rem 1rem;
      background: var(--purple-dim);
      border: 1px solid rgba(188,140,255,.2);
      border-radius: 8px;
    }}
    .code-notes-head {{
      font-size: .78rem;
      font-weight: 700;
      letter-spacing: .05em;
      text-transform: uppercase;
      color: var(--purple);
      margin-bottom: .55rem;
    }}
    .note-list {{
      margin: 0;
      padding: 0;
      list-style: none;
    }}
    .note-list li {{
      display: flex;
      gap: .55rem;
      padding: .35rem 0;
      font-size: .88rem;
      color: #c4b5fd;
      line-height: 1.6;
      border-bottom: 1px solid rgba(188,140,255,.1);
    }}
    .note-list li:last-child {{ border-bottom: none; }}
    .note-idx {{
      flex-shrink: 0;
      width: 1.2rem;
      height: 1.2rem;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(188,140,255,.2);
      color: var(--purple);
      border-radius: 4px;
      font-size: .7rem;
      font-weight: 700;
      margin-top: .15rem;
    }}
    .complexity {{
      margin-top: .75rem;
      font-size: .82rem;
      color: var(--muted);
      padding: .45rem .65rem;
      background: var(--bg2);
      border-radius: 6px;
      border-left: 3px solid var(--accent);
    }}
    .muted {{ color: var(--muted); font-size: .9rem; }}
    .no-result {{
      display: none;
      text-align: center;
      padding: 3rem;
      color: var(--muted);
    }}
    @media (max-width: 900px) {{
      .layout {{ grid-template-columns: 1fr; }}
      nav {{ position: static; height: auto; border-right: none; border-bottom: 1px solid var(--border); }}
      main {{ padding: 1.25rem; }}
    }}
  </style>
</head>
<body>
  <div class="layout">
    <nav>
      <h1>Algorithm 手册</h1>
      <div class="sub">共 {total} 题 · 更新于 {generated}</div>
      {''.join(nav_parts)}
    </nav>
    <main>
      <div class="hero">
        <h2>算法题目与解法</h2>
        <p>每题包含完整<strong>题目描述</strong>、示例、分步<strong>解题思路</strong>，以及带<strong>代码说明</strong>的 Python 实现。</p>
      </div>
      <div id="no-result" class="no-result">未找到匹配题目，请换个关键词试试。</div>
      {''.join(body_parts)}
    </main>
  </div>
  <script>
    const search = document.getElementById('search');
    const cards = document.querySelectorAll('.card');
    const noResult = document.getElementById('no-result');
    search.addEventListener('input', () => {{
      const q = search.value.trim().toLowerCase();
      let visible = 0;
      cards.forEach(card => {{
        const match = !q || card.innerText.toLowerCase().includes(q);
        card.classList.toggle('hidden', !match);
        if (match) visible++;
      }});
      noResult.style.display = q && visible === 0 ? 'block' : 'none';
    }});
  </script>
</body>
</html>
"""


def main() -> None:
    all_items: list[dict] = []
    for path in sorted(ROOT.rglob("*.py")):
        if path.name in SKIP_FILES or "__pycache__" in path.parts or "meta" in path.parts:
            continue
        all_items.extend(extract_items(path))

    OUTPUT.write_text(build_html(all_items), encoding="utf-8")
    print(f"Generated {OUTPUT} with {len(all_items)} entries")


if __name__ == "__main__":
    main()
