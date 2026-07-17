---
name: add-algorithm-problem
description: >-
  Adds a LeetCode/algorithm problem to this repo: implement the Python solution
  and incrementally update the offline handbook under catalog/. Use when the user
  asks to add a problem, 加题, 补充题目, update the catalog handbook, or register a
  new solution into catalog/index.html / problems-data.js. Do not revive meta/ or
  full-catalog regeneration.
---

# 增量加题（Algorithm 手册）

本仓库**不再**使用 `meta/` 或全量 `generate_catalog.py`。手册成品在 `catalog/`；UI 源在 `catalog_src/`。加题只做**增量修改**。

## 何时使用

- 用户要加题 / 补题解 / 把新函数登记进手册
- 需要改手册交互或样式（改 `catalog_src/` 再复制到 `catalog/`）

## 加题步骤（必须按序）

### 1. 写解法

- 放到对应模块（`patterns/`、`data_structures/`、`paradigms/`、`strings/`、`foundations/`、`common/`）
- 模块级函数优先；设计题用类（如 `LRUCache`）
- docstring 首行：`题号. 题名`（非 LC 可写中文题名）
- 带类型标注

### 2. 登记进手册

优先运行 skill 脚本（在仓库根目录）：

```bash
python .cursor/skills/add-algorithm-problem/scripts/add_to_catalog.py --file <相对路径.py> --name <函数或类名> --info <info.json>
```

`info.json` 字段见 [reference.md](reference.md)。也可用 `--info-stdin` 从 stdin 读 JSON。

脚本会：

1. 从源码抽出函数/类
2. 写入 `catalog/problems-data.js`
3. 在 `catalog/index.html` 对应分类插入卡片壳并更新计数

若脚本不便用，按 reference 手工改这两个文件（保持格式一致）。

### 3. 验收

- 打开 `catalog/index.html`，搜索题号/函数名可见
- 展开卡片有题面；再展开代码可复制
- **不要**新建 `meta/`、`generate_catalog.py`、`catalog_meta.py`
- **不要**留下临时 `info.json`（用完即删）

## 只改 UI

编辑 `catalog_src/static/catalog.css` 或 `catalog.js`，或 `catalog_src/templates/index.html`，然后复制到 `catalog/`：

```bash
copy catalog_src\static\catalog.css catalog\catalog.css
copy catalog_src\static\catalog.js catalog\catalog.js
```

（模板变更若需重建整页骨架，与用户确认；小规模加题通常只动 data + 插卡片。）

## 分类映射（插卡用）

| 路径前缀 | section id |
|----------|------------|
| common/ | common |
| foundations/ | foundations |
| patterns/two_pointers/ | two-pointers |
| patterns/sliding_window/ | sliding-window |
| patterns/prefix_sum/ | prefix-sum |
| patterns/graph/ | graph |
| patterns/binary_search/ | binary-search |
| patterns/（其余） | patterns |
| data_structures/array/ | array |
| data_structures/matrix/ | matrix |
| data_structures/linked_list/ | linked-list |
| data_structures/tree/ | tree |
| data_structures/stack_queue/ | stack-queue |
| data_structures/hash_map/ | hash-map |
| data_structures/trie/ | trie |
| paradigms/backtracking/ | backtracking |
| paradigms/greedy/ | greedy |
| paradigms/dynamic_programming/ | dp |
| strings/ | strings |

详情与 JSON 示例见 [reference.md](reference.md)。
