# 手册增量格式

## problems-data.js

文件形态：

```js
window.__PROBLEMS__ = { ... };
```

每条 key = 卡片 `id`，value：

```json
{
  "statement": "题面（可用 \\n\\n 分段）",
  "examples": ["示例 1：…", "示例 2：…"],
  "steps": ["步骤1", "步骤2"],
  "codeNotes": ["代码说明1", "代码说明2"],
  "complexity": "时间 O(n)，空间 O(1)。",
  "codeHtml": "<div class=\"code-scroll\">…预高亮 HTML…</div>",
  "codeText": "原始 Python 源码"
}
```

`codeHtml` / `codeText` 由脚本从源码生成；手写时至少保证 `codeText` 正确，`codeHtml` 可用简单 `<pre>` 包裹（观感较差）。

## 卡片壳（index.html）

插在对应 `<section class="section" id="…">` 的 `<div class="cards">` 内：

```html
<details class="card" id="lc-1-two-sum" data-id="lc-1-two-sum"
  data-title="leetcode 1 · 两数之和" data-lc="1" data-fn="two_sum"
  data-difficulty="Easy">
  <summary class="card-header">
    <div class="title-row">
      <h3>LeetCode 1 · 两数之和</h3>
      <span class="tag">哈希表</span>
      <span class="tag tag-diff tag-easy">Easy</span>
    </div>
    <div class="meta">
      <code class="fn-name">two_sum()</code>
      <span class="file-path">data_structures/hash_map/hash_map.py</span>
      <a class="lc-link" href="https://leetcode.cn/problems/two-sum/" target="_blank" rel="noopener">LeetCode</a>
      <span class="expand-hint">展开</span>
    </div>
  </summary>
  <div class="card-body"><p class="muted">加载中…</p></div>
</details>
```

规则：

- `id`：有题号 `lc-{no}-{name}`，否则 `fn-{name}`；全小写，非 `[a-z0-9]` 变 `-`
- 设计题：`name` 为类名，代码为整类
- 变体：加 `<span class="tag tag-variant">变体 · KMP</span>`
- 非 LC：不要 LeetCode 链接；标题不加 `LeetCode {no} ·`
- `data-difficulty`：`Easy` | `Medium` | `Hard` | `unset`
- 插入后更新该 section 的 `section-count`、侧栏对应 `nav-link span`、顶部「共 N 题」

## info.json（给脚本）

```json
{
  "no": "1",
  "title": "两数之和",
  "statement": "给定…",
  "examples": ["示例 1：…"],
  "steps": ["用哈希表…"],
  "code_notes": ["seen[x] = i"],
  "complexity": "时间 O(n)，空间 O(n)。",
  "pattern": "哈希表",
  "difficulty": "Easy",
  "slug": "two-sum",
  "variant": "",
  "non_lc": false
}
```

可省略空字段。`slug` 用于 `https://leetcode.cn/problems/{slug}/`。
