"""新增题目的元数据补充。"""
from meta.helpers import _m

PROBLEMS = {
    'paradigms/dynamic_programming/linear_dp.py::max_subarray': _m(
        '53', '最大子数组和',
        '给你一个整数数组 nums，'
        '请找出一个具有最大和的连续子数组（子数组最少包含一个元素），'
        '返回其最大和。\n\n'
        '子数组是数组中的一个连续部分。'
        '本题可用 Kadane 算法在线性时间内求解：'
        '遍历时维护「以当前元素结尾的最大子数组和」，'
        '并在每个位置更新全局最优值。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁵；-10⁴ ≤ nums[i] ≤ 10⁴。',
        [
            '示例 1：nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6。'
            '连续子数组 [4, -1, 2, 1] 的和最大，为 6。',
            '示例 2：nums = [1] → 1。',
            '示例 3：nums = [5, 4, -1, 7, 8] → 23。'
            '连续子数组 [5, 4, -1, 7, 8] 的和最大。',
        ],
        [
            '初始化 best = cur = nums[0]，分别表示全局最优与「以当前位置结尾」的最优和。',
            '从 nums[1] 起遍历每个 value：cur = max(value, cur + value)，'
            '即要么从 value 重新开始，要么接在前一段后面。',
            '每步更新 best = max(best, cur)，记录迄今为止的最大子数组和。',
            '遍历结束返回 best；无需额外数组，空间 O(1)。',
        ],
        '动态规划',
        code_notes=[
            'best = cur = nums[0] — 首元素既是初始局部最优也是全局最优。',
            'for value in nums[1:] — 从第二个元素起线性扫描。',
            'cur = max(value, cur + value) — Kadane 核心：延伸或重启子数组。',
            'best = max(best, cur) — 全局最大值与当前结尾最优同步更新。',
            '子数组至少含一个元素，故 cur 不会为「空子数组」的 0。',
            '全负数时 best 仍为其中最大单个元素（如 [-1] → -1）。',
            '也可写成 dp[i] = max(nums[i], dp[i-1]+nums[i]) 的一维滚动形式。',
        ],
        complexity='时间 O(n)，空间 O(1)，n = len(nums)。',
    ),
    'paradigms/dynamic_programming/linear_dp.py::climbing_stairs': _m(
        '70', '爬楼梯',
        '假设你正在爬楼梯，需要 n 阶才能到达楼顶。'
        '每次你可以爬 1 或 2 个台阶。'
        '问有多少种不同的方法可以爬到楼顶？\n\n'
        '到达第 i 阶的方法数等于「从 i-1 阶爬 1 步」与「从 i-2 阶爬 2 步」之和，'
        '即斐波那契递推。'
        '本实现用两个变量滚动，避免 O(n) 数组。\n\n'
        '约束：1 ≤ n ≤ 45；答案保证在 32 位有符号整数范围内。',
        [
            '示例 1：n = 2 → 2。'
            '1+1 与 2 两种。',
            '示例 2：n = 3 → 3。'
            '1+1+1、1+2、2+1 三种。',
            '示例 3：n = 1 → 1。'
            '只有一种方法。',
        ],
        [
            '边界：n ≤ 2 时直接返回 n（1 阶 1 种，2 阶 2 种）。',
            '初始化 prev = 1（f(1)）、cur = 2（f(2)）。',
            '从 i = 3 到 n 循环：prev, cur = cur, prev + cur，滚动更新相邻两项。',
            '循环结束后 cur 即为 f(n)，返回 cur。',
        ],
        '动态规划',
        code_notes=[
            'if n <= 2: return n — 小规模直接返回，避免多余循环。',
            'prev, cur = 1, 2 — 对应 f(1)、f(2)，仅保留最近两项。',
            'for _ in range(3, n + 1) — 从第 3 阶递推到第 n 阶。',
            'prev, cur = cur, prev + cur — 斐波那契滚动，无额外数组。',
            'f(i) = f(i-1) + f(i-2) — 最后一步走 1 阶或 2 阶的组合数。',
            '与「最小花费爬楼梯」同结构，本题无权重仅计数。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'paradigms/dynamic_programming/linear_dp.py::house_robber': _m(
        '198', '打家劫舍',
        '你是一个专业的小偷，计划偷窃沿街的房屋。'
        '每间房内都藏有一定现金，'
        '相邻的房屋装有相互连通的防盗系统，'
        '若两相邻房屋同时被偷则会触发报警。\n\n'
        '给定一个非负整数数组 nums 表示每间房的金额，'
        '计算在不触动报警的情况下，一夜之内能够偷窃到的最高金额。\n\n'
        '约束：1 ≤ nums.length ≤ 100；0 ≤ nums[i] ≤ 400。',
        [
            '示例 1：nums = [1, 2, 3, 1] → 4。'
            '偷第 1、3 间（1 + 3）。',
            '示例 2：nums = [2, 7, 9, 3, 1] → 12。'
            '偷第 1、3、5 间（2 + 9 + 1）。',
            '示例 3：nums = [2, 1, 1, 2] → 4。'
            '偷第 1、4 间。',
        ],
        [
            '定义 dp：到当前房屋为止的最大收益；'
            '偷当前屋则收益为 prev + value，不偷则为 cur。',
            '初始化 prev = 0（前 i-2 间最优）、cur = 0（前 i-1 间最优）。',
            '遍历 nums：prev, cur = cur, max(cur, prev + value)，滚动更新。',
            '遍历结束 cur 即为全数组最优，返回 cur。',
        ],
        '动态规划',
        code_notes=[
            'prev, cur = 0, 0 — 双变量滚动，prev 表示 dp[i-2]，cur 表示 dp[i-1]。',
            'for value in nums — 按房屋顺序线性扫描。',
            'prev, cur = cur, max(cur, prev + value) — 偷或不偷取较大值。',
            'max(cur, prev + value) — 不偷当前屋保留 cur；偷则 prev + 当前金额。',
            '相邻约束通过跳过 prev+1 的「偷当前」路径自然满足。',
            '全 0 时返回 0；单元素返回 nums[0]。',
            '打家劫舍 II/III 为本题的环形与树形扩展。',
        ],
        complexity='时间 O(n)，空间 O(1)，n = len(nums)。',
    ),
    'patterns/graph/graph.py::num_islands': _m(
        '200', '岛屿数量',
        '给你一个由「1」（陆地）和「0」（水）组成的 m×n 二维字符网格 grid，'
        '「岛屿」是由相邻陆地（上下左右）连接形成的最大区域；'
        '相邻仅指四连通，不包括对角线。\n\n'
        '网格四周均被水包围，'
        '若网格中不存在陆地则岛屿数量为 0。'
        '请计算网格中岛屿的数量。\n\n'
        '约束：m == grid.length；n == grid[i].length；'
        '1 ≤ m, n ≤ 300；grid[i][j] 为「0」或「1」。',
        [
            '示例 1：grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]] → 1。',
            '示例 2：grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]] → 3。',
            '示例 3：grid = [] → 0。'
            '空网格无岛屿。',
        ],
        [
            '若 grid 为空直接返回 0；初始化 count = 0。',
            '双重循环扫描每个格子 (i, j)，遇 grid[i][j] == "1" 则 count += 1。',
            '对每个新发现的陆地启动 DFS：将当前格标记为 "0"（visited），'
            '并递归四方向扩展。',
            'DFS 边界：越界或当前格不为 "1" 则返回。',
            '全部扫描完成后 count 即为岛屿数量。',
        ],
        '图论',
        code_notes=[
            'if not grid: return 0 — 空矩阵边界。',
            'dfs(r, c) — 深度优先搜索淹没整块连通陆地。',
            'grid[r][c] = "0" — 原地标记已访问，省去 visited 数组。',
            '四方向 dfs(r±1, c)、dfs(r, c±1) — 仅上下左右连通。',
            'if grid[i][j] == "1": count += 1; dfs(i, j) — 每块新陆地计一次。',
            '也可用 BFS 队列实现，复杂度同级。',
            '修改输入 grid，若需保留原矩阵应拷贝一份。',
        ],
        complexity='时间 O(m×n)，空间 O(m×n)（递归栈最坏全为陆地）。',
    ),
    'patterns/graph/graph.py::clone_graph': _m(
        '133', '克隆图',
        '给你无向连通图中一个节点的引用，'
        '请返回该图的深拷贝（克隆）。\n\n'
        '图中的每个节点都包含一个值 val（int）'
        '和一个邻居列表 neighbors。'
        '深拷贝需新建所有节点，'
        '且克隆图中相同 val 的节点在原图中不一定是同一节点；'
        '重点是复制邻接关系，并用哈希表避免重复克隆与死循环。\n\n'
        '约束：节点数 0 ≤ n ≤ 100；1 ≤ Node.val ≤ 100；'
        'Node.val 各节点互不相同；无自环；图连通。',
        [
            '示例 1：adjList = [[2,4],[1,3],[2,4],[1,3]] → 结构相同的克隆图。',
            '示例 2：adjList = [[]] → 单节点克隆。',
            '示例 3：node = null → null。'
            '空图返回空。',
        ],
        [
            '若 node 为 None 返回 None。',
            '维护 cloned: dict[GraphNode, GraphNode] 映射原节点到克隆节点。',
            'DFS(cur)：若 cur 已在 cloned 中则直接返回已有克隆。',
            '否则创建 copy = GraphNode(cur.val)，写入 cloned[cur] = copy。',
            '递归克隆每个邻居 nei，append 到 copy.neighbors。',
            '从入口 node 启动 DFS 并返回克隆根节点。',
        ],
        '图论',
        code_notes=[
            'cloned: dict[GraphNode, GraphNode] — 原节点到克隆节点的映射，防环与重复。',
            'if cur in cloned: return cloned[cur] — 已克隆则复用，避免无限递归。',
            'copy = GraphNode(cur.val) — 先创建节点再递归邻居。',
            'cloned[cur] = copy — 在递归邻居前登记，处理环（如 A-B-A）。',
            'for nei in cur.neighbors: copy.neighbors.append(dfs(nei)) — 深拷贝边。',
            'BFS + 哈希表同样可行；DFS 代码更简洁。',
            'GraphNode 定义见 algorithm.common.nodes。',
        ],
        complexity='时间 O(V + E)，空间 O(V)，V 为节点数，E 为边数。',
    ),
    'patterns/graph/graph.py::course_schedule': _m(
        '207', '课程表',
        '你这个学期必须选修 numCourses 门课程，'
        '编号为 0 到 numCourses - 1。'
        '部分课程有先修要求：prerequisites[i] = [a, b] 表示选 a 前必须先选 b。\n\n'
        '请判断是否可能完成所有课程的学习。'
        '等价于判断有向图是否存在环；'
        '无环则存在拓扑序，可以按序修完所有课。\n\n'
        '约束：1 ≤ numCourses ≤ 2000；0 ≤ prerequisites.length ≤ 5000；'
        'prerequisites[i].length == 2；0 ≤ a_i, b_i < numCourses；'
        '所有 [a_i, b_i] 互不相同。',
        [
            '示例 1：numCourses = 2, prerequisites = [[1,0]] → true。'
            '先修 0 再修 1 即可。',
            '示例 2：numCourses = 2, prerequisites = [[1,0],[0,1]] → false。'
            '0 与 1 互相依赖，形成环。',
            '示例 3：numCourses = 1, prerequisites = [] → true。'
            '无先修要求。',
        ],
        [
            '建图：prereq → course，并统计每门课 indegree。',
            '将 indegree 为 0 的节点入队（无先修，可先修）。',
            'BFS：出队 node，taken += 1；对其后继 nxt  indegree -= 1，'
            '若变为 0 则入队。',
            'BFS 结束后若 taken == numCourses 则无环，返回 True；否则 False。',
        ],
        '图论',
        code_notes=[
            'graph[prereq].append(course) — 有向边：先修 → 后续课程。',
            'indegree[course] += 1 — 入度统计后续课的前置数量。',
            'queue = deque(i for i in range(numCourses) if indegree[i] == 0) — 初始可修课程。',
            'while queue: node = queue.popleft(); taken += 1 — Kahn 拓扑排序。',
            'indegree[nxt] -= 1; if indegree[nxt] == 0: queue.append(nxt) — 解锁后续课。',
            'return taken == numCourses — 全部出队则无环；否则存在环。',
            '也可用 DFS 三色标记检测环。',
        ],
        complexity='时间 O(V + E)，空间 O(V + E)，V = numCourses。',
    ),
    'data_structures/trie/trie.py::Trie.__init__': _m(
        '208', '实现 Trie-初始化',
        'Trie（发音类似 "try"）即字典树，'
        '是一种用于高效存储与检索字符串数据的多叉树结构。\n\n'
        '请实现 Trie 类：'
        'Trie() 初始化前缀树对象；'
        'insert(word) 插入字符串 word；'
        'search(word) 查找完整单词；'
        'startsWith(prefix) 查找前缀。\n\n'
        '约束：1 ≤ word.length, prefix.length ≤ 2000；'
        'word 和 prefix 仅由小写英文字母组成；'
        'insert、search、startsWith 最多调用 3×10⁴ 次。',
        [
            '示例：trie = Trie() 后 children = {}，is_end = False。',
            '示例：insert("apple") 后沿 a-p-p-l-e 路径建节点，末节点 is_end = True。',
            '示例：search("app") → false；startsWith("app") → true。',
        ],
        [
            '创建 Trie 根节点，无需额外参数。',
            'self.children: dict[str, Trie] 存储当前节点的子节点映射。',
            'self.is_end: bool 标记从根到当前节点是否构成完整单词。',
            '根节点 is_end 初始为 False；insert/search 均从 self 出发。',
        ],
        '字典树',
        code_notes=[
            'self.children: dict[str, Trie] — 字符到子 Trie 节点的映射。',
            'self.is_end = False — 默认非单词结尾，insert 末字符处置 True。',
            'dict 实现比 26 长度数组更省空间（稀疏字母表）。',
            '根节点不存储字符，仅作为入口。',
            '与 LeetCode 208 设计题一致，后续三个方法操作同一棵树。',
        ],
        complexity='时间 O(1)，空间 O(1)（不含后续 insert 建树）。',
    ),
    'data_structures/trie/trie.py::Trie.insert': _m(
        '208', '实现 Trie-插入',
        '向 Trie 中插入字符串 word。'
        '若 word 已存在则更新结尾标记；'
        '若路径不存在则逐字符创建新节点。\n\n'
        '插入后 search(word) 应返回 True，'
        'startsWith(word 的任意前缀) 也应返回 True。\n\n'
        '约束：word 仅由小写英文字母组成；1 ≤ word.length ≤ 2000。',
        [
            '示例：insert("apple") 后 search("apple") → true。',
            '示例：insert("app") 后 search("app") → true，search("ap") → false。',
            '示例：insert("a") 后 startsWith("a") → true。',
        ],
        [
            'node 从 self（根）出发，逐字符 ch 遍历 word。',
            '若 ch 不在 node.children，创建 Trie() 子节点并登记。',
            'node 沿 ch 移动到子节点。',
            'word 遍历完毕后 node.is_end = True，标记完整单词。',
        ],
        '字典树',
        code_notes=[
            'node = self — 从根开始，不存储根字符。',
            'for ch in word — 按字符顺序向下延伸路径。',
            'if ch not in node.children: node.children[ch] = Trie() — 懒创建子节点。',
            'node = node.children[ch] — 移动到下一层。',
            'node.is_end = True — 末字符节点标记单词结束。',
            'insert 与 search 共享 children 结构，search 额外检查 is_end。',
            '平均路径长度等于 word 长度，无回溯。',
        ],
        complexity='时间 O(L)，空间 O(L)（最坏新建 L 个节点），L = len(word)。',
    ),
    'data_structures/trie/trie.py::Trie.search': _m(
        '208', '实现 Trie-查找单词',
        '查找 Trie 中是否存在完整单词 word。'
        '必须匹配完整路径且末节点 is_end 为 True；'
        '仅匹配前缀但非完整单词时返回 False。\n\n'
        '约束：word 仅由小写英文字母组成；1 ≤ word.length ≤ 2000。',
        [
            '示例：insert("apple") 后 search("apple") → true。',
            '示例：search("app") → false（"app" 仅为前缀未单独插入）。',
            '示例：search("ban") → false（不存在）。',
        ],
        [
            'node 从根出发，逐字符 ch 在 children 中查找下一节点。',
            '若某字符不存在则立即返回 False。',
            '全部字符匹配后，返回 node.is_end 是否为 True。',
        ],
        '字典树',
        code_notes=[
            'node = self — 从根开始查找。',
            'for ch in word — 沿字符路径向下。',
            'if ch not in node.children: return False — 路径中断，单词不存在。',
            'node = node.children[ch] — 进入子节点。',
            'return node.is_end — 必须到达单词结尾标记，区分前缀与完整词。',
            'startsWith 与本方法类似但不检查 is_end。',
            '最坏需走完 word 全长才判定。',
        ],
        complexity='时间 O(L)，空间 O(1)，L = len(word)。',
    ),
    'data_structures/trie/trie.py::Trie.starts_with': _m(
        '208', '实现 Trie-查找前缀',
        '查找 Trie 中是否存在以 prefix 为前缀的单词。'
        '只要路径存在即返回 True，'
        '不要求 prefix 本身是已插入的完整单词。\n\n'
        '约束：prefix 仅由小写英文字母组成；1 ≤ prefix.length ≤ 2000。',
        [
            '示例：insert("apple") 后 startsWith("app") → true。',
            '示例：startsWith("b") → false。',
            '示例：startsWith("apple") → true（完整词也是自身前缀）。',
        ],
        [
            'node 从根出发，逐字符 ch 遍历 prefix。',
            '若 ch 不在 node.children 则返回 False。',
            '全部字符均存在则返回 True，无需检查 is_end。',
        ],
        '字典树',
        code_notes=[
            'node = self — 前缀查找同样从根开始。',
            'for ch in prefix — 只验证路径存在性。',
            'if ch not in node.children: return False — 前缀路径不存在。',
            'node = node.children[ch] — 继续向下。',
            'return True — 走完 prefix 即成功，不检查 is_end。',
            'search("app") 需 is_end；startsWith("app") 仅需路径。',
            '可用于自动补全、前缀过滤等场景。',
        ],
        complexity='时间 O(L)，空间 O(1)，L = len(prefix)。',
    ),
    'data_structures/array/basic.py::max_product_subarray': _m(
        '152', '乘积最大子数组',
        '给你一个整数数组 nums，'
        '找出数组中乘积最大的非空连续子数组，'
        '返回该子数组的乘积。\n\n'
        '与最大子数组和不同，负数乘负数可能变为正数，'
        '因此需同时维护「以当前位置结尾的最大乘积」与「最小乘积」。'
        '遇到负数时交换 cur_max 与 cur_min。\n\n'
        '约束：1 ≤ nums.length ≤ 2×10⁴；-10 ≤ nums[i] ≤ 10；'
        '子数组乘积在 32 位整数范围内。',
        [
            '示例 1：nums = [2, 3, -2, 4] → 6。'
            '子数组 [2, 3] 乘积最大。',
            '示例 2：nums = [-2, 0, -1] → 0。'
            '结果不能是 2，因为 [-2, -1] 不是连续子数组（中间有 0）。',
            '示例 3：nums = [-2] → -2。',
        ],
        [
            '初始化 best = cur_max = cur_min = nums[0]。',
            '从 nums[1] 起遍历 value：若 value < 0 则交换 cur_max 与 cur_min。',
            'cur_max = max(value, cur_max * value)；cur_min = min(value, cur_min * value)。',
            'best = max(best, cur_max) 更新全局最大乘积。',
            '返回 best。',
        ],
        '数组',
        code_notes=[
            'best = cur_max = cur_min = nums[0] — 三个变量跟踪全局最大、局部最大/最小积。',
            'if value < 0: cur_max, cur_min = cur_min, cur_max — 负数翻转大小关系。',
            'cur_max = max(value, cur_max * value) — 延伸或重启最大积子数组。',
            'cur_min = min(value, cur_min * value) — 最小积可能在下个负数处变最大。',
            'best = max(best, cur_max) — 全局最优只来自 cur_max。',
            '含 0 时 cur_max/cur_min 会被重置为 0 或当前值。',
            'Kadane 乘积版，空间 O(1)。',
        ],
        complexity='时间 O(n)，空间 O(1)，n = len(nums)。',
    ),
    'data_structures/array/basic.py::next_permutation': _m(
        '31', '下一个排列',
        '整数数组 nums 表示一个排列，'
        '请原地修改 nums，'
        '使其变为字典序下一个更大的排列。'
        '若已是最大排列（降序），则重排为最小排列（升序）。\n\n'
        '必须原地修改，仅使用 O(1) 额外空间。\n\n'
        '约束：1 ≤ nums.length ≤ 100；0 ≤ nums[i] ≤ 100。',
        [
            '示例 1：nums = [1, 2, 3] → [1, 3, 2]。'
            '下一个排列为 132。',
            '示例 2：nums = [3, 2, 1] → [1, 2, 3]。'
            '已是最大，循环到最小。',
            '示例 3：nums = [1, 1, 5] → [1, 5, 1]。',
        ],
        [
            '从右向左找第一个 nums[i] < nums[i+1] 的 i（最长升序后缀的左邻）。',
            '若 i < 0 说明全降序，直接反转 i+1 到末尾得最小排列。',
            '否则从末尾找第一个 nums[j] > nums[i] 的 j，交换 nums[i] 与 nums[j]。',
            '反转 i+1 到末尾，使后缀变为最小升序，得到下一个排列。',
        ],
        '数组',
        code_notes=[
            'i = len(nums) - 2; while nums[i] >= nums[i+1]: i -= 1 — 找「拐点」i。',
            'if i >= 0 — i < 0 表示无更大排列，走全反转分支。',
            'j = len(nums) - 1; while nums[j] <= nums[i]: j -= 1 — 找后缀中大于 nums[i] 的最小者。',
            'nums[i], nums[j] = nums[j], nums[i] — 交换使第 i 位尽量小增幅。',
            'left, right = i + 1, len(nums) - 1 — 双指针反转后缀。',
            'while left < right: swap — 后缀变升序，即下一个排列。',
            '函数返回 None，结果原地保存在 nums 中。',
        ],
        complexity='时间 O(n)，空间 O(1)，n = len(nums)。',
    ),
    'data_structures/array/basic.py::product_except_self': _m(
        '238', '除自身以外数组的乘积',
        '给你一个整数数组 nums，'
        '返回数组 answer，'
        '其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。\n\n'
        '题目保证任意前缀积、后缀积均在 32 位整数范围内。'
        '要求 O(n) 时间且不使用除法；'
        '本实现用两次扫描分别累乘前缀与后缀。\n\n'
        '约束：2 ≤ nums.length ≤ 10⁵；-30 ≤ nums[i] ≤ 30；'
        '保证 answer[i] 在 32 位整数范围内。',
        [
            '示例 1：nums = [1, 2, 3, 4] → [24, 12, 8, 6]。',
            '示例 2：nums = [-1, 1, 0, -3, 3] → [0, 0, 9, 0, 0]。'
            '含 0 时多数位置乘积为 0。',
            '示例 3：nums = [2, 3] → [3, 2]。',
        ],
        [
            '初始化 result = [1] * n，prefix = 1。',
            '从左到右：result[i] = prefix，再 prefix *= nums[i]。'
            '此时 result[i] 为 nums[i] 左侧所有元素之积。',
            'suffix = 1，从右到左：result[i] *= suffix，再 suffix *= nums[i]。',
            '合并后缀积后 result[i] 即为除自身外全体乘积，返回 result。',
        ],
        '数组',
        code_notes=[
            'result = [1] * n — 输出数组，先存前缀积。',
            'prefix = 1 — 从左到右累积 nums[0..i-1] 的乘积。',
            'result[i] = prefix; prefix *= nums[i] — 第一遍只算左侧。',
            'suffix = 1 — 从右到左累积 nums[i+1..n-1] 的乘积。',
            'result[i] *= suffix; suffix *= nums[i] — 第二遍乘右侧，O(1) 额外空间。',
            '不用除法，天然处理 0 与负数。',
            'Follow-up O(1) 空间指除输出数组外；输出数组不计入额外空间。',
        ],
        complexity='时间 O(n)，空间 O(1)（不计输出数组），n = len(nums)。',
    ),
    'patterns/sliding_window/window.py::min_window': _m(
        '76', '最小覆盖子串',
        '给你一个字符串 s 和一个字符串 t，'
        '返回 s 中涵盖 t 所有字符（含重复）的最小子串；'
        '若 s 中不存在这样的子串则返回空字符串 ""。\n\n'
        '「涵盖」指子串中包含 t 中每个字符至少相应次数。'
        '本实现用哈希表 need 记录需求，'
        'missing 计数尚未满足的总字符数，'
        '右扩左缩维护最小窗口。\n\n'
        '约束：m == s.length, n == t.length；'
        '1 ≤ m, n ≤ 10⁵；s 和 t 由英文字母组成。',
        [
            '示例 1：s = "ADOBECODEBANC", t = "ABC" → "BANC"。'
            '最小覆盖子串为 "BANC"。',
            '示例 2：s = "a", t = "a" → "a"。',
            '示例 3：s = "a", t = "aa" → ""。'
            's 中 a 数量不足。',
        ],
        [
            '统计 t 中各字符需求 need，missing = len(t)（待匹配字符总数）。',
            '右指针 right 扩展窗口：若 s[right] 在 need 中则更新 need 与 missing。',
            '当 missing == 0 时窗口已覆盖 t，尝试左缩：'
            '记录更短窗口，左移 left 并恢复 need[left_ch]。',
            '重复至 right 扫完；若找到有效窗口则返回 s[start:start+best_len]，否则 ""。',
        ],
        '滑动窗口',
        code_notes=[
            'need: dict[str, int] — t 中各字符剩余需求次数。',
            'missing = len(t) — 简化的「未满足字符计数」，need[ch] 从 >0 变 ≤0 时减 1。',
            'for right, ch in enumerate(s) — 右指针单向扩展，O(n)。',
            'while missing == 0 — 窗口有效时尝试收缩左边界。',
            'best_len, start — 记录最短窗口长度与起始下标。',
            'need[left_ch] += 1; if need[left_ch] > 0: missing += 1 — 左移后可能失覆盖。',
            'if not t: return "" — 空 t 的边界（本题 n ≥ 1 通常不触发）。',
        ],
        complexity='时间 O(|s| + |t|)，空间 O(|s| + |t|) 哈希表。',
    ),
    'patterns/binary_search/basic.py::search_rotated': _m(
        '33', '搜索旋转排序数组',
        '整数数组 nums 按升序排列后在某个下标 k 上旋转，'
        '例如 [0,1,2,4,5,6,7] 旋转为 [4,5,6,7,0,1,2]。'
        '给定目标 target，'
        '若存在则返回下标，否则返回 -1。\n\n'
        '数组中无重复元素；'
        '需在 O(log n) 时间内完成。\n\n'
        '约束：1 ≤ nums.length ≤ 5000；-10⁴ ≤ nums[i], target ≤ 10⁴；'
        'nums 各元素互不相同；nums 是某个升序数组的旋转。',
        [
            '示例 1：nums = [4,5,6,7,0,1,2], target = 0 → 4。',
            '示例 2：nums = [4,5,6,7,0,1,2], target = 3 → -1。',
            '示例 3：nums = [1], target = 0 → -1。',
        ],
        [
            'left、right 二分，mid = (left + right) // 2。',
            '若 nums[mid] == target 直接返回 mid。',
            '判断左半 [left, mid] 是否有序：nums[left] <= nums[mid]。',
            '若左半有序且 target 落在 [nums[left], nums[mid]) 内，则 right = mid - 1；'
            '否则 left = mid + 1。',
            '若右半有序，对称判断 target 是否在 (nums[mid], nums[right]] 内并收缩区间。',
            '循环结束返回 -1。',
        ],
        '二分查找',
        code_notes=[
            'while left <= right — 闭区间二分。',
            'if nums[mid] == target: return mid — 命中直接返回。',
            'if nums[left] <= nums[mid] — 左段 [left,mid] 有序（含 mid 与 left 相等）。',
            'nums[left] <= target < nums[mid] — target 在有序左段内，缩至左半。',
            'else: left = mid + 1 — target 不在左段，去右半。',
            'else 分支：右段 [mid,right] 有序，对称判断 target 范围。',
            '无重复元素保证「<=」判断左/右哪段有序时不歧义。',
        ],
        complexity='时间 O(log n)，空间 O(1)，n = len(nums)。',
    ),
    'patterns/binary_search/basic.py::search_range': _m(
        '34', '在排序数组中查找元素的第一个和最后一个位置',
        '给定一个按非递减顺序排列的整数数组 nums 和目标值 target，'
        '找出 target 在数组中的开始位置和结束位置。\n\n'
        '若数组中不存在 target，返回 [-1, -1]。'
        '要求 O(log n) 时间；'
        '本实现分别用 lower_bound 与 upper_bound 找左端与「右端下一位置」。\n\n'
        '约束：0 ≤ nums.length ≤ 10⁵；-10⁹ ≤ nums[i], target ≤ 10⁹；'
        'nums 为非递减数组。',
        [
            '示例 1：nums = [5,7,7,8,8,10], target = 8 → [3, 4]。',
            '示例 2：nums = [5,7,7,8,8,10], target = 6 → [-1, -1]。',
            '示例 3：nums = [], target = 0 → [-1, -1]。',
        ],
        [
            'lower_bound：左闭右开 [lo, hi)，找第一个 nums[mid] >= target 的位置 left。',
            '若 left == len(nums) 或 nums[left] != target，说明不存在，返回 [-1, -1]。',
            'upper_bound：找第一个 nums[mid] > target 的位置，'
            '右端下标为 upper_bound() - 1。',
            '返回 [left, upper_bound() - 1] 即为 target 的起止位置（闭区间）。',
        ],
        '二分查找',
        code_notes=[
            'lower_bound — nums[mid] < target 则 lo = mid + 1，否则 hi = mid。',
            'upper_bound — nums[mid] <= target 则 lo = mid + 1，否则 hi = mid。',
            '左闭右开 while lo < hi — 与标准库 bisect 一致。',
            'left = lower_bound() — 第一个 >= target 的下标。',
            'if left == len(nums) or nums[left] != target: return [-1, -1] — 不存在。',
            'return [left, upper_bound() - 1] — 右端为最后一个 <= target 的位置。',
            '也可一次二分后向两侧扩展，但 O(log n) 双边界更优。',
            '全等数组如 [8,8,8] target=8 正确返回 [0,2]。',
        ],
        complexity='时间 O(log n)，空间 O(1)，n = len(nums)。',
    ),
    'patterns/two_pointers/array.py::two_sum_ii': _m(
        '167', '两数之和 II - 输入有序数组',
        '给你一个下标从 1 开始的整数数组 numbers，'
        '该数组已按非递减顺序排列。'
        '请找出两个数，使它们的和等于 target，'
        '返回这两个数的下标（从 1 开始）。\n\n'
        '题目保证恰好存在一组解，'
        '且同一元素不能使用两次。\n\n'
        '约束：2 ≤ numbers.length ≤ 3×10⁴；-1000 ≤ numbers[i] ≤ 1000；'
        'numbers 非递减；-1000 ≤ target ≤ 1000。',
        [
            '示例 1：numbers = [2, 7, 11, 15], target = 9 → [1, 2]。'
            '2 + 7 = 9。',
            '示例 2：numbers = [2, 3, 4], target = 6 → [1, 3]。',
            '示例 3：numbers = [-1, 0], target = -1 → [1, 2]。',
        ],
        [
            '左右双指针 left = 0，right = len(numbers) - 1。',
            '计算 total = numbers[left] + numbers[right]。',
            '若 total == target 返回 [left + 1, right + 1]（题要求 1-indexed）。',
            '若 total < target，left += 1 增大和；否则 right -= 1 减小和。',
            '题目保证有解，循环必命中。',
        ],
        '双指针',
        code_notes=[
            'left, right = 0, len(numbers) - 1 — 首尾夹逼。',
            'total = numbers[left] + numbers[right] — 当前两数之和。',
            'if total == target: return [left + 1, right + 1] — 下标从 1 开始。',
            'if total < target: left += 1 — 和太小，左指针右移增大。',
            'else: right -= 1 — 和太大，右指针左移减小。',
            '有序性保证移动方向单调，不会漏解。',
            '与哈希版两数之和不同，本题利用排序 O(n) 双指针。',
        ],
        complexity='时间 O(n)，空间 O(1)，n = len(numbers)。',
    ),
    'data_structures/hash_map/hash_map.py::contains_duplicate': _m(
        '217', '存在重复元素',
        '给你一个整数数组 nums，'
        '若任一值在数组中出现至少两次则返回 true；'
        '若每个元素互不相同则返回 false。\n\n'
        '本实现将 nums 转为 set 比较长度，'
        '代码最简且均摊 O(n)。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁵；-10⁹ ≤ nums[i] ≤ 10⁹。',
        [
            '示例 1：nums = [1, 2, 3, 1] → true。',
            '示例 2：nums = [1, 2, 3, 4] → false。',
            '示例 3：nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] → true。',
        ],
        [
            '将 nums 转为集合 set(nums)，集合自动去重。',
            '比较 len(nums) 与 len(set(nums)) 是否相等。',
            '不等则说明存在重复，返回 True；相等返回 False。',
        ],
        '哈希表',
        code_notes=[
            'return len(nums) != len(set(nums)) — 一行判定是否有重复。',
            'set(nums) — 构建哈希集合，均摊 O(n)。',
            '长度不等 ⟺ 至少一个元素出现两次以上。',
            '也可边遍历边 seen.add，遇重复提前返回 True。',
            '空间 O(n) 存储集合；时间 O(n)。',
            'Follow-up：若不能分配额外空间需排序后相邻比较 O(n log n)。',
        ],
        complexity='时间 O(n)，空间 O(n)，n = len(nums)。',
    ),
    'data_structures/hash_map/hash_map.py::longest_consecutive': _m(
        '128', '最长连续序列',
        '给定未排序整数数组 nums，'
        '找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。\n\n'
        '要求 O(n) 时间；'
        '本实现先将 nums 放入 set，'
        '仅当 num-1 不在集合中时才以 num 为起点向右扩展计数。\n\n'
        '约束：0 ≤ nums.length ≤ 10⁵；-10⁹ ≤ nums[i] ≤ 10⁹。',
        [
            '示例 1：nums = [100, 4, 200, 1, 3, 2] → 4。'
            '最长连续序列 [1, 2, 3, 4]。',
            '示例 2：nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] → 9。'
            '序列 [0, 1, ..., 8]。',
            '示例 3：nums = [] → 0。',
        ],
        [
            'num_set = set(nums) 实现 O(1) 查找。',
            '遍历 num_set 中每个 num：若 num - 1 在集合中则跳过（非序列起点）。',
            '以 num 为起点，while num + length in num_set 则 length += 1。',
            'best = max(best, length) 更新最长长度；返回 best。',
        ],
        '哈希表',
        code_notes=[
            'num_set = set(nums) — O(n) 建集，支持 O(1) 成员检测。',
            'if num - 1 in num_set: continue — 只从连续段最小元素起算，避免重复扫描。',
            'length = 1 — 当前连续段长度，从 num 向右扩展。',
            'while num + length in num_set: length += 1 — 逐个数检查是否存在。',
            'best = max(best, length) — 全局最长。',
            '每个元素最多被访问两次（起点判定 + 扩展），均摊 O(n)。',
            '排序后线性扫描也可但为 O(n log n)。',
        ],
        complexity='时间 O(n)，空间 O(n)，n = len(nums)。',
    ),
    'data_structures/linked_list/linked_list.py::reverse_k_group': _m(
        '25', 'K 个一组翻转链表',
        '给你链表 head 和正整数 k，'
        '每 k 个节点一组进行翻转，'
        '若剩余节点不足 k 个则保持原顺序。\n\n'
        '返回翻转后的链表头节点。'
        '本实现先定位每组第 k 个节点，'
        '再组内迭代反转并连接前后组。\n\n'
        '约束：链表节点数 n 满足 0 ≤ k ≤ n ≤ 5000；'
        '0 ≤ Node.val ≤ 1000。',
        [
            '示例 1：head = [1,2,3,4,5], k = 2 → [2,1,4,3,5]。',
            '示例 2：head = [1,2,3,4,5], k = 3 → [3,2,1,4,5]。'
            '最后不足 3 个不翻转。',
            '示例 3：head = [1], k = 1 → [1]。',
        ],
        [
            'dummy 哨兵指向 head，prev_group 指向上一组末尾（初始 dummy）。',
            '循环：从 prev_group 走 k 步找 kth，不足 k 则 return dummy.next。',
            'group_next = kth.next 为下一组起点；组内 prev/cur 迭代反转 k 个节点。',
            '反转后 kth 变组头、原组头 tail 接 group_next；'
            'prev_group.next = kth，prev_group = tail 处理下一组。',
        ],
        '链表',
        code_notes=[
            'dummy = ListNode(0, head) — 哨兵简化头节点变更。',
            'kth = prev_group; for _ in range(k): kth = kth.next — 定位本组第 k 个。',
            'if not kth: return dummy.next — 剩余不足 k，结束。',
            'group_next = kth.next — 下一组起点，也是反转后的 cur 终止条件。',
            'prev, cur = kth.next, prev_group.next — 组内标准迭代反转。',
            'while cur != group_next — 反转 [prev_group.next, kth] 共 k 个节点。',
            'prev_group.next = kth; prev_group = tail — 接好组间指针，tail 为原组头。',
        ],
        complexity='时间 O(n)，空间 O(1)，n 为链表长度。',
    ),
    'data_structures/matrix/matrix.py::rotate_image': _m(
        '48', '旋转图像',
        '给定 n×n 二维矩阵 matrix 表示图像，'
        '请你原地顺时针旋转 90 度。\n\n'
        '必须原地修改 matrix，'
        '本实现分两步：'
        '先沿主对角线转置，再每行左右反转，'
        '等价于顺时针 90°。\n\n'
        '约束：n == matrix.length == matrix[i].length；'
        '1 ≤ n ≤ 20；-1000 ≤ matrix[i][j] ≤ 1000。',
        [
            '示例 1：matrix = [[1,2,3],[4,5,6],[7,8,9]] → [[7,4,1],[8,5,2],[9,6,3]]。',
            '示例 2：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] → '
            '[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]。',
            '示例 3：matrix = [[1]] → [[1]]。',
        ],
        [
            '转置：对 i in [0,n)，j in (i+1,n)，交换 matrix[i][j] 与 matrix[j][i]。',
            '逐行反转：对 matrix 每一行执行 row.reverse()。',
            '两步完成后 matrix 即为顺时针旋转 90° 的结果。',
        ],
        '矩阵',
        code_notes=[
            'n = len(matrix) — 方阵边长。',
            'for i in range(n): for j in range(i + 1, n) — 只交换上三角，避免重复。',
            'matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] — 主对角线转置。',
            'for row in matrix: row.reverse() — 每行左右翻转。',
            '转置 + 行反转 = 顺时针 90°；转置 + 列反转 = 逆时针 90°。',
            '原地 O(1) 额外空间，无需新建矩阵。',
            '也可四层循环直接映射 (i,j)→(j,n-1-i)，但代码较长。',
        ],
        complexity='时间 O(n²)，空间 O(1)，n 为矩阵边长。',
    ),
    'data_structures/matrix/matrix.py::search_sorted_matrix': _m(
        '74', '搜索二维矩阵',
        '给你一个 m×n 矩阵 matrix，'
        '每行从左到右升序，'
        '且每行第一个元素大于上一行最后一个元素（等价于整体升序的一维数组）。\n\n'
        '给定 target，'
        '若存在则返回 true，否则 false。'
        '本实现将矩阵视为长度为 m×n 的升序数组做二分。\n\n'
        '约束：m == matrix.length；n == matrix[i].length；'
        '1 ≤ m, n ≤ 100；-10⁴ ≤ matrix[i][j], target ≤ 10⁴。',
        [
            '示例 1：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 → true。',
            '示例 2：同上，target = 13 → false。',
            '示例 3：matrix = [[1]], target = 1 → true。',
        ],
        [
            '若 matrix 为空返回 False。',
            'left = 0，right = rows * cols - 1，将二维下标映射为一维 mid。',
            'mid 对应 value = matrix[mid // cols][mid % cols]。',
            '二分比较 value 与 target，缩小 left/right；'
            '找到返回 True，否则 False。',
        ],
        '矩阵',
        code_notes=[
            'if not matrix: return False — 空矩阵边界。',
            'rows, cols = len(matrix), len(matrix[0]) — 行列数。',
            'left, right = 0, rows * cols - 1 — 一维化二分区间。',
            'mid // cols, mid % cols — 一维 mid 转二维 (row, col)。',
            'value = matrix[mid // cols][mid % cols] — 取 mid 处元素。',
            'while left <= right — 标准二分；value == target 则 True。',
            '与 240「搜索二维矩阵 II」不同，本题整体有序可一维二分。',
        ],
        complexity='时间 O(log(m×n))，空间 O(1)。',
    ),
    'data_structures/tree/tree.py::same_tree': _m(
        '100', '相同的树',
        '给你两棵二叉树的根节点 p 和 q，'
        '编写一个函数检验这两棵树是否相同。\n\n'
        '两棵树相同当且仅当结构相同且对应节点值相等。'
        '本实现递归比较根、左子树与右子树。\n\n'
        '约束：两棵树节点数 0 ≤ n ≤ 100；-10⁴ ≤ Node.val ≤ 10⁴。',
        [
            '示例 1：p = [1,2,3], q = [1,2,3] → true。',
            '示例 2：p = [1,2], q = [1,null,2] → false。'
            '结构不同。',
            '示例 3：p = [1,2,1], q = [1,1,2] → false。'
            '值不同。',
        ],
        [
            '若 p、q 均为 None 则相同，返回 True。',
            '若仅一方为 None 或 p.val != q.val 则不同，返回 False。',
            '递归 return same_tree(p.left, q.left) and same_tree(p.right, q.right)。',
        ],
        '二叉树',
        code_notes=[
            'if not p and not q: return True — 双空视为相同。',
            'if not p or not q or p.val != q.val: return False — 结构或值不一致。',
            'return same_tree(p.left, q.left) and same_tree(p.right, q.right) — 左右同步递归。',
            '先序遍历思想：根相等且左右子树分别相同。',
            '也可用 BFS 层序两队列同步比较。',
            '时间复杂度 O(min(n,m))，n、m 为两树节点数。',
        ],
        complexity='时间 O(n)，空间 O(n)（递归栈最坏链状），n 为节点数。',
    ),
    'data_structures/tree/tree.py::max_path_sum_binary_tree': _m(
        '124', '二叉树中的最大路径和',
        '二叉树的路径是从树中任意节点出发、'
        '沿父子边到达任意节点的序列；'
        '路径和为路径上节点值之和。\n\n'
        '路径至少包含一个节点，'
        '且不一定经过根节点。'
        '请返回最大路径和。'
        '本实现 DFS 返回「从当前节点向下延伸的单边最大和」，'
        '同时用 best 记录经过当前节点的「左+根+右」路径。\n\n'
        '约束：树节点数 1 ≤ n ≤ 3×10⁴；-1000 ≤ Node.val ≤ 1000。',
        [
            '示例 1：root = [1,2,3] → 6。'
            '路径 2 → 1 → 3。',
            '示例 2：root = [-10,9,20,null,null,15,7] → 42。'
            '路径 15 → 20 → 7。',
            '示例 3：root = [-3] → -3。',
        ],
        [
            '全局 best 初始 -inf；DFS(node) 返回以 node 为端点的向下最大单边和。',
            '空节点返回 0；left = max(dfs(node.left), 0)，负贡献舍弃。',
            'right 同理；best = max(best, node.val + left + right) 更新「拱形」路径。',
            'return node.val + max(left, right) — 供父节点接单边继续延伸。',
            'dfs(root) 后返回 int(best)。',
        ],
        '二叉树',
        code_notes=[
            'best = float("-inf") — 全局最大路径和，可能全负数。',
            'if not node: return 0 — 空子树贡献 0。',
            'left = max(dfs(node.left), 0) — 负路径不选。',
            'right = max(dfs(node.right), 0) — 同上。',
            'best = max(best, node.val + left + right) — 经过 node 的完整路径（可拐弯）。',
            'return node.val + max(left, right) — 返回给父节点仅能用一边。',
            '路径不能分叉成三边，故向上只传单边 max(left,right)。',
        ],
        complexity='时间 O(n)，空间 O(n) 递归栈，n 为节点数。',
    ),
    'data_structures/tree/tree.py::diameter_of_binary_tree': _m(
        '543', '二叉树的直径',
        '给你一棵二叉树的根节点 root，'
        '返回该树的直径长度。\n\n'
        '二叉树的直径是树中任意两个节点之间最长路径的长度；'
        '路径可能经过也可能不经过根。'
        '本实现用 DFS 求每个节点左右子树高度，'
        '以 left + right 更新经过该节点的最长路径。\n\n'
        '约束：树节点数 1 ≤ n ≤ 10⁴；0 ≤ Node.val ≤ 1000。',
        [
            '示例 1：root = [1,2,3,4,5] → 3。'
            '路径 [4,2,1,3] 或 [5,2,1,3]，边数为 3。',
            '示例 2：root = [1,2] → 1。'
            '路径 [2,1]。',
            '示例 3：root = [1] → 0。'
            '单节点直径为 0。',
        ],
        [
            'best 记录最大直径（边数）；depth(node) 返回以 node 为根的子树高度。',
            '空节点高度 0；递归 left = depth(node.left)，right = depth(node.right)。',
            'best = max(best, left + right) — 经过 node 的路径长度为左右深度之和。',
            'return 1 + max(left, right) — 当前子树高度供父节点使用。',
            'depth(root) 后返回 best。',
        ],
        '二叉树',
        code_notes=[
            'best = 0 — 全局最大直径（边数，非节点数）。',
            'if not node: return 0 — 空子树高度 0。',
            'left = depth(node.left); right = depth(node.right) — 左右子树高度。',
            'best = max(best, left + right) — 经过 node 的最长路径 = 左高 + 右高。',
            'return 1 + max(left, right) — 向上返回子树高度（节点数减 1 即边数）。',
            '后序遍历：先算子树高度再更新直径。',
            '与 max_path_sum 类似，best 在 DFS 中顺带维护。',
        ],
        complexity='时间 O(n)，空间 O(n) 递归栈，n 为节点数。',
    ),
    'paradigms/dynamic_programming/sequence_dp.py::length_of_lis': _m(
        '300', '最长递增子序列',
        '给你一个整数数组 nums，'
        '找到其中最长严格递增子序列的长度。\n\n'
        '子序列由数组派生而来，'
        '删除（或不删除）若干元素不改变相对顺序。'
        '本实现采用「 patience sorting / 牌堆」+ 二分：'
        'piles[i] 为长度为 i+1 的递增子序列的最小末尾元素。\n\n'
        '约束：1 ≤ nums.length ≤ 2500；-10⁴ ≤ nums[i] ≤ 10⁴。',
        [
            '示例 1：nums = [10, 9, 2, 5, 3, 7, 101, 18] → 4。'
            '最长递增子序列 [2, 3, 7, 101]。',
            '示例 2：nums = [0, 1, 0, 3, 2, 3] → 4。',
            '示例 3：nums = [7, 7, 7, 7] → 1。'
            '要求严格递增。',
        ],
        [
            '维护 piles 数组，表示各长度 LIS 的最小可能末尾。',
            '对每个 num 在 piles 上二分找第一个 piles[mid] >= num 的位置 lo。',
            '若 lo == len(piles) 则 append(num)（LIS 变长）；否则 piles[lo] = num 替换。',
            '返回 len(piles) 即为 LIS 长度。',
        ],
        '动态规划',
        code_notes=[
            'piles: list[int] — piles[k] 为长度 k+1 的 LIS 的最小末尾，保持 piles 递增。',
            'lo, hi = 0, len(piles); while lo < hi — 二分找第一个 >= num 的位置。',
            'if piles[mid] < num: lo = mid + 1 else hi = mid — lower_bound 变体。',
            'if lo == len(piles): piles.append(num) — 无法替换则延长 LIS。',
            'else: piles[lo] = num — 替换使该长度末尾更小，利于后续延伸。',
            'O(n log n) 优于 DP O(n²)；piles 长度即为答案。',
            '严格递增用 >=；非严格递增改为 >。',
        ],
        complexity='时间 O(n log n)，空间 O(n)，n = len(nums)。',
    ),
    'data_structures/stack_queue/stack_queue.py::LRUCache.__init__': _m(
        '146', 'LRU 缓存-初始化',
        '设计并实现 LRU（最近最少使用）缓存。'
        '应支持 get 和 put 操作，'
        '均在 O(1) 时间内完成。\n\n'
        'LRUCache(capacity) 以正整数 capacity 初始化缓存；'
        'get(key) 返回键值或 -1；'
        'put(key, value) 插入或更新。'
        '超出容量时淘汰最久未使用的项。\n\n'
        '约束：1 ≤ capacity ≤ 3000；0 ≤ key, value ≤ 10⁴；'
        '最多 2×10⁵ 次 get/put。',
        [
            '示例：cache = LRUCache(2) 后 capacity = 2，cache 为空 OrderedDict。',
            '示例：put(1,1), put(2,2), get(1) → 1；put(3,3) 淘汰 key 2。',
            '示例：get(2) → -1（已被淘汰）。',
        ],
        [
            '保存 self.capacity 为最大容量。',
            'self.cache 使用 collections.OrderedDict 同时维护键值与访问顺序。',
            '最近使用的键在 OrderedDict 末尾，最久未使用在开头。',
        ],
        '栈与队列',
        code_notes=[
            'self.capacity = capacity — 缓存上限，put 超限时淘汰。',
            'self.cache: OrderedDict[int, int] — 键到值的映射，顺序表示使用时间。',
            'OrderedDict 支持 move_to_end 与 popitem(last=False) O(1)。',
            '末尾 = 最近使用（MRU），开头 = 最久未使用（LRU）。',
            '与哈希表 + 双向链表等价，Python 内置 OrderedDict 更简洁。',
        ],
        complexity='时间 O(1)，空间 O(capacity)。',
    ),
    'data_structures/stack_queue/stack_queue.py::LRUCache.get': _m(
        '146', 'LRU 缓存-获取',
        '返回 key 对应的 value；'
        '若 key 不存在则返回 -1。'
        '每次成功 get 须将 key 标记为最近使用（移到 OrderedDict 末尾）。\n\n'
        '约束：get 操作 O(1)；0 ≤ key ≤ 10⁴。',
        [
            '示例：LRUCache(2); put(1,1); put(2,2); get(1) → 1。',
            '示例：get(3) → -1。'
            'key 不存在。',
            '示例：get(2) → 2；随后 put(3,3) 淘汰 key 1 而非 2（2 刚被访问）。',
        ],
        [
            '若 key not in self.cache，返回 -1。',
            '否则 self.cache.move_to_end(key) 标记为最近使用。',
            '返回 self.cache[key]。',
        ],
        '栈与队列',
        code_notes=[
            'if key not in self.cache: return -1 — 未命中。',
            'self.cache.move_to_end(key) — 访问后移到末尾，成为 MRU。',
            'return self.cache[key] — O(1) 取值。',
            'get 不改变 cache 大小，仅调整顺序。',
            'move_to_end 是 LRU 策略的核心操作之一。',
            'LeetCode 146 设计题接口之一。',
        ],
        complexity='时间 O(1)。',
    ),
    'data_structures/stack_queue/stack_queue.py::LRUCache.put': _m(
        '146', 'LRU 缓存-写入',
        '插入或更新键 key 的值为 value。'
        '若 key 已存在则更新 value 并标记为最近使用。'
        '若插入后 size > capacity，'
        '淘汰 OrderedDict 开头（最久未使用）的项。\n\n'
        '约束：put 操作 O(1)；1 ≤ capacity ≤ 3000。',
        [
            '示例：cache = LRUCache(2); put(1,1); put(2,2); put(1,1) 更新 1 为 MRU。',
            '示例：put(3,3) 后 cache 为 {2:2, 3:3}，淘汰 key 1。',
            '示例：put(4,4) 淘汰 key 2，cache 为 {3:3, 4:4}。',
        ],
        [
            '若 key 已在 cache 中，先 move_to_end(key) 标记最近使用。',
            '设置 self.cache[key] = value（新建或更新）。',
            '若 len(self.cache) > self.capacity，'
            'popitem(last=False) 移除最久未使用的首项。',
        ],
        '栈与队列',
        code_notes=[
            'if key in self.cache: self.cache.move_to_end(key) — 更新前先标记 MRU。',
            'self.cache[key] = value — 插入或覆盖值。',
            'if len(self.cache) > self.capacity — 超出容量触发淘汰。',
            'self.cache.popitem(last=False) — 弹出 LRU（OrderedDict 开头）。',
            'last=False 弹最左（最旧），last=True 弹最右（最新，本题不用）。',
            'put 与 get 均须维护顺序，保证 O(1) LRU 语义。',
            'capacity 至少为 1，不会出现 put 后空 cache 仍超限。',
        ],
        complexity='时间 O(1)。',
    ),
}
