"""Catalog metadata: common, array, hash_map."""
from meta.helpers import _m

PROBLEMS = {
    'common/kmp.py::build_next': _m('', '构建 KMP next 数组',
        '给定一个模式串 pattern，需要预先计算其「最长相同前后缀」（LPS / next）数组，'
        '供 KMP 匹配时在失配处快速回退，避免主串指针无谓后退。\n\n'
        'next[i] 表示 pattern[0:i) 这段前缀中，最长相同前后缀的长度；'
        'next[0] 恒为 0。该数组是 KMP 算法的核心预处理结果。\n\n'
        '约束：1 ≤ len(pattern) ≤ 10⁴；pattern 由可打印 ASCII 字符组成。',
        [
            '示例 1：pattern = "abab" → [0, 1, 2, 3]。'
            '前缀 "a" 无相同前后缀；前缀 "ab" 相同前后缀 "a" 长 1；'
            '前缀 "aba" 相同前后缀 "a" 长 1；前缀 "abab" 相同前后缀 "ab" 长 3。',
            '示例 2：pattern = "aabaa" → [0, 1, 0, 1, 2]。'
            '前缀 "aabaa" 的最长相同前后缀为 "aa"，长度为 2。',
        ],
        [
            '初始化 nxt = [0]，prefix_len 表示当前已匹配前缀长度，从 i = 1 开始扫描 pattern。',
            '若 pattern[prefix_len] == pattern[i]，说明前缀可延长：prefix_len += 1，写入 nxt[i] = prefix_len，i 前进。',
            '若字符不等且 prefix_len > 0，则回退 prefix_len = nxt[prefix_len - 1]，复用已算结果继续比较，不移动 i。',
            '若 prefix_len 已为 0 仍不匹配，则 nxt[i] = 0，i 前进。',
            'i 遍历完 pattern 后返回 nxt 数组，供 kmp_search 失配回退使用。',
        ],
        'KMP',
        code_notes=[
            'nxt: list[int] — 结果数组，nxt[i] 为 pattern[0:i) 的最长相同前后缀长度。',
            'prefix_len — 当前正在尝试匹配的前缀长度，也是「已匹配前缀」的末尾下标。',
            'while i < len(pattern) — 从第 2 个字符起逐位构建 next 表。',
            'if pattern[prefix_len] == pattern[i] — 当前字符能延长已知前缀，直接 append prefix_len。',
            'elif prefix_len == 0 — 无法延长且无更短前缀可试，当前位 next 值为 0。',
            'else: prefix_len = nxt[prefix_len - 1] — 失配回退，利用已计算的 next 值跳过重复比较。',
            'nxt[0] = 0 由初始化保证，空前缀与单字符前缀无需额外处理。',
        ],
        complexity='时间 O(m)，空间 O(m)，m 为 pattern 长度。',
    ),
    'common/kmp.py::kmp_search': _m('', 'KMP 字符串搜索',
        '给定主串 text 和模式串 pattern，在 text 中查找 pattern 首次出现的起始下标；'
        '若不存在则返回 -1。空模式串约定返回 0。\n\n'
        '朴素匹配在失配时主串指针回退，最坏时间 O(n×m)。'
        'KMP 利用 next 数组在失配时只回退模式串指针，主串指针始终单向前进，整体 O(n+m)。\n\n'
        '约束：0 ≤ len(text), len(pattern) ≤ 10⁴。',
        [
            '示例 1：text = "hello", pattern = "ll" → 2。'
            '下标 2 处开始匹配 "ll"。',
            '示例 2：text = "aaaaa", pattern = "bba" → -1。'
            'text 中不存在 pattern。',
            '示例 3：text = "abc", pattern = "" → 0。'
            '空模式串视为在开头匹配成功。',
        ],
        [
            '若 pattern 为空，直接返回 0。',
            '调用 build_next(pattern) 得到失配回退表 nxt。',
            'j 表示当前已匹配的 pattern 前缀长度，初始为 0；遍历 text 每个字符 ch。',
            '失配时 while j > 0 且 ch != pattern[j]，令 j = nxt[j - 1] 回退，直到可匹配或 j 为 0。',
            '若 ch == pattern[j]，则 j += 1；当 j == len(pattern) 时匹配成功，返回 i - len(pattern) + 1。',
            'text 遍历结束仍未完整匹配，返回 -1。',
        ],
        'KMP',
        code_notes=[
            'if not pattern: return 0 — 空模式串边界处理。',
            'nxt = build_next(pattern) — 预处理模式串，获取失配回退表。',
            'j — 已匹配的 pattern 前缀长度，也是下一个待匹配字符在 pattern 中的下标。',
            'for i, ch in enumerate(text) — 主串指针 i 只增不减，保证线性扫描。',
            'while j > 0 and ch != pattern[j]: j = nxt[j - 1] — 失配时沿 next 链回退 j。',
            'if ch == pattern[j]: j += 1 — 当前字符匹配成功，扩展已匹配前缀。',
            'if j == len(pattern): return i - len(pattern) + 1 — 完整匹配，计算起始下标。',
            'return -1 — 主串扫完仍未匹配。',
        ],
        complexity='时间 O(n + m)，空间 O(m)，n = len(text)，m = len(pattern)。',
    ),
    'common/kmp.py::str_str': _m('28', '实现 strStr()',
        '给你两个字符串 haystack 和 needle，'
        '请找出 needle 在 haystack 中首次出现的位置（下标从 0 开始）。'
        '若 needle 不是 haystack 的子串，则返回 -1。\n\n'
        '若 needle 为空字符串，返回 0。'
        '本题是标准子串搜索问题，本实现直接调用 KMP 搜索函数 kmp_search。\n\n'
        '约束：0 ≤ haystack.length, needle.length ≤ 5×10⁴；'
        'haystack 和 needle 仅由小写英文字母组成。',
        [
            '示例 1：haystack = "sadbutsad", needle = "sad" → 0。'
            '"sad" 从下标 0 开始出现。',
            '示例 2：haystack = "leetcode", needle = "leeto" → -1。'
            'haystack 中不存在 "leeto"。',
            '示例 3：haystack = "hello", needle = "" → 0。'
            '空 needle 在开头匹配。',
        ],
        [
            '本题等价于在 haystack 中查找 needle 首次出现位置。',
            '直接调用 kmp_search(haystack, needle)，复用 KMP 预处理与线性匹配逻辑。',
            'KMP 在失配时利用 next 数组跳过已匹配前缀，避免主串指针回退。',
            '匹配成功返回起始下标，失败返回 -1；空 needle 由 kmp_search 返回 0。',
        ],
        'KMP',
        code_notes=[
            'str_str(haystack, needle) — 对外接口，参数名与 LeetCode 一致。',
            'return kmp_search(haystack, needle) — 一行委托，逻辑全部在 kmp_search 中。',
            'kmp_search 内部先 build_next(needle) 预处理模式串。',
            '整体时间 O(n + m)，优于朴素 O(n×m) 双重循环。',
            'needle 为空时 kmp_search 返回 0，满足题意。',
        ],
        complexity='时间 O(n + m)，空间 O(m)，n = len(haystack)，m = len(needle)。',
    ),
    'data_structures/array/basic.py::plus_one': _m('66', '加一',
        '给定一个由整数组成的非负整数数组 digits，'
        '其中 digits[i] 表示数字的第 i 位（高位在左、低位在右）。'
        '将表示的整数加 1 后，返回新的数字数组。\n\n'
        '数组中任意位置（包括最高位）都可能产生进位，'
        '例如 [9, 9, 9] 加 1 后变为 [1, 0, 0, 0]。'
        '除最高位外，其余位均为 0 到 9 的整数。\n\n'
        '约束：1 ≤ digits.length ≤ 100；0 ≤ digits[i] ≤ 9。',
        [
            '示例 1：digits = [1, 2, 3] → [1, 2, 4]。'
            '123 + 1 = 124。',
            '示例 2：digits = [4, 3, 2, 1] → [4, 3, 2, 2]。'
            '4321 + 1 = 4322。',
            '示例 3：digits = [9, 9, 9] → [1, 0, 0, 0]。'
            '999 + 1 = 1000，最高位产生新进位。',
        ],
        [
            '从数组最后一位（个位）开始，模拟加一过程，维护 carry 进位，初始 carry = 1。',
            '对每一位 i 从右向左：用 divmod(digits[i] + carry, 10) 得到新数位 digits[i] 和新 carry。',
            '若遍历完所有位后 carry 仍为 1（如 999→1000），在数组头部插入 1，返回 [1] + digits。',
            '否则 carry 为 0，直接返回修改后的 digits（原地修改）。',
        ],
        '数组',
        code_notes=[
            'carry = 1 — 初始进位为 1，表示「加一」操作。',
            'for i in range(len(digits) - 1, -1, -1) — 从个位向高位遍历。',
            'carry, digits[i] = divmod(digits[i] + carry, 10) — 同时更新当前位与进位。',
            'return [1] + digits if carry else digits — 最高位仍有进位则在头部补 1。',
            '原地修改 digits 列表，除头部插入外无额外数组。',
        ],
        complexity='时间 O(n)，空间 O(1)（不计返回新数组时头部插入的 O(n) 拷贝）。',
    ),
    'data_structures/array/basic.py::merge_sorted_arrays': _m('88', '合并两个有序数组',
        '给你两个按非递减顺序排列的整数数组 nums1 和 nums2，'
        '以及两个整数 m 和 n，分别表示 nums1 中有效元素个数与 nums2 的元素个数。\n\n'
        'nums1 的尾部有足够空间（size 为 m + n）容纳 nums2 的全部元素。'
        '请将 nums2 合并进 nums1 中，使合并后的数组仍按非递减顺序排列，'
        '结果保存在 nums1 中，无需返回新数组。\n\n'
        '约束：nums1.length == m + n；nums2.length == n；'
        '0 ≤ m, n ≤ 200；1 ≤ m + n ≤ 200；-10⁹ ≤ nums1[i], nums2[j] ≤ 10⁹。',
        [
            '示例 1：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 → [1,2,2,3,5,6]。',
            '示例 2：nums1 = [1], m = 1, nums2 = [], n = 0 → [1]。'
            'nums2 为空，nums1 不变。',
            '示例 3：nums1 = [0], m = 0, nums2 = [1], n = 1 → [1]。'
            'nums1 无有效元素，直接填入 nums2。',
        ],
        [
            '从 nums1 末尾空位开始向前填，pos 指向当前应写入的位置（初始 m + n - 1）。',
            '比较 nums1[m-1] 与 nums2[n-1]，将较大者写入 nums1[pos]，对应指针 m 或 n 减 1，pos 减 1。',
            '当 m > 0 且 n > 0 时重复上述比较填充。',
            '若 nums2 仍有剩余（n > 0），将其拷贝到 nums1 前部；nums1 剩余部分已在正确位置，无需移动。',
            '合并完成后 nums1 即为升序结果。',
        ],
        '数组',
        code_notes=[
            'pos = m + n - 1 — 写入指针从合并数组末尾开始。',
            'while m > 0 and n > 0 — 两数组均还有元素时比较取大。',
            'if nums1[m - 1] < nums2[n - 1] — 取 nums2 较大者写入 pos。',
            'else: nums1[pos] = nums1[m - 1] — 相等时取 nums1 元素（保持稳定）。',
            'while n > 0 — nums2 有剩余时拷贝到 nums1 前部。',
            '函数返回 None，结果原地保存在 nums1 中。',
        ],
        complexity='时间 O(m + n)，空间 O(1)。',
    ),
    'data_structures/array/basic.py::majority_element': _m('169', '多数元素',
        '给定一个大小为 n 的数组 nums，返回其中的多数元素。'
        '多数元素是指在数组中出现次数严格大于 ⌊n/2⌋ 的元素。\n\n'
        '题目保证数组中一定存在多数元素。'
        'Boyer-Moore 投票算法可在 O(n) 时间、O(1) 空间内找到候选众数，'
        '在存在多数元素的前提下无需二次验证。\n\n'
        '约束：n == nums.length；1 ≤ n ≤ 5×10⁴；-10⁹ ≤ nums[i] ≤ 10⁹。',
        [
            '示例 1：nums = [3, 2, 3] → 3。'
            '3 出现 2 次，超过 3/2。',
            '示例 2：nums = [2, 2, 1, 1, 1, 2, 2] → 2。'
            '2 出现 4 次，超过 7/2。',
        ],
        [
            '初始化 candidate = nums[0]，count = 0，表示当前候选众数及其「净票数」。',
            '遍历 nums 每个元素 num：若 count == 0，将 candidate 换为 num。',
            '若 num == candidate，count += 1；否则 count -= 1（不同元素相互抵消）。',
            '遍历结束后 candidate 即为多数元素（题目保证存在，无需再计数验证）。',
        ],
        '数组',
        code_notes=[
            'count = 0 — 净票数，为 0 时需要更换候选。',
            'candidate = nums[0] — 初始候选设为第一个元素。',
            'if count == 0: candidate = num — 票数为 0 时重新提名。',
            'count += 1 if num == candidate else -1 — 同候选加票，异候选减票。',
            'return candidate — 多数元素保证最终 candidate 正确。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/array/basic.py::find_unsorted_subarray': _m('581', '最短无序连续子数组',
        '给你一个整数数组 nums，'
        '找出需要排序的最短连续子数组的长度，'
        '使得整个数组按非递减顺序排列。\n\n'
        '若数组已经有序，则返回 0。'
        '无序段是使数组整体有序所需修改的最短连续区间。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁴；-10⁵ ≤ nums[i] ≤ 10⁵。',
        [
            '示例 1：nums = [2, 6, 4, 8, 10, 9, 15] → 5。'
            '只需排序子数组 [6, 4, 8, 10, 9]，长度为 5。',
            '示例 2：nums = [1, 2, 3, 4] → 0。'
            '数组已有序，无需排序。',
            '示例 3：nums = [1] → 0。'
            '单元素数组已有序。',
        ],
        [
            '从左向右扫描：维护 max_left 为当前见过的最大值；'
            '若 nums[i] < max_left，说明 i 左侧存在更大元素，更新无序右边界 right = i。',
            '从右向左扫描：维护 min_right 为当前见过的最小值；'
            '若 nums[n-i-1] > min_right，说明该位置右侧存在更小元素，更新无序左边界 left = n-i-1。',
            '若 right 从未更新（仍为 -1），说明数组已有序，返回 0。',
            '否则无序段长度为 right - left + 1。',
        ],
        '数组',
        code_notes=[
            'max_left, min_right — 分别记录左扫过程中的最大值与右扫过程中的最小值。',
            'left, right = -1, -1 — 无序区间边界，right == -1 表示已有序。',
            'for i in range(n) — 一次循环同时完成左右两向扫描。',
            'if max_left > nums[i]: right = i — 当前值小于左侧最大值，扩展右边界。',
            'if min_right < nums[n - i - 1]: left = n - i - 1 — 对称更新左边界。',
            'return 0 if right == -1 else right - left + 1 — 边界差加 1 即为长度。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/array/basic.py::increasing_triplet': _m('334', '递增的三元子序列',
        '给你一个整数数组 nums，'
        '判断是否存在三个下标 i、j、k 满足 i < j < k 且 nums[i] < nums[j] < nums[k]。'
        '若存在这样的三元组，返回 true；否则返回 false。\n\n'
        '子序列不要求连续，但下标必须严格递增。'
        '本实现用 O(n) 时间、O(1) 空间维护目前见过的最小值与次小值。\n\n'
        '约束：1 ≤ nums.length ≤ 5×10⁵；-2³¹ ≤ nums[i] ≤ 2³¹ - 1。',
        [
            '示例 1：nums = [1, 2, 3, 4, 5] → true。'
            '任意连续三个元素即满足条件。',
            '示例 2：nums = [5, 4, 3, 2, 1] → false。'
            '严格递减，不存在递增三元组。',
            '示例 3：nums = [2, 1, 5, 0, 4, 6] → true。'
            '三元组 (1, 4, 6) 即 1 < 4 < 6。',
        ],
        [
            '维护 first、second 为目前见过的最小值与次小值，初始均为 inf。',
            '遍历每个 num：若 num > second，说明存在 first < second < num，返回 True。',
            '若 num > first，更新 second = num（在保持 first 的前提下尽量缩小 second）。',
            '否则更新 first = num（尽量让 first 更小，便于后续找到更小的 second）。',
            '全部扫完仍未找到，返回 False。',
        ],
        '数组',
        code_notes=[
            'first = second = float("inf") — 尚未找到有效的一、二次小值。',
            'if num > second: return True — 找到比次小值更大的数，构成三元组。',
            'if num > first: second = num — 更新次小值，first 保持不变。',
            'else: first = num — num 不大于 first，更新最小值。',
            '贪心维护：first 尽量小、second 在 first 固定下尽量小，最大化匹配机会。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/array/basic.py::check_possibility': _m('665', '非递减数列',
        '给你一个长度为 n 的整数数组 nums，'
        '判断能否通过最多修改一个元素（将某个元素改为任意值），'
        '使数组按非递减顺序排列。\n\n'
        '非递减指 nums[i] ≤ nums[i+1] 对所有有效 i 成立。'
        '最多允许一次「下降」并通过修改其中一个元素来修复。\n\n'
        '约束：n == nums.length；1 ≤ n ≤ 10⁴；0 ≤ nums[i] ≤ 10⁴。',
        [
            '示例 1：nums = [4, 2, 3] → true。'
            '将 4 改为 1 或 2，可得 [1,2,3] 或 [2,2,3]。',
            '示例 2：nums = [4, 2, 1] → false。'
            '需要修改超过 1 个元素才能非递减。',
            '示例 3：nums = [3, 4, 2, 5] → true。'
            '将 2 改为 4 即可。',
        ],
        [
            '遍历相邻元素，若 nums[i] > nums[i+1] 则下降次数 changes 加 1，超过 1 次直接返回 False。',
            '遇到下降时，默认修改 nums[i+1] 使其不小于 nums[i]：令 nums[i+1] = nums[i]。',
            '但若 i > 0 且 nums[i+1] < nums[i-1]，改 nums[i+1] 会破坏更前面的非递减关系，'
            '此时应改 nums[i] = nums[i+1]。',
            '遍历结束 changes ≤ 1 则返回 True。',
        ],
        '数组',
        code_notes=[
            'changes = 0 — 记录下降（逆序对）次数。',
            'if nums[i] > nums[i + 1] — 发现非递减被破坏。',
            'if changes > 1: return False — 超过一次修改机会，直接失败。',
            'if i > 0 and nums[i + 1] < nums[i - 1] — 改右端会破坏左邻关系。',
            'nums[i + 1] = nums[i] — 默认贪心修改右端（隐含在 else 分支未触发时）。',
            'nums[i] = nums[i + 1] — 无法改右端时改左端，原地调整便于后续判断。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/array/basic.py::dist_money': _m('2591', '分发糖果',
        '给你两个整数 money 和 children，'
        '分别表示你有的钱数和需要分发糖果的孩子人数。'
        '每个孩子至少获得 1 元，且最多获得 8 元（恰好 8 元视为「得到最多糖果」）。\n\n'
        '返回最多有多少个孩子可以得到恰好 8 元。'
        '若无法给每个孩子至少 1 元，返回 -1。\n\n'
        '约束：1 ≤ money, children ≤ 10⁹。',
        [
            '示例 1：money = 20, children = 3 → 1。'
            '分配 8、1、11 或 8、2、10 等，最多 1 人得 8 元。',
            '示例 2：money = 16, children = 2 → 2。'
            '每人 8 元，恰好分完。',
            '示例 3：money = 3, children = 2 → -1。'
            '每人至少 1 元需要 2 元，但 3 元分给 2 人后无法使两人都得 8 元且满足约束。',
        ],
        [
            '每人至少 1 元，先令 money -= children；若 money < 0，无法分配，返回 -1。',
            '在剩余 money 中，每人再得 7 元即可凑成 8 元；'
            '最多 count = min(money // 7, children) 人得 8 元，并更新 money 与 children。',
            '分配后检查边界：若 children == 0 但 money > 0（钱没分完），或 children == 1 且 money == 3（剩 3 元无法再分 8），'
            '则 count 需减 1。',
            '返回 count。',
        ],
        '数组',
        code_notes=[
            'if money < children: return -1 — 连每人 1 元都不够。',
            'money -= children — 扣除每人保底 1 元后的剩余金额。',
            'count = min(money // 7, children) — 每人再补 7 元凑 8 元，取人数与金额双重上限。',
            'money -= count * 7; children -= count — 更新剩余钱数与未得 8 元的孩子数。',
            'if (children == 0 and money > 0) or (children == 1 and money == 3): count -= 1 — 排除非法分配。',
            'return count — 返回最多得 8 元的人数。',
        ],
        complexity='时间 O(1)，空间 O(1)。',
    ),
    'data_structures/array/basic.py::convert_to_base7': _m('504', '七进制数',
        '给定一个整数 num，将其转换为七进制字符串并返回。\n\n'
        '七进制只使用数字 0-6 表示，不含前导零（但单独的数字 0 应返回 "0"）。'
        '负数需在结果前加负号。\n\n'
        '约束：-10⁷ ≤ num ≤ 10⁷。',
        [
            '示例 1：num = 100 → "202"。'
            '100₁₀ = 2×7² + 0×7¹ + 2×7⁰ = 202₇。',
            '示例 2：num = -7 → "-10"。'
            '负数先取绝对值转换再加负号。',
            '示例 3：num = 0 → "0"。'
            '零的特殊处理。',
        ],
        [
            '若 num == 0，直接返回 "0"；记录 negative = num < 0，取 num 的绝对值。',
            '循环 num % 7 收集各位数字字符，再 num //= 7，直到 num 为 0。',
            '若原数为负，在 digits 末尾追加 "-"（后续反转时负号到最前）。',
            '将 digits 反转后拼接成字符串返回。',
        ],
        '数组',
        code_notes=[
            'if num == 0: return "0" — 零无需进位转换。',
            'negative = num < 0; num = abs(num) — 负数单独处理符号。',
            'digits: list[str] — 按低位到高位收集数位。',
            'digits.append(str(num % 7)); num //= 7 — 标准进制转换循环。',
            'if negative: digits.append("-") — 负号作为最后一位，反转后在首位。',
            'return "".join(reversed(digits)) — 低位在前收集，反转得正确顺序。',
        ],
        complexity='时间 O(log₇|num|)，空间 O(log₇|num|)。',
    ),
    'data_structures/array/basic.py::get_permutation': _m('60', '排列序列',
        '给出 n 和 k，返回 [1, 2, ..., n] 按字典序排列后的第 k 个排列（k 从 1 开始计数）。\n\n'
        '1 到 n 共有 n! 种排列，按字典序从小到大编号为第 1 到第 n! 个。'
        '无需生成全部排列，可通过阶乘数系统直接定位第 k 个。\n\n'
        '约束：1 ≤ n ≤ 9；1 ≤ k ≤ n!。',
        [
            '示例 1：n = 3, k = 3 → "213"。'
            '排列依次为 "123"、"132"、"213"…，第 3 个是 "213"。',
            '示例 2：n = 4, k = 9 → "2314"。'
            '4! = 24 种排列中的第 9 个。',
            '示例 3：n = 3, k = 1 → "123"。'
            '第一个排列即字典序最小。',
        ],
        [
            '列出 nums = ["1", "2", …, "n"] 作为可选数字池，k 转为 0-index（k -= 1）。',
            '从左到右确定每一位：剩余 n-1 个数的排列有 (n-1)! 种，'
            'index = k // (n-1)! 即为当前位应选的数在 nums 中的下标。',
            'pop 出该数加入 result，k %= (n-1)!，n 减 1。',
            '重复直到 n 为 0，拼接 result 返回字符串。',
        ],
        '数组',
        code_notes=[
            'nums = [str(i) for i in range(1, n + 1)] — 可选数字列表。',
            'k -= 1 — 转为 0-index，便于整除取模。',
            'while n > 0: n -= 1 — 每确定一位，剩余规模减 1。',
            'index, k = divmod(k, math.factorial(n)) — 当前位下标与剩余 k。',
            'result.append(nums.pop(index)) — 取出选中数字，不可重复使用。',
            'return "".join(result) — 拼接为排列字符串。',
        ],
        complexity='时间 O(n²)（pop 与阶乘计算），空间 O(n)。',
    ),
    'data_structures/array/basic.py::max_subarray_sum_circular': _m('918', '环形子数组最大和',
        '给定一个环形整数数组 nums（首尾相连），'
        '求非空子数组的最大和。\n\n'
        '子数组可以跨越数组末尾回到开头，例如 nums = [5, -3, 5] 的最大和为 10（取 [5, -3, 5]）。'
        '环形数组的最大子数组和 = max(普通最大子数组和, 总和 - 最小子数组和)，'
        '但子数组不能为空，若全为正则最小子数组和等于总和，需特殊处理。\n\n'
        '约束：1 ≤ nums.length ≤ 3×10⁴；-3×10⁴ ≤ nums[i] ≤ 3×10⁴。',
        [
            '示例 1：nums = [1, -2, 3, -2] → 3。'
            '普通最大子数组和为 3（取 [3]），环形不更优。',
            '示例 2：nums = [5, -3, 5] → 10。'
            '跨越首尾取 [5, -3, 5]。',
            '示例 3：nums = [3, -1, 2, -1] → 4。'
            '取 [3, -1, 2] 或环形等价段。',
        ],
        [
            '分别用 Kadane 算法求 max_subarray（最大子数组和）与 min_subarray（最小子数组和）。',
            '计算 total = sum(nums)。',
            '环形最大和候选为 total - min_subarray（即去掉最小子段后的剩余部分）。',
            '若 min_subarray == total（全为正或全为负导致最小段即全体），不能删全部元素，只能取 max_subarray。',
            '返回 max(max_subarray, total - min_subarray) 在特殊情况下的 max(nums) 或 max_sum。',
        ],
        '数组',
        code_notes=[
            'min_subarray / max_subarray — 内部 Kadane 函数，dp 维护以当前元素结尾的最小/最大和。',
            'dp = min(value, dp + value) / max(value, dp + value) — Kadane 状态转移。',
            'total = sum(nums) — 数组元素总和。',
            'if min_sum == total: return max(nums) — 全数组为最小段时不能取 total - min_sum。',
            'return max(max_sum, total - min_sum) — 普通最大与环形最大取较大者。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/hash_map/hash_map.py::is_anagram': _m('242', '有效的字母异位词',
        '给你两个字符串 s 和 t，'
        '判断 t 是否是 s 的字母异位词。\n\n'
        '字母异位词指两个字符串包含相同的字符，'
        '且每个字符出现的次数相同；字符顺序可以不同。'
        '若 s 和 t 长度不同，直接返回 false。\n\n'
        '约束：1 ≤ s.length, t.length ≤ 5×10⁴；s 和 t 仅由小写英文字母组成。',
        [
            '示例 1：s = "anagram", t = "nagaram" → true。'
            '两串字符频次完全相同。',
            '示例 2：s = "rat", t = "car" → false。'
            '字符集合不同。',
        ],
        [
            '字母异位词等价于两串各字符出现次数完全相同。',
            '分别用 Counter 统计 s 和 t 的字符频次。',
            '直接比较 Counter(s) == Counter(t)，相等则为异位词。',
            'Counter 比较同时涵盖字符种类与出现次数，O(n) 完成判断。',
        ],
        '哈希表',
        code_notes=[
            'from collections import Counter — 使用标准库计数器。',
            'Counter(s) — 统计 s 中每个字符的出现次数。',
            'Counter(t) — 统计 t 中每个字符的出现次数。',
            'return Counter(s) == Counter(t) — 频次完全相同则返回 True。',
            'Counter 相等性比较键集合与计数值均须一致。',
        ],
        complexity='时间 O(n)，空间 O(1)（字符集大小为 26，视为常数）。',
    ),
    'data_structures/hash_map/hash_map.py::find_anagrams': _m('438', '找到字符串中所有字母异位词',
        '给你两个字符串 s 和 p，'
        '找到 s 中所有 p 的字母异位词的起始下标。'
        '答案可以按任意顺序返回。\n\n'
        '字母异位词指由相同字母以不同顺序组成的字符串，'
        '不包含其他字符。滑动窗口长度固定为 len(p)。\n\n'
        '约束：1 ≤ s.length, p.length ≤ 3×10⁴；s 和 p 仅由小写英文字母组成。',
        [
            '示例 1：s = "cbaebabacd", p = "abc" → [0, 6]。'
            '下标 0 处 "cba" 与 6 处 "bac" 均为 "abc" 的异位词。',
            '示例 2：s = "abab", p = "ab" → [0, 1, 2]。'
            '每个长度为 2 的窗口都是异位词。',
        ],
        [
            '若 len(p) > len(s)，不可能存在异位词，返回 []。',
            '用长度 26 的数组 need 记录 p 的字符频次，window 记录当前窗口频次。',
            '先初始化第一个长度为 len(p) 的窗口，若 window == need 则下标 0 加入结果。',
            '窗口右移：去掉 s[i]、加入 s[i+len(p)]，更新 window；'
            '若 window == need 则记录起始下标 i + 1。',
            '返回所有匹配起始下标列表。',
        ],
        '哈希表',
        code_notes=[
            'need = [0] * 26 — p 的目标字符频次（仅小写字母）。',
            'window = [0] * 26 — 当前滑动窗口的字符频次。',
            'ord(ch) - ord("a") — 将字符映射到 0-25 下标。',
            'result = [0] if window == need else [] — 首窗口匹配则记录 0。',
            'for i in range(len(s) - len(p)) — 窗口左端从 0 滑到 len(s)-len(p)-1。',
            'window[ord(s[i]) - ord("a")] -= 1 — 左端字符移出窗口。',
            'window[ord(s[i + len(p)]) - ord("a")] += 1 — 右端新字符进入窗口。',
            'if window == need: result.append(i + 1) — 新窗口起始下标为 i + 1。',
        ],
        complexity='时间 O(n)，空间 O(1)（固定 26 长度数组）。',
    ),
    'data_structures/hash_map/hash_map.py::can_construct': _m('383', '赎金信',
        '给你两个字符串 ransomNote 和 magazine，'
        '判断能否从 magazine 中挑选字符组成 ransomNote。\n\n'
        'magazine 中的每个字符只能使用一次；'
        '若 ransomNote 中某字符在 magazine 中数量不足，则无法构成。\n\n'
        '约束：1 ≤ ransomNote.length, magazine.length ≤ 10⁵；'
        'ransomNote 和 magazine 由小写英文字母组成。',
        [
            '示例 1：ransomNote = "a", magazine = "b" → false。'
            'magazine 中没有 "a"。',
            '示例 2：ransomNote = "aa", magazine = "aab" → true。'
            'magazine 中有两个 "a"。',
            '示例 3：ransomNote = "aa", magazine = "ab" → false。'
            '"a" 只有一个，不够两个。',
        ],
        [
            '用 Counter 统计 magazine 各字母的可用数量 counts。',
            '遍历 ransomNote 每个字符 ch，将 counts[ch] 减 1。',
            '若某字符 counts[ch] < 0，说明 magazine 中该字母不够用，返回 False。',
            '全部字符都能覆盖则返回 True。',
        ],
        '哈希表',
        code_notes=[
            'counts = Counter(magazine) — 统计 magazine 字母库存。',
            'for ch in ransom_note — 逐个消耗 ransomNote 所需字符。',
            'counts[ch] -= 1 — 每用一个字母，库存减 1。',
            'if counts[ch] < 0: return False — 库存不足，无法构成。',
            'return True — 所有字符均成功消耗。',
        ],
        complexity='时间 O(m + n)，空间 O(1)（字符集 26），m = len(magazine)，n = len(ransomNote)。',
    ),
    'data_structures/hash_map/hash_map.py::common_chars': _m('1002', '查找共用字符',
        '给你一个字符串数组 words，'
        '找出所有字符串的共用字符，'
        '若某字符在多个字符串中出现次数不同，取各串中出现次数的最小值。\n\n'
        '结果中每个字符出现次数等于它在所有字符串中出现次数的最小值，'
        '输出顺序按字母 a-z 排列。\n\n'
        '约束：1 ≤ words.length ≤ 1000；1 ≤ words[i].length ≤ 1000；'
        'words[i] 由小写英文字母组成。',
        [
            '示例 1：words = ["bella","label","roller"] → ["e","l","l"]。'
            '"e" 各出现 1 次，"l" 各至少 2 次，取 min 得 2 个 "l"。',
            '示例 2：words = ["cool","lock","cook"] → ["c","o"]。'
            '"c" 和 "o" 在各串中均出现至少 1 次。',
        ],
        [
            '用 26 位数组 freq 记录第一个单词各字母出现次数。',
            '对其余每个单词统计频次 other，freq 与 other 逐位取 min（公共部分不能超过任一单词）。',
            '按 a-z 顺序遍历 freq：将 min 频次对应的字母重复追加到结果列表。',
            '返回结果列表。',
        ],
        '哈希表',
        code_notes=[
            'if not words: return [] — 空输入边界。',
            'freq = [0] * 26 — 以首词初始化公共频次上界。',
            'other = [0] * 26 — 当前单词的字母频次。',
            'freq = [min(a, b) for a, b in zip(freq, other)] — 逐字母取交集频次。',
            'result.extend(chr(i + ord("a")) * count) — 按字母序追加 count 个该字符。',
            'return result — 共用字符列表。',
        ],
        complexity='时间 O(N × L)，空间 O(1)，N 为单词数，L 为平均单词长度。',
    ),
    'data_structures/hash_map/hash_map.py::two_sum': _m('1', '两数之和',
        '给定一个整数数组 nums 和一个整数目标值 target，'
        '请在数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。\n\n'
        '你可以假设每种输入只会对应一个答案，且同一个元素不能使用两次。'
        '返回的下标须按任意顺序即可。\n\n'
        '约束：2 ≤ nums.length ≤ 10⁴；-10⁹ ≤ nums[i] ≤ 10⁹；-10⁹ ≤ target ≤ 10⁹。',
        '示例：nums = [2,7,11,15], target = 9 → [0,1]，因为 nums[0] + nums[1] = 2 + 7 = 9。',
        [
            '暴力做法是双重循环 O(n²)；优化思路是用哈希表把「找配对」变成 O(1) 查询。',
            '一遍扫描：对每个 value，先查 target - value 是否已在表中；在则返回两数下标。',
            '不在表中则把 value → index 写入哈希表，供后续元素配对。',
            '每个元素最多入表一次，保证不会重复使用同一元素。',
        ],
        '哈希表',
        code_notes=[
            'seen: dict[int, int] — 数值 → 该数值在数组中的下标。',
            'enumerate(nums) 同时得到 index 和 value，一遍扫描即可。',
            'if target - value in seen — 之前见过需要的配对数，且下标一定小于当前 index。',
            'return [seen[target - value], index] — 先见到的下标在前。',
            'seen[value] = index — 未配对成功时入表，供后面的元素查找。',
        ],
        complexity='时间 O(n)，空间 O(n)。',
    ),
    'data_structures/hash_map/hash_map.py::first_uniq_char': _m('387', '字符串中的第一个唯一字符',
        '给定一个字符串 s，'
        '找到它的第一个不重复字符的下标；'
        '若不存在，则返回 -1。\n\n'
        '不重复字符指在字符串中只出现一次的字符。'
        '需要同时考虑出现次数与首次出现位置。\n\n'
        '约束：1 ≤ s.length ≤ 10⁵；s 仅含小写英文字母。',
        [
            '示例 1：s = "leetcode" → 0。'
            '"l" 是第一个只出现一次的字符。',
            '示例 2：s = "loveleetcode" → 2。'
            '"v" 是第一个唯一字符。',
            '示例 3：s = "aabb" → -1。'
            '所有字符均重复，无唯一字符。',
        ],
        [
            '用 defaultdict(list) 记录每个字符出现的所有下标列表 positions。',
            '第一遍扫描：enumerate(s) 将每个字符的下标 append 到 positions[ch]。',
            '第二遍遍历 positions 各字符的下标列表，找出长度为 1 的字符。',
            '取这些唯一字符下标的最小值 best；若没有唯一字符，返回 -1。',
        ],
        '哈希表',
        code_notes=[
            'positions = defaultdict(list) — 字符 → 下标列表。',
            'for index, ch in enumerate(s): positions[ch].append(index) — 收集所有出现位置。',
            'best = float("inf") — 记录最小唯一字符下标。',
            'for indices in positions.values() — 遍历每个字符的下标列表。',
            'if len(indices) == 1: best = min(best, indices[0]) — 唯一字符更新最小下标。',
            'return -1 if best == float("inf") else best — 无唯一字符返回 -1。',
        ],
        complexity='时间 O(n)，空间 O(1)（字符集 26，下标列表总长 n）。',
    ),
    'data_structures/hash_map/hash_map.py::length_of_longest_substring': _m('3', '无重复字符的最长子串',
        '给定一个字符串 s，找出其中不含有重复字符的最长子串的长度。\n\n'
        '子串指字符串中连续的一段字符（例如 "abc" 是 "abcabcbb" 的子串，而 "acb" 不是，因为字符不连续）。'
        '答案只需返回最长子串的长度，不需要输出子串本身。\n\n'
        '约束：0 ≤ s.length ≤ 5×10⁴；s 由英文字母、数字、符号和空格组成。',
        [
            '示例 1：s = "abcabcbb" → 3。不含重复字符的最长子串是 "abc"。',
            '示例 2：s = "bbbbb" → 1。不含重复字符的最长子串是 "b"。',
            '示例 3：s = "pwwkew" → 3。不含重复字符的最长子串是 "wke"；'
            '注意 "pwke" 是子序列而非子串，不能算。',
        ],
        [
            '核心模型是滑动窗口：维护区间 [start, index]，保证窗口内没有重复字符。',
            '右指针 index 从左到右扩展窗口，每加入一个字符就尝试更新当前最长长度。',
            '若新字符 ch 在窗口内已经出现过（last_index[ch] ≥ start），说明窗口非法，'
            '需要把左边界 start 跳到「ch 上次出现位置 + 1」，把重复字符挤出窗口。',
            '哈希表 last_index 只记录每个字符最近出现的下标，O(1) 判断重复并收缩左边界。',
            'index 扫描完整个字符串后，best 即为答案；不需要显式保存子串内容。',
        ],
        '哈希表',
        code_notes=[
            'last_index: dict[str, int] — 字符 → 该字符最近一次出现的下标。',
            'start — 当前无重复窗口的左边界（闭区间）；best — 目前为止的最长子串长度。',
            'for index, ch in enumerate(s) — index 作为右指针，每轮向右扩展一位。',
            'if ch in last_index and last_index[ch] >= start — 重复发生在当前窗口内部；'
            '若 last_index[ch] < start，说明该重复字符已被左边界排除，无需收缩。',
            'start = last_index[ch] + 1 — 左边界跳到重复字符右侧，恢复「无重复」不变量。',
            'best = max(best, index - start + 1) — 窗口 [start, index] 的长度即候选答案。',
            'last_index[ch] = index — 无论是否发生重复，都更新 ch 的最近位置，供后续使用。',
        ],
        complexity='时间 O(n)，空间 O(min(n, |Σ|))，|Σ| 为字符集大小。',
    ),
    'data_structures/hash_map/hash_map.py::is_happy': _m('202', '快乐数',
        '编写一个算法来判断一个数 n 是否为快乐数。\n\n'
        '「快乐数」定义为：对一个正整数，每次将该数替换为它每个数位上数字的平方和，'
        '重复此过程直到结果为 1（是快乐数），或无限循环但始终不为 1（不是快乐数）。\n\n'
        '约束：1 ≤ n ≤ 2³¹ - 1。',
        [
            '示例 1：n = 19 → true。'
            '1² + 9² = 82 → 8² + 2² = 68 → 6² + 8² = 100 → 1² + 0² + 0² = 1。',
            '示例 2：n = 2 → false。'
            '进入循环，永远到不了 1。',
        ],
        [
            '定义 _digit_square_sum(n)：逐位取 n % 10 平方累加，n //= 10，得到数位平方和。',
            '用集合 seen 记录迭代过程中出现过的 n 值。',
            '循环：若 n == 1 则是快乐数；若 n 已在 seen 中则进入循环，不是快乐数。',
            '否则将 n 加入 seen，令 n = _digit_square_sum(n) 继续迭代。',
            '循环结束后 return n == 1。',
        ],
        '哈希表',
        code_notes=[
            'seen: set[int] — 记录已出现过的数值，检测循环。',
            'while n != 1 and n not in seen — 未到 1 且未循环时继续。',
            'seen.add(n) — 当前值入集合，标记已访问。',
            'n = _digit_square_sum(n) — 替换为各位数字平方和。',
            '_digit_square_sum 中 n, rem = divmod(n, 10) — 逐位拆分。',
            'total += rem ** 2 — 累加每位数字的平方。',
            'return n == 1 — 最终为 1 则是快乐数。',
        ],
        complexity='时间 O(log n) 每次迭代位数有限，空间 O(log n) 存储 seen。',
    ),
    'data_structures/hash_map/hash_map.py::group_anagrams': _m('49', '字母异位词分组',
        '给你一个字符串数组 strs，'
        '将字母异位词组合在一起。'
        '字母异位词指字母相同但排列不同的字符串；'
        '字母异位词分组后顺序可以任意。\n\n'
        '异位词具有相同的字符频次，'
        '可用 26 位计数元组作为哈希键，将相同频次的单词归入同一组。\n\n'
        '约束：1 ≤ strs.length ≤ 10⁴；0 ≤ strs[i].length ≤ 100；'
        'strs[i] 仅由小写英文字母组成。',
        [
            '示例 1：strs = ["eat","tea","tan","ate","nat","bat"] → '
            '[["bat"],["nat","tan"],["ate","eat","tea"]]。',
            '示例 2：strs = [""] → [[""]]。'
            '空字符串单独成组。',
            '示例 3：strs = ["a"] → [["a"]]。'
            '单字符串成组。',
        ],
        [
            '异位词具有相同的字符频次，用 26 位计数元组作为签名 _anagram_key(word)。',
            '遍历每个 word，计算 signature，将 word 加入 groups[signature] 列表。',
            'groups 为 defaultdict(list)，自动创建新分组。',
            '返回 list(groups.values())，即所有分组列表。',
        ],
        '哈希表',
        code_notes=[
            'groups: dict[tuple[int, ...], list[str]] = defaultdict(list) — 签名 → 单词列表。',
            'signature = _anagram_key(word) — 计算 26 位字符频次元组作为键。',
            'groups[signature].append(word) — 同签名单词归入同一组。',
            '_anagram_key 中 counts = [0] * 26 — 26 个小写字母计数。',
            'counts[ord(ch) - 97] += 1 — 字符映射到 0-25 并计数。',
            'return tuple(counts) — 元组可哈希，用作 dict 键。',
            'return list(groups.values()) — 输出所有分组（顺序任意）。',
        ],
        complexity='时间 O(N × K)，空间 O(N × K)，N 为字符串数，K 为平均长度。',
    ),
}
