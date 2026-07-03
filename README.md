# Algorithm 代码库

LeetCode 刷题实现，按 **解题模式 + 数据结构 + 算法范式** 组织，全部为**纯函数/独立类**，无无效的 `@abstractmethod` 包装。

## 目录结构

```
algorithm/
├── common/                 # 公共定义（ListNode、TreeNode、KMP）
├── foundations/            # 基础（排序、位运算）
├── patterns/               # 通用技巧（双指针、滑动窗口、前缀和、图论、二分、单调栈）
├── data_structures/        # 数据结构专题（数组、矩阵、链表、树、栈队列、哈希、字典树）
├── paradigms/              # 算法范式（回溯、贪心、动态规划）
├── strings/                # 字符串
└── README.md
```

## 代码规范（本次重构）

| 改进项 | 说明 |
|--------|------|
| 去掉伪抽象类 | 原 `ArrayCode`、`LinkLeetCode` 等从未被继承，已全部改为模块级函数 |
| 拆分大文件 | 原 800+ 行 `array.py`、`1000+` 行 `core.py` 按职责拆分 |
| 消除重复 | KMP `build_next` 统一到 `common/kmp.py`；`merge_intervals` 只保留在 `greedy.py` |
| 修复 bug | 单调栈 `daily_temperatures` 补全 return；树 `count_nodes` 递归名修正；去掉调试 `print` |
| 优化实现 | 打家劫舍/最大子数组用滚动变量；`QueueUsingStack` 改为双栈均摊 O(1) |

## 模块索引

### common/
- `nodes.py` — `ListNode`, `TreeNode`
- `kmp.py` — `build_next`, `kmp_search`, `str_str`

### foundations/
- `sorting.py` — 快速排序
- `bit_manipulation.py` — 位运算题目

### patterns/
- `two_pointers/array.py` — 双指针（三数之和、盛水、去重等）
- `sliding_window/window.py` — 滑动窗口
- `prefix_sum/prefix.py` — 前缀和 + 哈希
- `prefix_sum/min_subarray_divisible_by_p.py` — 整除子数组
- `graph/graph.py` — 岛屿、克隆图、课程表
- `binary_search/basic.py` — 二分查找
- `binary_search/median_of_two_sorted_arrays.py` — 两数组中位数
- `monotonic_stack.py` — 单调栈

### data_structures/
- `array/basic.py` — 数组基础操作
- `matrix/matrix.py` — 矩阵搜索/置零
- `linked_list/linked_list.py` — 链表全套
- `tree/tree.py` — 二叉树/BST 全套
- `stack_queue/stack_queue.py` — 栈、队列、堆、设计题
- `hash_map/hash_map.py` — 哈希表
- `trie/trie.py` — 字典树（Trie）

### paradigms/
- `backtracking/backtracking.py` — 回溯
- `greedy/greedy.py` — 贪心（含区间合并）
- `dynamic_programming/linear_dp.py` — 线性 DP（最大子数组、爬楼梯、打家劫舍）
- `dynamic_programming/linear_dp.py` — 线性 DP
- `dynamic_programming/knapsack.py` — 背包系列
- `dynamic_programming/stock.py` — 股票系列
- `dynamic_programming/sequence_dp.py` — 子序列/编辑距离/回文
- `dynamic_programming/grid_dp.py` — 网格/三角形/博弈

### strings/
- `operations.py` — 字符串操作（含 Z 字形变换、整数反转）
- `pattern_matching.py` — 重复子串、KMP 应用

## 使用示例

```python
from algorithm.patterns.two_pointers.array import three_sum
from algorithm.paradigms.dynamic_programming.knapsack import coin_change_min
from algorithm.data_structures.tree.tree import level_order

print(three_sum([-1, 0, 1, 2, -1, -4]))
print(coin_change_min(11, [1, 2, 5]))
```

> 需在项目根目录 `jx_coupons/` 下运行，使 `algorithm` 作为包被导入。
