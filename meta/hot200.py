"""Hot 200 新增题目的元数据。"""
from meta.helpers import _m

PROBLEMS = {
    'patterns/binary_search/basic.py::search_insert_position': _m(
        '35', '搜索插入位置',
        '给定一个按升序排列的整数数组 nums 和一个目标值 target，'
        '在数组中找到 target，若不存在则返回按升序插入的位置。\n\n'
        '你必须在 O(log n) 时间复杂度内完成，'
        '等价于在有序数组中找第一个 ≥ target 的下标。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁴；-10⁴ ≤ nums[i], target ≤ 10⁴；'
        'nums 为严格递增（无重复元素）。',
        [
            '示例 1：nums = [1, 3, 5, 6], target = 5 → 2。'
            '5 存在于下标 2。',
            '示例 2：nums = [1, 3, 5, 6], target = 2 → 1。'
            '2 应插入下标 1，数组变为 [1, 2, 3, 5, 6]。',
            '示例 3：nums = [1, 3, 5, 6], target = 7 → 4。'
            '7 应插入末尾。',
        ],
        [
            '初始化 lo = 0、hi = len(nums)，左闭右开区间 [lo, hi)。',
            'while lo < hi：取 mid = (lo + hi) // 2。',
            '若 nums[mid] < target，说明插入点在 mid 右侧，lo = mid + 1。',
            '否则 nums[mid] ≥ target，插入点可能在 mid 或左侧，hi = mid。',
            '循环结束 lo == hi，即为插入位置，返回 lo。',
        ],
        '二分查找',
        code_notes=[
            'lo, hi = 0, len(nums) — 左闭右开，hi 可取 len(nums) 表示末尾插入。',
            'while lo < hi — 标准二分终止条件，收敛到唯一位置。',
            'mid = (lo + hi) // 2 — 防溢写法与本题等价。',
            'if nums[mid] < target: lo = mid + 1 — target 在右半区。',
            'else: hi = mid — 第一个 ≥ target 的下标留在左半区。',
            'return lo — 无论 target 是否存在，lo 均为插入位置。',
            '与 lower_bound 语义一致；若允许重复元素需调整相等时的分支。',
        ],
        complexity='时间 O(log n)，空间 O(1)，n = len(nums)。',
    ),
    'data_structures/array/basic.py::first_missing_positive': _m(
        '41', '缺失的第一个正数',
        '给你一个未排序的整数数组 nums，'
        '请你找出其中没有出现的最小的正整数。\n\n'
        '要求时间 O(n)、空间 O(1)，'
        '核心思路是将每个正整数 num 交换到下标 num - 1 处，'
        '使数组成为「值等于下标 + 1」的哈希表。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁵；-2³¹ ≤ nums[i] ≤ 2³¹ - 1。',
        [
            '示例 1：nums = [1, 2, 0] → 3。'
            '缺失的最小正整数为 3。',
            '示例 2：nums = [3, 4, -1, 1] → 2。',
            '1 在但 2 缺失。',
            '示例 3：nums = [7, 8, 9, 11, 12] → 1。'
            '1 未出现。',
        ],
        [
            '遍历下标 i，while 循环将 nums[i] 交换到正确位置。',
            '交换条件：1 ≤ nums[i] ≤ n 且 nums[nums[i]-1] != nums[i]（避免死循环）。',
            'j = nums[i] - 1，交换 nums[i] 与 nums[j]。',
            '全部交换完成后，扫描 i：若 nums[i] != i + 1，返回 i + 1。',
            '若 1..n 均存在，返回 n + 1。',
        ],
        '数组',
        code_notes=[
            'n = len(nums) — 答案必在 [1, n+1] 范围内。',
            'while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i] — 原地哈希交换条件。',
            'j = nums[i] - 1; nums[i], nums[j] = nums[j], nums[i] — 值 v 放到下标 v-1。',
            'nums[nums[i]-1] != nums[i] — 已有正确值或重复值时停止交换。',
            'for i in range(n): if nums[i] != i + 1: return i + 1 — 找第一个错位。',
            'return n + 1 — 1..n 齐全时最小缺失为 n+1。',
            '修改原数组，O(1) 额外空间；负数和超范围值会被忽略。',
        ],
        complexity='时间 O(n)，空间 O(1)，每个元素最多交换一次到正确位置。',
    ),
    'data_structures/array/basic.py::rotate_array': _m(
        '189', '轮转数组',
        '给定一个整数数组 nums，'
        '将数组中的元素向右轮转 k 个位置，'
        '其中 k 是非负数。\n\n'
        '本实现采用三次反转：'
        '整体反转 → 反转前 k 个 → 反转后 n-k 个，'
        '原地完成，无需额外数组。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁵；0 ≤ nums[i] ≤ 10⁹；0 ≤ k ≤ 10⁵。',
        [
            '示例 1：nums = [1, 2, 3, 4, 5, 6, 7], k = 3 → [5, 6, 7, 1, 2, 3, 4]。'
            '向右轮转 3 步。',
            '示例 2：nums = [-1, -100, 3, 99], k = 2 → [3, 99, -1, -100]。',
            '示例 3：nums = [1, 2], k = 3 → [2, 1]。'
            'k 对长度取模后为 1。',
        ],
        [
            'k %= len(nums)，k 为 0 时三次反转等价于不变。',
            '定义 reverse(lo, hi) 双指针交换区间 [lo, hi]。',
            'reverse(0, n-1) 整体反转。',
            'reverse(0, k-1) 将后 k 个元素（原末尾）翻到前面。',
            'reverse(k, n-1) 恢复前 n-k 个元素的相对顺序。',
        ],
        '数组',
        code_notes=[
            'def reverse(lo, hi) — 局部双指针 swap，while lo < hi。',
            'k %= len(nums) — 轮转 len 次等于不变，避免无效操作。',
            'reverse(0, len(nums)-1) — 第一步：整段倒序。',
            'reverse(0, k-1) — 第二步：前 k 段再倒序，得到原末尾 k 元。',
            'reverse(k, len(nums)-1) — 第三步：后 n-k 段倒序，恢复原相对顺序。',
            '三次反转等价于 cyclic replace；无额外 O(n) 数组。',
            'nums 原地修改，无返回值（LeetCode 要求 void）。',
        ],
        complexity='时间 O(n)，空间 O(1)，n = len(nums)。',
    ),
    'data_structures/array/basic.py::find_duplicate': _m(
        '287', '寻找重复数',
        '给定一个包含 n + 1 个整数的数组 nums，'
        '其数字都在 [1, n] 范围内，'
        '且只有一个重复数字（可重复多次），'
        '请找出这个重复的数字。\n\n'
        '要求不修改数组、O(1) 额外空间；'
        '本实现将数组视为链表 next(i) = nums[i]，'
        '用 Floyd 快慢指针找环入口即为重复值。\n\n'
        '约束：1 ≤ n ≤ 10⁵；nums.length == n + 1；1 ≤ nums[i] ≤ n。',
        [
            '示例 1：nums = [1, 3, 4, 2, 2] → 2。',
            '示例 2：nums = [3, 1, 3, 4, 2] → 3。',
            '示例 3：nums = [1, 1] → 1。'
            '仅两个元素。',
        ],
        [
            '将 nums 看作隐式链表：从 index 0 出发，next = nums[i]。',
            '第一阶段：slow 走一步，fast 走两步，直至 slow == fast 相遇。',
            '第二阶段：slow 重置为 nums[0]，与 fast 同步各走一步。',
            '再次相遇处即为环入口，对应重复数字，返回 slow。',
        ],
        '数组',
        code_notes=[
            'slow = fast = nums[0] — 从链表头（下标 0 的值）出发。',
            'slow = nums[slow] — 慢指针走一步。',
            'fast = nums[nums[fast]] — 快指针走两步。',
            'if slow == fast: break — 第一阶段找环内相遇点。',
            'slow = nums[0] — 第二阶段 slow 回起点。',
            'while slow != fast: 同步 nums[步进] — 相遇点为环入口。',
            'return slow — 环入口值即重复数；不修改 nums，O(1) 空间。',
        ],
        complexity='时间 O(n)，空间 O(1)，Floyd 判圈算法。',
    ),
    'data_structures/array/basic.py::pascal_triangle': _m(
        '118', '杨辉三角',
        '给定 numRows，'
        '生成杨辉三角的前 numRows 行。\n\n'
        '杨辉三角每行首尾为 1，'
        '其余每个数等于上一行左上方与正上方之和。\n\n'
        '约束：1 ≤ numRows ≤ 30。',
        [
            '示例 1：numRows = 5 → [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]。',
            '示例 2：numRows = 1 → [[1]]。',
            '示例 3：numRows = 3 → [[1],[1,1],[1,2,1]]。',
        ],
        [
            '初始化 result 为空列表，逐行构建。',
            '第 i 行（0-indexed）先创建长度为 i+1、全 1 的 row。',
            '对 j 从 1 到 i-1：row[j] = result[i-1][j-1] + result[i-1][j]。',
            '将 row 追加到 result。',
            '循环 i = 0..numRows-1 后返回 result。',
        ],
        '数组',
        code_notes=[
            'result: list[list[int]] = [] — 逐行累积结果。',
            'row = [1] * (i + 1) — 每行首尾默认为 1。',
            'for j in range(1, i) — 中间元素由上一行相邻两数求和。',
            'row[j] = result[i-1][j-1] + result[i-1][j] — 杨辉递推公式。',
            'result.append(row) — 当前行完成后再加入总结果。',
            'i=0 时内层 j 循环为空，正确得到 [1]。',
            '空间可优化为只保留上一行，本题返回完整三角。',
        ],
        complexity='时间 O(numRows²)，空间 O(numRows²)（输出占主导）。',
    ),
    'data_structures/array/basic.py::my_pow': _m(
        '50', 'Pow(x, n)',
        '实现 pow(x, n)，'
        '即计算 x 的整数 n 次幂。\n\n'
        '本实现采用快速幂（二进制幂）：'
        '将 n 按位分解，'
        '平方底数并累乘对应位为 1 的因子，'
        '时间 O(log |n|)。\n\n'
        '约束：-100.0 < x < 100.0；-2³¹ ≤ n ≤ 2³¹ - 1；'
        'n 为整数；结果在有效范围内。',
        [
            '示例 1：x = 2.0, n = 10 → 1024.0。',
            '示例 2：x = 2.1, n = 3 → 9.261。',
            '示例 3：x = 2.0, n = -2 → 0.25。'
            '负指数取倒数。',
        ],
        [
            '若 n < 0，将 x 变为 1/x，n 取 -n 转为正指数。',
            '初始化 result = 1.0，底数 x 随位迭代平方。',
            'while n > 0：若 n 最低位为 1（n & 1），result *= x。',
            'x *= x 底数平方；n >>= 1 右移处理下一位。',
            '循环结束返回 result。',
        ],
        '数学',
        code_notes=[
            'if n < 0: x, n = 1 / x, -n — 负指数转倒数。',
            'result = 1.0 — 累乘因子初始为 1。',
            'while n: — 二进制快速幂主循环。',
            'if n & 1: result *= x — 当前最低位为 1 时乘入底数。',
            'x *= x — 底数自乘，对应指数位左移。',
            'n >>= 1 — 指数右移一位，O(log n) 轮。',
            '也可递归实现 x^n = x^(n/2) * x^(n/2)（n 偶）或 x * x^(n-1)（n 奇）。',
        ],
        complexity='时间 O(log |n|)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::copy_random_list': _m(
        '138', '复制带随机指针的链表',
        '给定一个链表，'
        '每个节点包含一个额外增加的随机指针 random，'
        '该指针可以指向链表中的任意节点或 null。\n\n'
        '请深拷贝该链表，'
        '返回复制链表的头节点。\n\n'
        '本实现采用「交错插入」三步法：'
        '复制节点插入原节点后 → 设置 random → 拆分两条链，'
        'O(n) 时间 O(1) 额外空间（不含输出）。\n\n'
        '约束：节点数 0 ≤ n ≤ 1000；-10⁴ ≤ Node.val ≤ 10⁴；'
        'random 为 null 或指向链表内节点。',
        [
            '示例 1：head = [[7,null],[13,0],[11,4],[10,2],[1,0]] → 结构相同的深拷贝。',
            '示例 2：head = [[1,1],[2,1]] → 两节点互指 random。',
            '示例 3：head = [] → null。'
            '空链表返回 null。',
        ],
        [
            '若 head 为空返回 None。',
            '第一遍：遍历原链，在每个 cur 后插入 copy = RandomListNode(cur.val)，'
            'cur.next 指向 copy，copy.next 指向原 next。',
            '第二遍：若 cur.random 存在，cur.next.random = cur.random.next（克隆节点）。',
            '第三遍：用 dummy 头节点拆分：原链 cur.next = clone.next，'
            '新链 prev.next = clone，交替推进。',
            '返回 dummy.next 作为克隆链表头。',
        ],
        '链表',
        code_notes=[
            'copy = RandomListNode(cur.val, cur.next) — 创建值相同的克隆节点。',
            'cur.next = copy; cur = copy.next — 交错插入，原节点与克隆相邻。',
            'cur.next.random = cur.random.next — 原 random 的下一个即其克隆。',
            'dummy = RandomListNode() — 虚拟头简化新链构建。',
            'clone = cur.next; cur.next = clone.next — 恢复原链 next 指针。',
            'prev.next = clone; prev = clone — 串联克隆链。',
            '哈希表 O(n) 空间亦可：map[原节点]=克隆节点，代码更直观。',
        ],
        complexity='时间 O(n)，空间 O(1) 额外（不含输出链表），n 为节点数。',
    ),
    'data_structures/linked_list/linked_list.py::sort_list': _m(
        '148', '排序链表',
        '给你链表的头节点 head，'
        '请将其按升序排列并返回排序后的链表。\n\n'
        '要求 O(n log n) 时间、O(1) 空间（递归栈除外），'
        '本实现采用归并排序：'
        '快慢指针找中点 → 递归排序两半 → 双指针合并。\n\n'
        '约束：节点数 0 ≤ n ≤ 5×10⁴；-10⁵ ≤ Node.val ≤ 10⁵。',
        [
            '示例 1：head = [4, 2, 1, 3] → [1, 2, 3, 4]。',
            '示例 2：head = [-1, 5, 3, 4, 0] → [-1, 0, 3, 4, 5]。',
            '示例 3：head = [] → []。'
            '空链表。',
        ],
        [
            '边界：head 为空或单节点直接返回 head。',
            '快慢指针 slow/fast 找中点，slow.next 置 None 断开两半。',
            '递归 sort_list(左半) 与 sort_list(右半)。',
            'merge(l1, l2) 用 dummy 节点双路归并较小值。',
            '返回 merge 结果作为已排序链表头。',
        ],
        '链表',
        code_notes=[
            'def merge(l1, l2) — 标准有序链表归并，dummy 虚拟头。',
            'if l1.val <= l2.val — 升序取较小节点接在 cur.next。',
            'cur.next = l1 or l2 — 归并结束后接剩余段。',
            'slow, fast = head, head.next — fast 先走一步，避免中点偏左重复。',
            'while fast and fast.next — 快指针到末尾时 slow 在中点。',
            'mid = slow.next; slow.next = None — 断链，分治递归。',
            'return merge(sort_list(head), sort_list(mid)) — 归并排序核心。',
        ],
        complexity='时间 O(n log n)，空间 O(log n) 递归栈。',
    ),
    'data_structures/linked_list/linked_list.py::is_palindrome_list': _m(
        '234', '回文链表',
        '给你一个单链表的头节点 head，'
        '请判断该链表是否为回文链表。\n\n'
        '本实现 O(n) 时间、O(1) 空间：'
        '快慢指针找中点 → 反转后半段 → 头尾同步比较。\n\n'
        '约束：节点数 1 ≤ n ≤ 10⁵；0 ≤ Node.val ≤ 9。',
        [
            '示例 1：head = [1, 2, 2, 1] → true。',
            '示例 2：head = [1, 2] → false。',
            '示例 3：head = [1] → true。'
            '单节点为回文。',
        ],
        [
            '空链或单节点直接返回 True。',
            'slow/fast 找中点：slow 走一步，fast 走两步。',
            '从 slow 开始反转后半链表（prev 指针迭代）。',
            'left 从头、right 从反转后的后半头同步比较 val。',
            '任一不等返回 False；全部匹配返回 True。',
        ],
        '链表',
        code_notes=[
            'if not head or not head.next: return True — 0/1 节点边界。',
            'slow = slow.next; fast = fast.next.next — 快慢指针，slow 最终在中点或偏左。',
            'nxt = slow.next; slow.next = prev — 原地反转后半段。',
            'prev = slow — 反转后 prev 为后半段头（右端指针）。',
            'left, right = head, prev — 双指针从两端向中间比较。',
            'while right: 比较 left.val 与 right.val — 仅遍历后半长度。',
            '修改了链表 next 结构；若需保持原链可再反转恢复。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/tree/tree.py::zigzag_level_order': _m(
        '103', '二叉树的锯齿形层序遍历',
        '给你二叉树的根节点 root，'
        '返回其节点值的锯齿形层序遍历。'
        '即奇数层从左到右，偶数层从右到左。\n\n'
        '约束：节点数 0 ≤ n ≤ 2000；-1000 ≤ Node.val ≤ 1000。',
        [
            '示例 1：root = [3,9,20,null,null,15,7] → [[3],[20,9],[15,7]]。',
            '示例 2：root = [1] → [[1]]。',
            '示例 3：root = [] → []。'
            '空树返回空列表。',
        ],
        [
            '若 root 为空返回 []。',
            'BFS 队列初始化 [root]，left_to_right = True 标记当前层方向。',
            '每层处理 len(queue) 个节点，收集 level 值并扩展子节点入队。',
            '若 left_to_right 为 False，将 level 反转后追加到 result。',
            '翻转方向标志 left_to_right = not left_to_right，继续下一层。',
            '返回 result。',
        ],
        '树',
        code_notes=[
            'queue = deque([root]) — 标准层序 BFS 队列。',
            'left_to_right = True — 方向标志，奇数层从左到右。',
            'for _ in range(len(queue)) — 按层批量处理，固定当前层大小。',
            'node = queue.popleft(); level.append(node.val) — 出队并记录。',
            'if node.left/right: queue.append — 子节点入队，下轮处理。',
            'result.append(level if left_to_right else level[::-1]) — 偶数层反转。',
            'left_to_right = not left_to_right — 每层切换方向。',
            '也可在 deque 头尾交替 append 实现，本代码逻辑更清晰。',
        ],
        complexity='时间 O(n)，空间 O(n)，n 为节点数（队列与结果）。',
    ),
    'data_structures/tree/tree.py::flatten': _m(
        '114', '二叉树展开为链表',
        '给你二叉树的根节点 root，'
        '将其展开为单链表：'
        '展开后的链表同样使用 TreeNode，'
        'right 子指针指向下一个节点，left 始终为 null，'
        '顺序与先序遍历一致。\n\n'
        '请原地修改，不返回新结构。\n\n'
        '约束：节点数 0 ≤ n ≤ 2000；-100 ≤ Node.val ≤ 100。',
        [
            '示例 1：root = [1,2,5,3,4,null,6] → [1,null,2,null,3,null,4,null,5,null,6]。'
            '先序展开。',
            '示例 2：root = [] → []。',
            '示例 3：root = [1,2] → [1,null,2]。',
        ],
        [
            'cur 从 root 出发，沿 right 指针遍历目标链表。',
            '若 cur.left 存在：找到左子树最右节点 tail。',
            'tail.right = cur.right — 原右子树接到左子树最右后。',
            'cur.right = cur.left; cur.left = None — 左子树移到右侧。',
            'cur = cur.right 继续处理下一节点。',
        ],
        '树',
        code_notes=[
            'cur = root — 头插法式展开，逐节点处理。',
            'if cur.left: — 有左子树才需重连。',
            'tail = cur.left; while tail.right: tail = tail.right — 找左子树最右。',
            'tail.right = cur.right — 原右子树挂到最右节点后。',
            'cur.right = cur.left; cur.left = None — 左变右，左清空。',
            'cur = cur.right — 沿展开后的 next 前进。',
            'O(1) 额外空间；反序先序+头插亦可实现。',
        ],
        complexity='时间 O(n)，空间 O(1)，每个节点最多被 tail 遍历一次。',
    ),
    'data_structures/tree/tree.py::rob_tree': _m(
        '337', '打家劫舍 III',
        '小偷又发现新的可行窃地区，'
        '这一地区只有一个入口，'
        '入口之外的所有房间组成一棵二叉树。'
        '每个房间存有一定现金，'
        '相邻房间（父子节点）不能同时被偷。\n\n'
        '给定二叉树根节点 root，'
        '返回能偷到的最高金额。\n\n'
        '约束：节点数 1 ≤ n ≤ 10⁴；0 ≤ Node.val ≤ 10⁴。',
        [
            '示例 1：root = [3,2,3,null,3,null,1] → 7。'
            '偷 3+3+1=7（根、右子、右孙）。',
            '示例 2：root = [3,4,5,1,3,null,1] → 9。'
            '偷 4+5=9。',
            '示例 3：root = [1] → 1。',
        ],
        [
            'DFS 返回 (rob, skip) 二元组：'
            'rob 为偷当前节点的最大收益，skip 为不偷当前节点的最大收益。',
            '空节点返回 (0, 0)。',
            '递归左右子树得 left_rob/skip、right_rob/skip。',
            'rob = node.val + left_skip + right_skip — 偷当前则子必不偷。',
            'skip = max(left_rob, left_skip) + max(right_rob, right_skip)。',
            '返回 max(dfs(root))。',
        ],
        '树',
        code_notes=[
            'def dfs(node) -> tuple[int, int] — 后序 DFS，自底向上。',
            'if not node: return 0, 0 — 空子树贡献为零。',
            'left_rob, left_skip = dfs(node.left) — 左子树两种状态。',
            'rob = node.val + left_skip + right_skip — 偷父则子不能偷。',
            'skip = max(left_rob, left_skip) + max(right_rob, right_skip) — 不偷父取子最优组合。',
            'return rob, skip — 向上传递状态。',
            'return max(dfs(root)) — 根可偷可不偷，取较大。',
            '与打家劫舍 I/II 同 DP 思想，树形结构用递归后序实现。',
        ],
        complexity='时间 O(n)，空间 O(h) 递归栈，h 为树高。',
    ),
    'data_structures/tree/tree.py::Codec.serialize': _m(
        '297', '二叉树的序列化-序列化',
        '请设计一个算法来实现二叉树的序列化与反序列化。'
        '本题实现 Codec 类的 serialize 方法：'
        '将二叉树编码为字符串；'
        'deserialize 将字符串解码还原树。\n\n'
        'serialize 采用先序 DFS，'
        '空节点用 "#" 占位，'
        '节点值与占位符用逗号连接。\n\n'
        '约束：树节点数 0 ≤ n ≤ 10⁴；'
        '1 ≤ Node.val ≤ 10⁹；serialize 与 deserialize 成对调用。',
        [
            '示例 1：root = [1,2,3,null,null,4,5] → "1,2,#,#,3,4,#,#,5,#,#"。',
            '示例 2：root = [] → ""。'
            '空树序列化为空字符串。',
            '示例 3：root = [1] → "1,#,#"。'
            '单节点带左右空占位。',
        ],
        [
            '若 root 为 None 返回空字符串 ""。',
            '维护 parts 列表收集先序 token。',
            'DFS：空节点 append "#" 并返回。',
            '非空节点 append str(node.val)，再递归 left、right。',
            'return ",".join(parts) 得到逗号分隔序列。',
        ],
        '树',
        code_notes=[
            'parts: list[str] = [] — 先序 token 收集器。',
            'def dfs(node) — 嵌套递归，先序遍历。',
            'if not node: parts.append("#"); return — 空子树占位符。',
            'parts.append(str(node.val)) — 根值在前。',
            'dfs(node.left); dfs(node.right) — 左子树先于右子树。',
            'return ",".join(parts) — 逗号分隔便于 split 解析。',
            'deserialize 用 iter + 递归 build() 按相同先序顺序还原。',
            '"#" 必须显式编码空指针，否则无法区分缺失子树。',
        ],
        complexity='时间 O(n)，空间 O(n)，n 为节点数（含空占位 token）。',
    ),
    'data_structures/tree/tree.py::Codec.deserialize': _m(
        '297', '二叉树的序列化-反序列化',
        'Codec.deserialize(data) 将 serialize 产生的字符串'
        '还原为原始二叉树结构。\n\n'
        '本实现按先序顺序用迭代器逐个读取 token：'
        '遇 "#" 返回 None，'
        '否则创建节点并递归构建左右子树。\n\n'
        '约束：data 为合法 serialize 输出；'
        '空字符串对应空树。',
        [
            '示例 1：data = "1,2,#,#,3,4,#,#,5,#,#" → [1,2,3,null,null,4,5]。',
            '示例 2：data = "" → null。',
            '示例 3：data = "1,#,#" → [1]。'
            '单节点树。',
        ],
        [
            '若 data 为空字符串返回 None。',
            'tokens = iter(data.split(",")) 创建迭代器。',
            'def build()：取 next(tokens) 为 val。',
            'val == "#" 时返回 None。',
            '否则 TreeNode(int(val))，递归 node.left = build()、node.right = build()。',
            'return build() 作为还原后的根节点。',
        ],
        '树',
        code_notes=[
            'if not data: return None — 空串对应空树。',
            'tokens = iter(data.split(",")) — 全局迭代器保证先序消费顺序。',
            'val = next(tokens) — 每次 build 取一个 token。',
            'if val == "#": return None — 空指针占位。',
            'node = TreeNode(int(val)) — 创建当前节点。',
            'node.left = build(); node.right = build() — 先序：根-左-右。',
            'return build() — 从根开始重建整棵树。',
            '与 serialize 的先序 "#" 编码严格对应，成对使用。',
        ],
        complexity='时间 O(n)，空间 O(n) 递归栈与 token 列表。',
    ),
    'paradigms/dynamic_programming/linear_dp.py::house_robber_ii': _m(
        '213', '打家劫舍 II',
        '你是一个专业的小偷，'
        '计划偷窃沿街的房屋，'
        '每间房内都藏有一定现金。'
        '相邻房屋装有防盗系统，'
        '首尾房屋也视为相邻（环形）。\n\n'
        '给定非负整数数组 nums，'
        '计算在不触动报警的情况下一夜能偷到的最高金额。\n\n'
        '约束：1 ≤ nums.length ≤ 100；0 ≤ nums[i] ≤ 1000。',
        [
            '示例 1：nums = [2, 3, 2] → 3。'
            '不能偷 2+2（首尾相邻），偷中间 3。',
            '示例 2：nums = [1, 2, 3, 1] → 4。'
            '偷 1+3=4。',
            '示例 3：nums = [1, 2, 3] → 3。'
            '偷 3 或 1+2 均为 3。',
        ],
        [
            '单元素直接返回 nums[0]。',
            '环形拆为两个线性区间：[0, n-2] 与 [1, n-1]，'
            '分别代表「不偷尾」与「不偷头」。',
            'rob_range(start, end) 用双变量滚动 DP 求区间最大收益。',
            'return max(rob_range(0, n-2), rob_range(1, n-1))。',
        ],
        '动态规划',
        code_notes=[
            'if len(nums) == 1: return nums[0] — 单房屋无环歧义。',
            'def rob_range(start, end) — 198 题打家劫舍线性版。',
            'prev, cur = 0, 0 — 滚动变量，prev=dp[i-2], cur=dp[i-1]。',
            'for i in range(start, end): prev, cur = cur, max(cur, prev + nums[i])。',
            'return cur — 区间最优解。',
            'max(rob_range(0, len-2), rob_range(1, len-1)) — 环拆两段取 max。',
            '首屋与尾屋不能同偷，故两段分别排除一端。',
        ],
        complexity='时间 O(n)，空间 O(1)，n = len(nums)。',
    ),
    'patterns/graph/graph.py::course_schedule_ii': _m(
        '210', '课程表 II',
        '你这个学期必须选修 numCourses 门课，'
        '编号 0 到 numCourses - 1。'
        'prerequisites[i] = [a, b] 表示选 a 前必须先选 b。\n\n'
        '返回完成所有课程的学习顺序；'
        '若不可能（有环）返回空数组。\n\n'
        '本实现 Kahn 拓扑排序 BFS。\n\n'
        '约束：1 ≤ numCourses ≤ 2000；0 ≤ prerequisites.length ≤ numCourses×(numCourses-1)/2。',
        [
            '示例 1：numCourses = 2, prerequisites = [[1,0]] → [0,1]。'
            '先修 0 再 1。',
            '示例 2：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]] → [0,1,2,3] 或 [0,2,1,3]。',
            '示例 3：numCourses = 1, prerequisites = [] → [0]。'
            '无先修要求。',
        ],
        [
            '建图 graph[prereq].append(course)，统计 indegree。',
            '将 indegree 为 0 的节点入队。',
            'BFS：出队 node 加入 order，对其后继 nxt  indegree -= 1。',
            '若 indegree[nxt] == 0 则入队。',
            'BFS 结束：若 len(order) == numCourses 返回 order，否则返回 []（有环）。',
        ],
        '图论',
        code_notes=[
            'graph: dict[int, list[int]] — prereq → course 有向边。',
            'indegree[course] += 1 — 每门课的先修计数。',
            'queue = deque(i for i in range(numCourses) if indegree[i] == 0) — 无先修课。',
            'order.append(node) — 拓扑序输出。',
            'indegree[nxt] -= 1; if indegree[nxt] == 0: queue.append(nxt) — 解锁后续课。',
            'return order if len(order) == numCourses else [] — 未全部出队则有环。',
            '与 207 课程表判定环相比，本题需输出具体顺序。',
        ],
        complexity='时间 O(V + E)，空间 O(V + E)，V = numCourses。',
    ),
    'data_structures/stack_queue/stack_queue.py::min_meeting_rooms': _m(
        '253', '会议室 II',
        '给定一个会议时间间隔数组 intervals，'
        'intervals[i] = [start_i, end_i]，'
        '返回所需会议室的最少数量。\n\n'
        '等价于求同一时刻进行中的会议最大重叠数；'
        '本实现分别排序开始与结束时间，双指针扫描。\n\n'
        '约束：1 ≤ intervals.length ≤ 10⁴；'
        '0 ≤ start_i < end_i ≤ 10⁶。',
        [
            '示例 1：intervals = [[0,30],[5,10],[15,20]] → 2。'
            '0-30 与 5-10、15-20 重叠需 2 间。',
            '示例 2：intervals = [[7,10],[2,4]] → 1。'
            '时间不重叠。',
            '示例 3：intervals = [] → 0。'
            '无会议。',
        ],
        [
            '空 intervals 返回 0。',
            'starts 与 ends 分别按开始、结束时间排序。',
            '双指针 i（开始）、j（结束），rooms 记录当前占用数。',
            '若 starts[i] < ends[j]：新会议开始且前一未结束，rooms += 1，更新 max_rooms。',
            '否则 starts[i] >= ends[j]：释放一间，rooms -= 1，j += 1。',
            '返回 max_rooms。',
        ],
        '堆与队列',
        code_notes=[
            'if not intervals: return 0 — 空输入边界。',
            'starts = sorted(start for start, _ in intervals) — 开始时间升序。',
            'ends = sorted(end for _, end in intervals) — 结束时间升序。',
            'if starts[i] < ends[j] — 新会议开始时上一会议未结束，需新房间。',
            'rooms += 1; max_rooms = max(max_rooms, rooms) — 维护峰值。',
            'else: rooms -= 1; j += 1 — 会议结束释放房间。',
            'i 仅在 starts[i] < ends[j] 时前进 — 扫描所有开始事件。',
            '也可用最小堆维护结束时间，复杂度同为 O(n log n)。',
        ],
        complexity='时间 O(n log n) 排序，空间 O(n)。',
    ),
    'data_structures/stack_queue/stack_queue.py::MedianFinder.__init__': _m(
        '295', '数据流的中位数-初始化',
        '中位数是有序整数列表中中间位置的数。'
        '若列表长度为偶数，'
        '则为中间两数的平均值。\n\n'
        '请实现 MedianFinder 类：'
        '__init__ 初始化；addNum(num) 添加整数；'
        'findMedian() 返回当前中位数。\n\n'
        '本实现用两个堆：'
        'small 存较小一半（大根堆），'
        'large 存较大一半（小根堆）。\n\n'
        '约束：-10⁵ ≤ num ≤ 10⁵；'
        '最多 5×10⁴ 次 addNum 与 findMedian 调用。',
        [
            '示例：finder = MedianFinder() 后 small = []，large = []。',
            '示例：addNum(1) 后 small = [-1]，large = []。',
            '示例：addNum(2) 后 small = [-2], large = [1]（平衡后）。',
        ],
        [
            '创建 MedianFinder 实例。',
            'self.small: list[int] — 较小一半，Python heapq 配合取负模拟大根堆。',
            'self.large: list[int] — 较大一半，标准小根堆。',
            '初始两堆均为空，addNum 时维护大小差不超过 1。',
        ],
        '堆与队列',
        code_notes=[
            'self.small: list[int] = [] — 存较小半，heapq 默认小根，存 -num 模拟大根。',
            'self.large: list[int] = [] — 存较大半，标准 min-heap。',
            '两堆设计使 small 堆顶为较小半最大值，large 堆顶为较大半最小值。',
            '不变量：len(small) >= len(large) 且 len(small) - len(large) <= 1。',
            '与 addNum、findMedian 配合完成 O(log n) 插入与 O(1) 查询。',
            'Python heapq 无 max-heap，-num 取负是常见技巧。',
        ],
        complexity='时间 O(1)，空间 O(1)（不含后续 addNum 数据）。',
    ),
    'data_structures/stack_queue/stack_queue.py::MedianFinder.addNum': _m(
        '295', '数据流的中位数-添加数字',
        '向数据流中添加整数 num。'
        '添加后两堆须保持：'
        'small 存较小一半、large 存较大一半，'
        '且 small 的大小等于 large 或比 large 多 1。\n\n'
        '约束：-10⁵ ≤ num ≤ 10⁵。',
        [
            '示例：addNum(1) → small = [-1]，median 待查为 1。',
            '示例：连续 addNum(1), addNum(2) → small = [-2], large = [1]。',
            '示例：addNum(3) 后 findMedian() → 2.0。',
        ],
        [
            '先将 num 压入 small（大根堆，存 -num）。',
            '将 small 堆顶（当前较小半最大）弹出并压入 large，'
            '保证 large 最小值不小于 small 最大值。',
            '若 large 比 small 多，将 large 堆顶弹回 small 平衡大小。',
            '三步后维持堆大小不变量。',
        ],
        '堆与队列',
        code_notes=[
            'heapq.heappush(self.small, -num) — 先入较小半大根堆。',
            'heapq.heappush(self.large, -heapq.heappop(self.small)) — 较小半最大移到较大半。',
            'if len(self.large) > len(self.small): heapq.heappush(self.small, -heapq.heappop(self.large)) — 平衡。',
            '每步 O(log n)；三步后 len(small) >= len(large)。',
            '先 push small 再调整，简化边界处理。',
            'large 堆顶始终为较大半最小元素，与 small 堆顶相邻。',
            '奇数个元素时 median 为 -small[0]；偶数为两堆顶均值。',
        ],
        complexity='时间 O(log n)，空间 O(1) 均摊（计入堆存储则为 O(总数)）。',
    ),
    'data_structures/stack_queue/stack_queue.py::MedianFinder.findMedian': _m(
        '295', '数据流的中位数-查询中位数',
        '返回数据流当前所有整数的中位数。'
        '若元素个数为奇数，'
        '返回 small 堆顶（较小半的最大值）；'
        '若为偶数，'
        '返回 small 堆顶与 large 堆顶的平均值。\n\n'
        '约束：至少调用一次 addNum 后再调用 findMedian。',
        [
            '示例：addNum(1), findMedian() → 1.0。',
            '示例：addNum(1), addNum(2), findMedian() → 1.5。',
            '示例：addNum(1), addNum(2), addNum(3), findMedian() → 2.0。',
        ],
        [
            '若 len(small) > len(large)，元素总数为奇数。',
            '中位数为 float(-self.small[0])（大根堆存负值）。',
            '否则总数为偶数，中位数为 (-small[0] + large[0]) / 2.0。',
            '返回浮点结果。',
        ],
        '堆与队列',
        code_notes=[
            'if len(self.small) > len(self.large) — 奇数个元素，small 多一个。',
            'return float(-self.small[0]) — small 存负值，取负得较小半最大值即中位数。',
            'return (-self.small[0] + self.large[0]) / 2.0 — 偶数时两堆顶平均。',
            'small[0] 与 large[0] 分别为堆顶，O(1) 访问。',
            'addNum 保证不变量，findMedian 无需额外计算或排序。',
            '返回 float 满足 LeetCode 对偶数平均的要求。',
        ],
        complexity='时间 O(1)，空间 O(1)。',
    ),
    'foundations/bit_manipulation.py::count_bits': _m(
        '338', '比特位计数',
        '给定非负整数 n，'
        '计算 [0, n] 范围内每个数的二进制表示中 1 的个数，'
        '返回长度为 n+1 的数组 ans，'
        'ans[i] 为 i 的二进制 1 的个数。\n\n'
        '约束：0 ≤ n ≤ 10⁵。',
        [
            '示例 1：n = 2 → [0, 1, 1]。'
            '0→0, 1→1, 2→10 有 1 个 1。',
            '示例 2：n = 5 → [0, 1, 1, 2, 1, 2]。',
            '示例 3：n = 0 → [0]。',
        ],
        [
            '初始化 dp = [0] * (n + 1)，dp[0] = 0。',
            '对 i 从 1 到 n：dp[i] = dp[i >> 1] + (i & 1)。',
            'i >> 1 为去掉最低位后的数，其 1 的个数已知。',
            'i & 1 为最低位是否为 1。',
            '返回 dp。',
        ],
        '位运算',
        code_notes=[
            'dp = [0] * (n + 1) — 结果数组，dp[0] = 0 已隐含。',
            'for i in range(1, n + 1) — 从 1 递推到 n。',
            'dp[i] = dp[i >> 1] + (i & 1) — 状态转移：右移一位 + 最低位。',
            'i >> 1 等价于 i // 2，去掉最低二进制位。',
            'i & 1 — 最低位为 1 则加 1，否则加 0。',
            '也可 dp[i] = dp[i & (i-1)] + 1 清除最低 1 后加一。',
            'O(n) 一次遍历，无逐位 while 循环。',
        ],
        complexity='时间 O(n)，空间 O(n)（输出数组）。',
    ),
    'foundations/bit_manipulation.py::hamming_distance': _m(
        '461', '汉明距离',
        '两个整数之间的汉明距离'
        '指的是两个数的二进制对应位不同的位置的数量。\n\n'
        '给定两个整数 x 和 y，'
        '计算并返回它们之间的汉明距离。\n\n'
        '约束：0 ≤ x, y ≤ 2³¹ - 1。',
        [
            '示例 1：x = 1, y = 4 → 2。'
            '1=0001, 4=0100，两位不同。',
            '示例 2：x = 3, y = 1 → 1。'
            '3=11, 1=01。',
            '示例 3：x = 0, y = 0 → 0。',
        ],
        [
            'xor = x ^ y，不同位为 1。',
            '初始化 count = 0。',
            'while xor > 0：xor &= xor - 1 清除最低位的 1，count += 1。',
            '循环次数即为 1 的个数，返回 count。',
        ],
        '位运算',
        code_notes=[
            'xor = x ^ y — 异或后 1 的位即不同位。',
            'count = 0 — 累加器。',
            'while xor: — Brian Kernighan 算法循环。',
            'xor &= xor - 1 — 每次清除 xor 最低位的 1。',
            'count += 1 — 清除次数即汉明距离。',
            '比逐位 (xor >> i) & 1 更高效，循环次数等于 1 的个数。',
            '也可 bin(x ^ y).count("1")，但位运算写法更标准。',
        ],
        complexity='时间 O(k)，k 为 xor 中 1 的个数，最坏 O(32)；空间 O(1)。',
    ),
    'data_structures/hash_map/hash_map.py::find_disappeared_numbers': _m(
        '448', '找到所有数组中消失的数字',
        '给定一个含 n 个整数的数组 nums，'
        '其中 nums[i] 在区间 [1, n] 内，'
        '找出 [1, n] 范围内所有未出现在 nums 中的数字。\n\n'
        '要求 O(n) 时间、O(1) 额外空间；'
        '本实现用下标作哈希，'
        '将对应位置数值取负标记「出现过」。\n\n'
        '约束：n == nums.length；1 ≤ n ≤ 10⁵；1 ≤ nums[i] ≤ n。',
        [
            '示例 1：nums = [4, 3, 2, 7, 8, 2, 3, 1] → [5, 6]。',
            '示例 2：nums = [1, 1] → [2]。',
            '示例 3：nums = [1, 2, 3, 4] → []。'
            '无缺失。',
        ],
        [
            '遍历 num：idx = abs(num) - 1 为应标记的下标。',
            '若 nums[idx] > 0，将其取负表示 idx+1 出现过。',
            '第二遍扫描下标 i：若 nums[i] > 0，说明 i+1 未出现。',
            '收集并返回所有 i+1。',
        ],
        '哈希表',
        code_notes=[
            'idx = abs(num) - 1 — 值 v 对应下标 v-1，abs 因可能已取负。',
            'if nums[idx] > 0: nums[idx] = -nums[idx] — 首次出现则标记为负。',
            '已负则不再翻转，避免误还原。',
            'return [i + 1 for i, num in enumerate(nums) if num > 0] — 仍为正的下标+1 即缺失。',
            '原地修改 nums，O(1) 额外空间。',
            '与 41 题原地哈希思想类似，本题找缺失而非最小缺失。',
        ],
        complexity='时间 O(n)，空间 O(1)（不含输出列表）。',
    ),
    'patterns/monotonic_stack.py::maximal_rectangle': _m(
        '85', '最大矩形',
        '给定一个仅包含 0 和 1 的二维二进制矩阵 matrix，'
        '找出只包含 1 的最大矩形面积，'
        '返回其面积。\n\n'
        '本实现逐行更新柱状图高度 heights，'
        '每行调用 largest_rectangle_area（单调栈）'
        '求最大矩形并取全局 max。\n\n'
        '约束：rows == matrix.length；cols == matrix[i].length；'
        '1 ≤ rows, cols ≤ 200；matrix[i][j] 为 "0" 或 "1"。',
        [
            '示例 1：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]] → 6。'
            '最大矩形 3×2=6。',
            '示例 2：matrix = [["0"]] → 0。',
            '示例 3：matrix = [["1"]] → 1。',
        ],
        [
            '空矩阵返回 0；初始化 heights = [0] * cols。',
            '逐行遍历 matrix：'
            '若 cell 为 "1" 则 heights[j] += 1，否则置 0。',
            '每行更新后 best = max(best, largest_rectangle_area(heights))。',
            'largest_rectangle_area 用单调栈求柱状图最大矩形（LC 84）。',
            '返回 best。',
        ],
        '单调栈',
        code_notes=[
            'heights = [0] * cols — 每列连续 1 的高度柱状图。',
            'heights[j] = heights[j] + 1 if row[j] == "1" else 0 — 逐行累积或清零。',
            'best = max(best, largest_rectangle_area(heights)) — 每行转化为 LC 84。',
            'largest_rectangle_area 用 padded=[0,*heights,0] 与单调栈。',
            'while padded[i] < padded[stack[-1]] — 弹出计算 width × height。',
            '二维问题降为一维 histogram 重复求解。',
            'cols = len(matrix[0]) — 列数固定，heights 可复用。',
        ],
        complexity='时间 O(rows × cols)，空间 O(cols)。',
    ),
    'paradigms/greedy/greedy.py::insert_interval': _m(
        '57', '插入区间',
        '给你一个无重叠、按区间起始端点排序的区间列表 intervals，'
        'intervals[i] = [start_i, end_i]，'
        '以及一个待插入区间 newInterval = [start, end]。\n\n'
        '请确保 intervals 仍无重叠且按 start 升序，'
        '必要时合并相邻或重叠区间。\n\n'
        '约束：0 ≤ intervals.length ≤ 10⁴；'
        'intervals[i].length == 2；0 ≤ start_i ≤ end_i ≤ 10⁵；'
        'intervals 无重叠且按 start 升序。',
        [
            '示例 1：intervals = [[1,3],[6,9]], newInterval = [2,5] → [[1,5],[6,9]]。'
            '2-5 与 1-3 合并。',
            '示例 2：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8] → [[1,2],[3,10],[12,16]]。',
            '示例 3：intervals = [], newInterval = [5,7] → [[5,7]]。',
        ],
        [
            '维护 result 与 inserted 标志。',
            '遍历 [lo, hi]：若 hi < start，区间在新区间左侧，直接 append。',
            '若 lo > end，新区间应在当前区间前插入（若未插入），再 append 当前区间。',
            '否则与新区间重叠，扩展 start = min(start, lo)、end = max(end, hi)。',
            '遍历结束若未插入，将合并后的 [start, end] append。',
        ],
        '贪心',
        code_notes=[
            'start, end = newInterval — 合并过程中区间可能扩展。',
            'inserted = False — 标记新区间是否已写入 result。',
            'if hi < start: result.append([lo, hi]) — 完全在左侧，无重叠。',
            'elif lo > end: if not inserted: result.append([start,end]); inserted=True — 右侧首次越界时插入。',
            'else: start = min(start, lo); end = max(end, hi) — 重叠则合并扩展。',
            'if not inserted: result.append([start, end]) — 新区间在最后或最大。',
            '一次线性扫描 O(n)，无需先插入再 merge。',
        ],
        complexity='时间 O(n)，空间 O(n)，n = len(intervals)。',
    ),
    'paradigms/dynamic_programming/sequence_dp.py::num_trees': _m(
        '96', '不同的二叉搜索树',
        '给定整数 n，'
        '求以 1 到 n 为节点组成的二叉搜索树有多少种不同结构。\n\n'
        'BST 性质：左子树所有节点 < 根 < 右子树所有节点；'
        'dp[n] = Σ dp[i-1] * dp[n-i]（i 为根节点值）。\n\n'
        '约束：1 ≤ n ≤ 19。',
        [
            '示例 1：n = 3 → 5。'
            '五种不同 BST 结构。',
            '示例 2：n = 1 → 1。',
            '示例 3：n = 2 → 2。'
            '根为 1 或 2 各一种。',
        ],
        [
            'dp[0] = 1（空树一种结构）。',
            '对 nodes 从 1 到 n：枚举根 root 从 1 到 nodes。',
            '左子树节点数 root-1，右子树 nodes-root。',
            'dp[nodes] += dp[root-1] * dp[nodes-root] — 卡特兰数递推。',
            '返回 dp[n]。',
        ],
        '动态规划',
        code_notes=[
            'dp = [0] * (n + 1); dp[0] = 1 — 空树计数为 1。',
            'for nodes in range(1, n + 1) — 子问题规模递增。',
            'for root in range(1, nodes + 1) — 枚举根节点值。',
            'dp[nodes] += dp[root - 1] * dp[nodes - root] — 左右独立，乘法原理。',
            '左子树由 1..root-1 构成，右子树由 root+1..nodes 构成。',
            '结果为卡特兰数 C_n；n=19 时 dp 值较大但仍在 int 范围。',
            '也可直接用卡特兰公式 C(2n,n)/(n+1)。',
        ],
        complexity='时间 O(n²)，空间 O(n)。',
    ),
    'strings/pattern_matching.py::is_match': _m(
        '10', '正则表达式匹配',
        '给你一个字符串 s 和一个字符规律 p，'
        '请实现支持 "." 和 "*" 的正则表达式匹配。\n\n'
        '"." 匹配任意单个字符；'
        '"*" 匹配零个或多个前面的那一个元素。'
        '保证每次出现 "*" 时前面都有一个有效字符。\n\n'
        '约束：1 ≤ s.length ≤ 20；1 ≤ p.length ≤ 30；'
        's 仅含小写英文字母；p 含小写字母、"."、"*"。',
        [
            '示例 1：s = "aa", p = "a" → false。',
            '示例 2：s = "aa", p = "a*" → true。'
            'a* 可匹配 aa。',
            '示例 3：s = "ab", p = ".*" → true。'
            '.* 可匹配任意串。',
        ],
        [
            'dp[i][j] 表示 s 前 i 字符与 p 前 j 字符是否匹配。',
            '初始化 dp[0][0] = True；处理 p 中 a*b* 类空串匹配 dp[0][j]。',
            '双重循环填表：若 p[j-1]=="*"，'
            '可不匹配（dp[i][j-2]）或重复前一字符（dp[i-1][j] 且字符匹配）。',
            '若 p[j-1] 为普通字符或 "."，'
            '需 dp[i-1][j-1] 且字符匹配。',
            '返回 dp[m][n]。',
        ],
        '动态规划',
        code_notes=[
            'dp = [[False] * (n+1) for _ in range(m+1)] — (m+1)×(n+1) 状态表。',
            'dp[0][0] = True — 空串匹配空模式。',
            'if p[j-1] == "*": dp[0][j] = dp[0][j-2] — 空 s 时 a*b* 可消为零。',
            'dp[i][j] = dp[i][j-2] — * 匹配零次前一字符。',
            'if p[j-2] == "." or p[j-2] == s[i-1]: dp[i][j] |= dp[i-1][j] — * 匹配一次或多次。',
            'elif p[j-1] == "." or p[j-1] == s[i-1]: dp[i][j] = dp[i-1][j-1] — 普通匹配。',
            'return dp[m][n] — 全串匹配结果。',
        ],
        complexity='时间 O(m×n)，空间 O(m×n)，m = len(s)，n = len(p)。',
    ),
    'strings/operations.py::my_atoi': _m(
        '8', '字符串转换整数 (atoi)',
        '请你来实现一个 myatoi(s) 函数，'
        '使其能将字符串转换成一个 32 位有符号整数。\n\n'
        '算法流程：'
        '1. 忽略前导空格；'
        '2. 检查正负号；'
        '3. 读入数字直到非数字；'
        '4. 溢出则 clamp 到 [−2³¹, 2³¹−1]。\n\n'
        '约束：0 ≤ s.length ≤ 200；'
        's 由英文字母、数字、空格和符号组成。',
        [
            '示例 1：s = "42" → 42。',
            '示例 2：s = "   -42" → -42。'
            '前导空格与负号。',
            '示例 3：s = "4193 with words" → 4193。'
            '读到空格停止。',
        ],
        [
            '跳过前导空格，指针 i 前进。',
            '读取可选正负号 sign = ±1。',
            '循环读取数字字符，累加 result = result * 10 + digit。',
            '累加前检查溢出：若 result > (bound - digit) // 10，'
            '返回 bound-1（正）或 -bound（负）。',
            '返回 sign * result。',
        ],
        '字符串',
        code_notes=[
            'while i < len(s) and s[i] == " ": i += 1 — 跳过前导空格。',
            'sign = -1 if s[i] == "-" else 1 — 处理可选符号。',
            'bound = 2 ** 31 — 32 位有符号边界。',
            'if result > (bound - digit) // 10: return ... — 溢出 clamp。',
            'result = result * 10 + digit — 逐位构建整数。',
            'ord(s[i]) - ord("0") — 字符转数字。',
            '读到非数字即停止，不解析后续。',
        ],
        complexity='时间 O(len(s))，空间 O(1)。',
    ),
    'paradigms/backtracking/core.py::solve_n_queens': _m(
        '51', 'N 皇后',
        '按照国际象棋的规则，'
        '皇后可以攻击与之处在同一行、同一列、'
        '同一对角线上的棋子。\n\n'
        'n 皇后问题研究如何将 n 个皇后放在 n×n 棋盘上，'
        '使它们不能互相攻击。'
        '给你一个整数 n，'
        '返回所有不同的 N 皇后解决方案。\n\n'
        '约束：1 ≤ n ≤ 9。',
        [
            '示例 1：n = 4 → [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]。'
            '两种解法。',
            '示例 2：n = 1 → [["Q"]]。',
            '示例 3：n = 2 → []。'
            '无解。',
        ],
        [
            '维护 cols、diag1（row-col）、diag2（row+col）三个集合记录占用。',
            'board 为 n×n 字符矩阵，backtrack(row) 逐行放置皇后。',
            'row == n 时收集当前 board 快照加入 result。',
            '每行尝试 col：若列或对角冲突则 skip。',
            '放置皇后：更新集合与 board，递归 row+1，回溯撤销。',
        ],
        '回溯',
        code_notes=[
            'cols, diag1, diag2: set[int] — 列与两条对角线占用标记。',
            'row - col in diag1; row + col in diag2 — 对角线编码。',
            'board = [["."] * n for _ in range(n)] — 棋盘状态。',
            'if row == n: result.append(["".join(line) for line in board]) — 收集解。',
            'board[row][col] = "Q" — 放置；回溯时恢复 "."。',
            'cols.add(col); ... backtrack(row+1); cols.remove(col) — 标准回溯。',
            '每行只放一个皇后，逐行 DFS 共 n 层。',
        ],
        complexity='时间 O(n!) 量级，空间 O(n²)（board 与递归栈）。',
    ),
    'paradigms/backtracking/core.py::remove_invalid_parentheses': _m(
        '301', '删除无效的括号',
        '给你一个由若干括号和字母组成的字符串 s，'
        '删除最小数量的无效括号，'
        '使得输入字符串有效；'
        '返回所有可能的结果。'
        '答案可以按任意顺序返回。\n\n'
        '有效字符串需满足：'
        '任意前缀左括号数 ≥ 右括号数，且总数平衡。\n\n'
        '约束：1 ≤ s.length ≤ 25；'
        's 由小写英文字母及 "("、")" 组成。',
        [
            '示例 1：s = "()())()" → ["(())()","()()()"]。',
            '示例 2：s = "(a)())()" → ["(a())()","(a)()()"]。',
            '示例 3：s = ")(" → [""]。'
            '需删光括号。',
        ],
        [
            'BFS 层序：从 s 出发，逐层删除一个 "(" 或 ")" 生成下一层。',
            'is_valid 检查括号平衡：遇 ")" 时 balance 减至负则无效。',
            '若当前串 valid，加入 result 并设 found = True。',
            '若 found 为 True，同层其余不再扩展（保证删除数最少）。',
            'visited 集合去重；返回 list(result)。',
        ],
        '回溯',
        code_notes=[
            'def is_valid(text) — balance 计数，")" 使 balance<0 则 False。',
            'queue = [s]; visited = {s} — BFS 初始状态。',
            'if is_valid(cur): result.add(cur); found = True — 首次 valid 定最小删除数。',
            'if found: continue — 同层不再扩展，保证最小删除。',
            'nxt = cur[:i] + cur[i+1:] — 每次删一个括号字符。',
            'if cur[i] not in "()": continue — 字母不删。',
            'BFS 保证先找到删除数最少的层；set 去重。',
        ],
        complexity='时间 O(2^n) 最坏，空间 O(2^n)（队列与 visited）。',
    ),
    'data_structures/matrix/matrix.py::spiral_order': _m(
        '54', '螺旋矩阵',
        '给你一个 m×n 矩阵 matrix，'
        '请按照顺时针螺旋顺序，'
        '返回矩阵中的所有元素。\n\n'
        '约束：m == matrix.length；n == matrix[i].length；'
        '1 ≤ m, n ≤ 10；'
        '-100 ≤ matrix[i][j] ≤ 100。',
        [
            '示例 1：matrix = [[1,2,3],[4,5,6],[7,8,9]] → [1,2,3,6,9,8,7,4,5]。',
            '示例 2：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] → [1,2,3,4,8,12,11,10,9,5,6,7]。',
            '示例 3：matrix = [[1]] → [1]。',
        ],
        [
            '维护四边界 top、bottom、left、right。',
            'while top <= bottom and left <= right 循环：',
            '从左到右遍历 top 行，top += 1。',
            '从上到下遍历 right 列，right -= 1。',
            '若 top <= bottom，从右到左遍历 bottom 行，bottom -= 1。',
            '若 left <= right，从下到上遍历 left 列，left += 1。',
            '返回 result。',
        ],
        '矩阵',
        code_notes=[
            'top, bottom = 0, len(matrix)-1 — 上下边界。',
            'left, right = 0, len(matrix[0])-1 — 左右边界。',
            'for col in range(left, right+1): result.append(matrix[top][col]) — 顶行左→右。',
            'for row in range(top+1, bottom+1): ... matrix[row][right] — 右列上→下。',
            'if top <= bottom: ... matrix[bottom][col] — 底行右→左，防单行重复。',
            'if left <= right: ... matrix[row][left] — 左列下→上，防单列重复。',
            '每轮收缩一层边界，O(mn) 每个元素访问一次。',
        ],
        complexity='时间 O(m×n)，空间 O(1) 额外（不含输出）。',
    ),
    'patterns/two_pointers/array.py::three_sum_closest': _m(
        '16', '最接近的三数之和',
        '给你一个长度为 n 的整数数组 nums 和一个目标值 target，'
        '请从 nums 中选出三个整数，'
        '使它们的和与 target 最接近。'
        '返回这三个数的和。\n\n'
        '假定每组输入只存在恰好一个最接近的和。\n\n'
        '约束：3 ≤ nums.length ≤ 1000；'
        '-1000 ≤ nums[i] ≤ 1000；'
        '-10⁴ ≤ target ≤ 10⁴。',
        [
            '示例 1：nums = [-1, 2, 1, -4], target = 1 → 2。'
            '和 2 与 target 差值为 1 最小。',
            '示例 2：nums = [0, 0, 0], target = 1 → 0。',
            '示例 3：nums = [1, 1, 1, 0], target = -100 → 2。'
            '三数之和 2 最接近 -100。',
        ],
        [
            'nums.sort() 升序；初始化 closest 为前三个元素之和。',
            '固定指针 i 从 0 到 n-3，内层双指针 left=i+1、right=n-1。',
            '计算 total = nums[i] + nums[left] + nums[right]。',
            '若 |total - target| 更小则更新 closest = total。',
            'total < target 则 left += 1；total > target 则 right -= 1；'
            '相等则直接返回 total。',
            '遍历结束返回 closest。',
        ],
        '双指针',
        code_notes=[
            'nums.sort() — 排序后双指针可行，O(n log n)。',
            'closest = nums[0] + nums[1] + nums[2] — 初始最接近值。',
            'for i in range(len(nums) - 2) — 固定最小元素。',
            'left, right = i + 1, len(nums) - 1 — 夹逼最大两元。',
            'if abs(total - target) < abs(closest - target): closest = total — 更新最优。',
            'if total < target: left += 1 elif total > target: right -= 1 else: return total — 三分支。',
            '与三数之和 LC 15 结构相同，目标改为最小化 |sum - target|。',
        ],
        complexity='时间 O(n²)，空间 O(1)（排序原地）。',
    ),
}
