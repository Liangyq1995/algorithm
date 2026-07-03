"""Catalog metadata: linked_list, matrix, patterns."""
from meta.helpers import _m

PROBLEMS = {
    'data_structures/linked_list/linked_list.py::remove_elements': _m(
        '203', '移除链表元素',
        '给你一个链表的头节点 head 和一个整数 val，请你删除链表中所有满足 Node.val == val 的节点，'
        '并返回新的头节点。\n\n'
        '删除操作需要在原链表上完成，通常借助哑节点（dummy）统一处理「头节点也可能被删」的情况。'
        '遍历过程中若下一个节点的值等于 val，则跳过该节点；否则指针正常前进。\n\n'
        '约束：链表节点数目在范围 [0, 10⁴] 内；0 ≤ Node.val ≤ 50；0 ≤ val ≤ 50。',
        [
            '示例 1：head = [1,2,6,3,4,5,6], val = 6 → [1,2,3,4,5]',
            '示例 2：head = [], val = 1 → []',
            '示例 3：head = [7,7,7,7], val = 7 → []',
        ],
        [
            '创建哑节点 dummy 指向 head，cur 从 dummy 出发，避免删除头节点的特判。',
            '当 cur.next 存在且 cur.next.val == val 时，执行 cur.next = cur.next.next 跳过目标节点。',
            '否则 cur 前进一位，继续检查后续节点。',
            '遍历结束后返回 dummy.next 作为新链表头。',
        ],
        '链表',
        code_notes=[
            'dummy = ListNode(0, head) — 哑节点简化头节点删除逻辑。',
            'cur = dummy — 当前指针始终指向「待检查节点的前驱」。',
            'while cur.next — 只要还有后继节点就继续检查。',
            'if cur.next.val == val: cur.next = cur.next.next — 跳过值等于 val 的节点。',
            'else: cur = cur.next — 当前后继保留，指针前进。',
            'return dummy.next — 返回真实头节点（可能已被替换）。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::reverse_list': _m(
        '206', '反转链表',
        '给你单链表的头节点 head，请你反转链表，并返回反转后的链表头节点。\n\n'
        '迭代解法维护三个指针：prev 指向已反转部分的头，cur 指向当前待处理节点，'
        '每次将 cur.next 改指 prev，然后整体前移。\n\n'
        '约束：链表中节点的数目范围是 [0, 5000]；-5000 ≤ Node.val ≤ 5000。',
        [
            '示例 1：head = [1,2,3,4,5] → [5,4,3,2,1]',
            '示例 2：head = [1,2] → [2,1]',
            '示例 3：head = [] → []',
        ],
        [
            '初始化 prev = None，cur = head。',
            '循环中先保存 nxt = cur.next，防止断链。',
            '将 cur.next 指向 prev，完成当前节点的反转。',
            'prev 和 cur 各前进一步，直到 cur 为 None。',
            '循环结束时 prev 即为新头节点。',
        ],
        '链表',
        code_notes=[
            'prev = None — 已反转部分的头，初始为空。',
            'while head — 以 head 作为 cur 逐节点处理。',
            'nxt = head.next — 暂存后继，避免修改 next 后丢失链表。',
            'head.next = prev — 当前节点反向指向前驱。',
            'prev = head; head = nxt — 双指针同步前移。',
            'return prev — 遍历结束后 prev 指向新链表头。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::reverse_between': _m(
        '92', '反转链表 II',
        '给你单链表的头指针 head 和两个整数 left 和 right，其中 left ≤ right。'
        '请你反转从位置 left 到位置 right 的链表节点，返回反转后的链表。\n\n'
        '本实现采用头插法：定位 left 前驱 prev 后，反复将 cur 的下一个节点摘下并插到 prev 之后，'
        '共执行 right - left 次，实现局部反转而无需额外空间。\n\n'
        '约束：链表中节点数目为 n；1 ≤ n ≤ 500；-500 ≤ Node.val ≤ 500；1 ≤ left ≤ right ≤ n。',
        [
            '示例 1：head = [1,2,3,4,5], left = 2, right = 4 → [1,4,3,2,5]',
            '示例 2：head = [5], left = 1, right = 1 → [5]',
        ],
        [
            'dummy 指向 head；prev 走到 left 位置的前一个节点。',
            'cur 固定在 left 处，作为待反转段的「锚点」。',
            '头插法：取 nxt = cur.next，将其从原位置摘下。',
            'nxt.next = prev.next，prev.next = nxt，完成一次头插。',
            '重复 right - left 次后，cur 之后的段已全部反转到 prev 之后。',
        ],
        '链表',
        code_notes=[
            'dummy = ListNode(0, head) — 哑节点，prev 最终停在 left 前一位。',
            'for _ in range(left - 1): prev = prev.next — 定位反转区间前驱。',
            'cur = prev.next — 锚点节点，位置不变。',
            'nxt = cur.next; cur.next = nxt.next — 将 cur 的后继摘下。',
            'nxt.next = prev.next; prev.next = nxt — 头插到 prev 之后。',
            '循环 right - left 次 — 每次将 cur 后一个节点移到区间头部。',
            'return dummy.next — 返回可能变化的头节点。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::odd_even_list': _m(
        '328', '奇偶链表',
        '给定单链表的头节点 head，将所有奇数下标（下标从 0 开始）的节点排在前面，'
        '偶数下标的节点排在后面，并保持各自相对顺序，返回重排后的链表。\n\n'
        '用 odd 和 even 两条指针分别维护奇数位链和偶数位链的尾部，'
        '最后将偶链接到奇链末尾即可，无需额外数组。\n\n'
        '约束：n == 链表中的节点数；0 ≤ n ≤ 10⁴；-10⁶ ≤ Node.val ≤ 10⁶。',
        [
            '示例 1：head = [1,2,3,4,5] → [1,3,5,2,4]',
            '示例 2：head = [2,1,3,5,6,4,7] → [2,3,6,7,1,5,4]',
        ],
        [
            '若 head 为空直接返回；odd 指向第 0 位，even 指向第 1 位，even_head 保存偶链头。',
            'while even 且 even.next：odd.next = even.next（奇链连下一奇），odd 前进。',
            'even.next = odd.next（偶链连下一偶），even 前进。',
            'odd.next = even_head 将偶链整体接到奇链尾部。',
        ],
        '链表',
        code_notes=[
            'odd, even = head, head.next — 分别指向当前奇、偶链尾部。',
            'even_head = even — 保存偶数位链表的头，便于最后拼接。',
            'odd.next = even.next — 将下一奇数节点接到奇链。',
            'odd = odd.next — 奇指针前进。',
            'even.next = odd.next — 将下一偶数节点接到偶链。',
            'even = even.next — 偶指针前进。',
            'odd.next = even_head — 奇链尾连接偶链头，完成重排。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::add_two_numbers': _m(
        '2', '两数相加',
        '给你两个非空的链表，每个链表的每个节点存放一个 0-9 的数字，'
        '所表示的数字是逆序存储的（个位在前）。请你将两个数相加，并以相同形式返回一个表示和的链表。\n\n'
        '模拟竖式加法：逐位相加并维护进位 carry，用 divmod 分离当前位与进位。'
        '两链长度可能不同，需处理某一链先耗尽但仍有进位的情况。\n\n'
        '约束：每个链表中的节点数在范围 [1, 100] 内；0 ≤ Node.val ≤ 9；'
        '题目数据保证链表表示的数字不含前导零。',
        [
            '示例 1：l1 = [2,4,3], l2 = [5,6,4] → [7,0,8]，342 + 465 = 807。',
            '示例 2：l1 = [0], l2 = [0] → [0]',
            '示例 3：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] → [8,9,9,9,0,0,0,1]',
        ],
        [
            'dummy 哑节点作为结果链起点，carry 初始为 0。',
            'while l1 或 l2 或 carry 非零时继续循环。',
            '累加当前两链节点值（若存在）与 carry 得到 total。',
            'divmod(total, 10) 得到新节点 digit 和更新后的 carry。',
            '创建 ListNode(digit) 接到结果链尾部，对应链指针前进。',
        ],
        '链表',
        code_notes=[
            'dummy = ListNode(); cur = dummy — 结果链哑节点与尾指针。',
            'carry = 0 — 进位，初始为零。',
            'while l1 or l2 or carry — 任一路径未走完或仍有进位则继续。',
            'total = carry; 若 l1/l2 存在则累加对应 val 并前进。',
            'carry, digit = divmod(total, 10) — 分离进位与当前位。',
            'cur.next = ListNode(digit); cur = cur.next — 追加新节点。',
            'return dummy.next — 返回结果链表头。',
        ],
        complexity='时间 O(max(m,n))，空间 O(max(m,n))（结果链表）。',
    ),
    'data_structures/linked_list/linked_list.py::swap_pairs': _m(
        '24', '两两交换链表中的节点',
        '给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。'
        '你必须在不修改节点值的情况下完成（即只能交换指针）。\n\n'
        '借助 dummy 和 prev，每次处理一对相邻节点 first 与 second，'
        '调整指针使 second 在前、first 在后，然后 prev 移到 first 继续下一对。\n\n'
        '约束：链表中节点的数目在范围 [0, 100] 内；0 ≤ Node.val ≤ 100。',
        [
            '示例 1：head = [1,2,3,4] → [2,1,4,3]',
            '示例 2：head = [] → []',
            '示例 3：head = [1] → [1]',
        ],
        [
            'dummy 指向 head，prev 指向待交换对的前驱。',
            '当 prev.next 与 prev.next.next 均存在时进入交换循环。',
            'first = prev.next, second = first.next 定位当前对。',
            '调整指针：first.next = second.next, second.next = first, prev.next = second。',
            'prev 移到 first（交换后的第二个），处理下一对。',
        ],
        '链表',
        code_notes=[
            'dummy = ListNode(0, head); prev = dummy — 哑节点简化头交换。',
            'while prev.next and prev.next.next — 至少还有两个节点可交换。',
            'first = prev.next; second = first.next — 定位相邻对。',
            'first.next = second.next — first 指向 second 的后继。',
            'second.next = first — second 指向 first，完成局部反转。',
            'prev.next = second — 前驱指向新对首 second。',
            'prev = first — 前驱移到交换后的第二个节点。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::remove_nth_from_end': _m(
        '19', '删除链表的倒数第 N 个结点',
        '给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头节点。\n\n'
        '快慢指针：fast 先走 n+1 步，再与 slow 同步前进；'
        '当 fast 到达末尾时，slow 恰在待删节点的前驱，一次删除即可。\n\n'
        '约束：链表中结点的数目为 sz；1 ≤ n ≤ sz；0 ≤ Node.val ≤ 500。',
        [
            '示例 1：head = [1,2,3,4,5], n = 2 → [1,2,3,5]',
            '示例 2：head = [1], n = 1 → []',
            '示例 3：head = [1,2], n = 1 → [1]',
        ],
        [
            'dummy 指向 head，fast 和 slow 均从 dummy 出发。',
            'fast 先前进 n+1 步，拉开与 slow 的固定距离。',
            'fast 与 slow 同步前进，直到 fast 为 None。',
            '此时 slow.next 即为倒数第 n 个节点，执行 slow.next = slow.next.next 删除。',
        ],
        '链表',
        code_notes=[
            'dummy = ListNode(0, head) — 处理删除头节点的边界。',
            'fast = slow = dummy — 双指针同起点。',
            'for _ in range(n + 1): fast = fast.next — fast 领先 n+1 步。',
            'while fast: fast = fast.next; slow = slow.next — 同步前进。',
            'slow.next = slow.next.next — 跳过倒数第 n 个节点。',
            'return dummy.next — 返回可能更新的头节点。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::get_intersection_node': _m(
        '160', '相交链表',
        '给你两个单链表的头节点 headA 和 headB，请你找出并返回两个单链表相交的起始节点。'
        '如果两个链表没有交点，返回 null。\n\n'
        '设两链长度分别为 a+c 和 b+c（c 为公共尾部长度）。'
        '两指针各走 a+b 步后必在交点相遇（或同时为 None），无需计算长度。\n\n'
        '约束：listA 中节点数目为 m；listB 中节点数目为 n；1 ≤ m, n ≤ 3×10⁴；'
        'intersectVal 为 0 或 listA[intersectVal] == listB[intersectVal]；'
        '如果两个链表没有交点，intersectVal 为 0。',
        [
            '示例 1：listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], 相交于值为 8 的节点 → 返回该节点',
            '示例 2：listA = [2,6,4], listB = [1,5], 无相交 → null',
        ],
        [
            'pa 从 headA、pb 从 headB 同时出发。',
            '各自走到末尾后切换到另一条链的头，继续同步前进。',
            '若相交，两指针会在交点相遇；不相交则同时变为 None。',
            '返回 pa（即相遇节点或 None）。',
        ],
        '链表',
        code_notes=[
            'pa, pb = head_a, head_b — 两指针分别遍历两链。',
            'while pa != pb — 直到相遇（含同为 None 的情况）。',
            'pa = pa.next if pa else head_b — 走完 A 则切到 B 头。',
            'pb = pb.next if pb else head_a — 走完 B 则切到 A 头。',
            'return pa — 交点节点或 None。',
        ],
        complexity='时间 O(m+n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::partition_list': _m(
        '86', '分隔链表',
        '给你一个链表的头节点 head 和一个特定值 x，请你对链表进行分隔，'
        '使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。'
        '你应当保留两个分区中每个节点的初始相对顺序。\n\n'
        '维护 before 和 after 两条独立链表，遍历原链按值分流，最后拼接。\n\n'
        '约束：链表中节点的数目在范围 [0, 200] 内；-100 ≤ Node.val ≤ 100；-200 ≤ x ≤ 200。',
        [
            '示例 1：head = [1,4,3,2,5,2], x = 3 → [1,2,2,4,3,5]',
            '示例 2：head = [2,1], x = 2 → [1,2]',
        ],
        [
            'before_dummy/before 维护小于 x 的链，after_dummy/after 维护其余链。',
            '遍历 head：按值接到 before 或 after 尾部，原节点 next 不断前进。',
            'after.next = None 防止成环。',
            'before.next = after_dummy.next 拼接两链，返回 before_dummy.next。',
        ],
        '链表',
        code_notes=[
            'before_dummy = before = ListNode() — 小于 x 的哑链。',
            'after_dummy = after = ListNode() — 大于等于 x 的哑链。',
            'if head.val < x: before.next = head; before = before.next — 分流到 before 链。',
            'else: after.next = head; after = after.next — 分流到 after 链。',
            'head = head.next — 原链指针前进。',
            'after.next = None — 截断 after 链尾，避免环。',
            'before.next = after_dummy.next — 拼接两链。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::reorder_list': _m(
        '143', '重排链表',
        '给定一个单链表 L 的头节点 head，请将其重新排列为 L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …\n\n'
        '本实现先将所有节点存入数组，再用双指针从两端交替拼接 next 指针，'
        '直观易懂；进阶可拆分为找中点、反转后半、合并三步。\n\n'
        '约束：链表的长度范围为 [1, 5×10⁴]；1 ≤ Node.val ≤ 1000。',
        [
            '示例 1：head = [1,2,3,4] → [1,4,2,3]',
            '示例 2：head = [1,2,3,4,5] → [1,5,2,4,3]',
        ],
        [
            '遍历链表，将所有节点引用存入数组 nodes。',
            '双指针 left=0、right=len-1 从两端向中间移动。',
            'nodes[left].next = nodes[right]，left 前进；若 left==right 则断开。',
            'nodes[right].next = nodes[left]，right 后退，交替拼接。',
            '最后 nodes[left].next = None 截断尾部，返回 nodes[0]。',
        ],
        '链表',
        code_notes=[
            'nodes: list[ListNode] — 按顺序存储所有节点引用。',
            'cur = head — 遍历原链收集节点。',
            'left, right = 0, len(nodes) - 1 — 双指针从两端向中间。',
            'nodes[left].next = nodes[right]; left += 1 — 左端连右端。',
            'if left == right: break — 奇数个节点时避免自环。',
            'nodes[right].next = nodes[left]; right -= 1 — 右端连下一左端。',
            'nodes[left].next = None — 截断链表尾。',
        ],
        complexity='时间 O(n)，空间 O(n)。',
    ),
    'data_structures/linked_list/linked_list.py::delete_duplicates': _m(
        '83', '删除排序链表中的重复元素',
        '给定一个已排序的链表的头 head，删除所有重复的元素，使每个元素只出现一次。'
        '返回已排序的链表。\n\n'
        '有序链表重复值必相邻，cur 遍历时若 cur.val == cur.next.val 则跳过 cur.next，'
        '否则 cur 前进。\n\n'
        '约束：链表中节点数目在范围 [0, 300] 内；-100 ≤ Node.val ≤ 100；'
        '题目数据保证链表已经按升序排列。',
        [
            '示例 1：head = [1,1,2] → [1,2]',
            '示例 2：head = [1,1,2,3,3] → [1,2,3]',
        ],
        [
            'cur 从 head 出发，检查 cur 与 cur.next。',
            '若值相等，cur.next = cur.next.next 删除重复后继。',
            '若不相等，cur = cur.next 前进。',
            '重复直到 cur.next 为空，返回 head。',
        ],
        '链表',
        code_notes=[
            'cur = head — 当前检查节点。',
            'while cur and cur.next — 确保有后继可比较。',
            'if cur.val == cur.next.val — 发现相邻重复。',
            'cur.next = cur.next.next — 跳过一个重复节点。',
            'else: cur = cur.next — 无重复则前进。',
            'return head — 头节点不变。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::delete_all_duplicates': _m(
        '82', '删除排序链表中的重复元素 II',
        '给定一个已排序的链表的头 head，删除原始链表中所有重复数字的节点，'
        '只留下不同的数字。返回已排序的链表。\n\n'
        '与 LC83 不同：凡出现重复的值，其所有节点均删除。'
        'dummy + prev 指针，发现重复段则整段跳过。\n\n'
        '约束：链表中节点数目在范围 [0, 300] 内；-100 ≤ Node.val ≤ 100；'
        '题目数据保证链表已经按升序排列。',
        [
            '示例 1：head = [1,2,3,3,4,4,5] → [1,2,5]',
            '示例 2：head = [1,1,1,2,3] → [2,3]',
        ],
        [
            'dummy 指向 head，prev 指向已确定保留段的最后一个节点。',
            '若 prev.next 与 prev.next.next 值相同，记录 val 并跳过所有值为 val 的节点。',
            '否则 prev 正常前进。',
            '返回 dummy.next。',
        ],
        '链表',
        code_notes=[
            'dummy = ListNode(0, head); prev = dummy — 哑节点处理头重复。',
            'while prev.next and prev.next.next — 至少两个后继可比较。',
            'if prev.next.val == prev.next.next.val — 发现重复段起点。',
            'val = prev.next.val — 记录重复值。',
            'while prev.next and prev.next.val == val — 跳过整段重复。',
            'prev.next = prev.next.next',
            'else: prev = prev.next — 无重复则 prev 前进。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::has_cycle': _m(
        '141', '环形链表',
        '给你一个链表的头节点 head，判断链表中是否有环。\n\n'
        'Floyd 快慢指针：slow 每次走一步，fast 每次走两步；'
        '若存在环则两指针必相遇，无环则 fast 先到达 None。\n\n'
        '约束：链表中节点的数目范围是 [0, 10⁴]；-10⁵ ≤ Node.val ≤ 10⁵；'
        'pos 为 -1 或有效的链表下标（若 pos 为 -1，则无环）。',
        [
            '示例 1：head = [3,2,0,-4], pos = 1 → true（尾连到 index 1）',
            '示例 2：head = [1,2], pos = 0 → true',
            '示例 3：head = [1], pos = -1 → false',
        ],
        [
            'slow 和 fast 均从 head 出发。',
            'fast 每次走两步，slow 走一步，循环条件为 fast 与 fast.next 均非空。',
            '若 slow == fast，说明有环，返回 True。',
            'fast 到达 None 则返回 False。',
        ],
        '链表',
        code_notes=[
            'slow = fast = head — 快慢指针同起点。',
            'while fast and fast.next — fast 需能走两步。',
            'slow = slow.next — 慢指针走一步。',
            'fast = fast.next.next — 快指针走两步。',
            'if slow == fast: return True — 相遇即有环。',
            'return False — fast 到末尾说明无环。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::rotate_right': _m(
        '61', '旋转链表',
        '给你一个链表的头节点 head，旋转链表，将链表每个节点向右移动 k 个位置，'
        '其中 k 是非负数。\n\n'
        '先求长度并对 k 取模；将尾节点连回头部成环，'
        '再在新尾（第 length-k 个节点）处断开得到旋转结果。\n\n'
        '约束：链表中节点的数目在范围 [0, 500] 内；-100 ≤ Node.val ≤ 100；0 ≤ k ≤ 2×10⁹。',
        [
            '示例 1：head = [1,2,3,4,5], k = 2 → [4,5,1,2,3]',
            '示例 2：head = [0,1,2], k = 4 → [2,0,1]',
        ],
        [
            '遍历求 length 和 tail；k %= length，k==0 直接返回 head。',
            'tail.next = head 将链表首尾相连成环。',
            'new_tail 从 head 走 length-k-1 步，new_head = new_tail.next。',
            'new_tail.next = None 断开环，返回 new_head。',
        ],
        '链表',
        code_notes=[
            'length = 1; tail = head — 初始化长度与尾节点。',
            'while tail.next — 遍历求 length 和 tail。',
            'k %= length; if k == 0: return head — 取模避免无效旋转。',
            'tail.next = head — 首尾相连成环。',
            'new_tail = head; for _ in range(steps - 1) — 定位新尾。',
            'new_head = new_tail.next; new_tail.next = None — 断开并返回新头。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::detect_cycle': _m(
        '142', '环形链表 II',
        '给定一个链表 head，返回链表开始入环的第一个节点。如果链表无环，则返回 null。\n\n'
        '快慢指针相遇后，令 slow 回到 head，两者同步每次走一步，'
        '再次相遇处即为环入口（距 head 与距相遇点路程相等）。\n\n'
        '约束：链表中节点的数目范围在 [0, 10⁴] 内；-10⁵ ≤ Node.val ≤ 10⁵；'
        'pos 为 -1 或链表中的一个有效索引。',
        [
            '示例 1：head = [3,2,0,-4], pos = 1 → 返回 index 1 的节点',
            '示例 2：head = [1,2], pos = 0 → 返回 index 0 的节点',
            '示例 3：head = [1], pos = -1 → null',
        ],
        [
            '快慢指针同 has_cycle，寻找相遇点。',
            '相遇后 slow 重置为 head，fast 保持相遇点。',
            '两者同步每次走一步，再次相遇处即为环入口。',
            '若 fast 无法进入环（无相遇），返回 None。',
        ],
        '链表',
        code_notes=[
            'slow = fast = head — 快慢指针初始化。',
            'while fast and fast.next — 寻找相遇点。',
            'slow = slow.next; fast = fast.next.next',
            'if slow == fast — 相遇，进入第二阶段。',
            'slow = head — 一指针回 head。',
            'while slow != fast — 同步前进直至再次相遇。',
            'return slow — 环入口节点。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::merge_two_lists': _m(
        '21', '合并两个有序链表',
        '将两个升序链表合并为一个新的升序链表并返回。'
        '新链表是通过拼接给定的两个链表的所有节点组成的。\n\n'
        '双指针比较两链当前节点，较小者接到结果链尾部，'
        '一方耗尽后将另一方剩余直接接上。\n\n'
        '约束：两个链表的节点数目范围是 [0, 50]；-100 ≤ Node.val ≤ 100；'
        'l1 和 l2 均按非递减顺序排列。',
        [
            '示例 1：l1 = [1,2,4], l2 = [1,3,4] → [1,1,2,3,4,4]',
            '示例 2：l1 = [], l2 = [] → []',
            '示例 3：l1 = [], l2 = [0] → [0]',
        ],
        [
            'dummy 哑节点，cur 指向结果链尾部。',
            'while l1 和 l2 均非空：比较当前值，较小者接到 cur.next。',
            '对应链指针前进，cur 同步前进。',
            '一方耗尽后 cur.next = l1 or l2 接上剩余。',
        ],
        '链表',
        code_notes=[
            'dummy = ListNode(); cur = dummy — 结果链哑节点。',
            'while l1 and l2 — 两链均还有节点。',
            'if l1.val <= l2.val — 取较小者（相等时取 l1）。',
            'cur.next = l1; l1 = l1.next — 接入 l1 并前进。',
            'else: cur.next = l2; l2 = l2.next — 接入 l2 并前进。',
            'cur = cur.next — 尾指针前进。',
            'cur.next = l1 or l2 — 接上剩余段。',
        ],
        complexity='时间 O(m+n)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::merge_k_lists': _m(
        '23', '合并 K 个升序链表',
        '给你一个链表数组 lists，每个链表都已按升序排列。'
        '请你将所有链表合并到一个升序链表中，返回合并后的链表。\n\n'
        '本实现过滤空链后用 functools.reduce 依次两两 merge_two_lists；'
        '进阶可用分治或最小堆优化至 O(N log k)。\n\n'
        '约束：k == lists.length；0 ≤ k ≤ 10⁴；0 ≤ lists[i].length ≤ 500；'
        '-10⁴ ≤ lists[i][j] ≤ 10⁴；lists[i] 按升序排列；'
        'lists[i].length 的总和不超过 10⁴。',
        [
            '示例 1：lists = [[1,4,5],[1,3,4],[2,6]] → [1,1,2,3,4,4,5,6]',
            '示例 2：lists = [] → []',
            '示例 3：lists = [[]] → []',
        ],
        [
            '过滤掉所有空链表；若过滤后为空则返回 None。',
            '使用 reduce(merge_two_lists, lists) 链式两两合并。',
            '每次 merge 比较两链当前节点，较小者接入结果链尾部。',
            '一方耗尽后将另一方剩余段直接接上，保持升序。',
            '全部合并完成后返回 dummy.next 作为最终有序链表头。',
        ],
        '链表',
        code_notes=[
            'lists = [node for node in lists if node] — 过滤空链。',
            'if not lists: return None — 全空则返回 None。',
            'reduce(merge_two_lists, lists) — 从左到右依次两两合并。',
            'merge_two_lists 每次合并两条升序链 — 复用 LC21 逻辑。',
            '链式合并总复杂度 O(kN)，k 为链数、N 为总节点数。',
        ],
        complexity='时间 O(kN)（链式两两合并），空间 O(1) 额外空间。',
    ),
    'data_structures/linked_list/linked_list.py::insertion_sort_list': _m(
        '147', '对链表进行插入排序',
        '给定单个链表的头 head，使用插入排序对链表进行排序，并返回排序后链表的头。\n\n'
        '维护 dummy 作为已排序部分的头（val=-inf 便于比较），'
        '逐个取出原链节点，在已排序部分找插入位置后插入。\n\n'
        '约束：链表中节点的数目在 [0, 5000] 范围内；-5000 ≤ Node.val ≤ 5000。',
        [
            '示例 1：head = [4,2,1,3] → [1,2,3,4]',
            '示例 2：head = [-1,5,3,4,0] → [-1,0,3,4,5]',
        ],
        [
            'dummy 哑节点 val=-inf 作为已排序链头。',
            '逐个取出 head 节点，保存 nxt = head.next。',
            'prev 从 dummy 出发，找 prev.next.val < head.val 的最后一个位置。',
            'head.next = prev.next; prev.next = head 完成插入。',
            'head = nxt 继续处理下一节点。',
        ],
        '链表',
        code_notes=[
            'dummy = ListNode(float("-inf")) — 已排序链哑头，便于边界比较。',
            'nxt = head.next — 暂存下一待处理节点。',
            'prev = dummy — 在已排序链中找插入前驱。',
            'while prev.next and prev.next.val < head.val — 找插入位置。',
            'head.next = prev.next; prev.next = head — 插入当前节点。',
            'head = nxt — 处理原链下一节点。',
        ],
        complexity='时间 O(n²)，空间 O(1)。',
    ),
    'data_structures/linked_list/linked_list.py::merge': _m(
        '88', '合并两个有序数组',
        '给你两个按非递减顺序排列的整数数组 nums1 和 nums2，'
        '另有两个整数 m 和 n，分别表示 nums1 和 nums2 中元素的数目。\n\n'
        'nums1 的末尾有足够空间（大小为 m+n）存放 nums2 的元素。'
        '请你合并 nums2 到 nums1 中，使合并后的数组仍按非递减顺序排列。'
        '必须原地修改 nums1，不使用额外数组。\n\n'
        '约束：nums1.length == m + n；nums2.length == n；0 ≤ m, n ≤ 200；'
        '1 ≤ m + n ≤ 200；-10⁹ ≤ nums1[i], nums2[j] ≤ 10⁹。',
        [
            '示例 1：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 → [1,2,2,3,5,6]',
            '示例 2：nums1 = [1], m = 1, nums2 = [], n = 0 → [1]',
            '示例 3：nums1 = [0], m = 0, nums2 = [1], n = 1 → [1]',
        ],
        [
            '从 nums1 末尾空位 pos = m+n-1 开始向前填。',
            '比较 nums1[m-1] 与 nums2[n-1]，较大者写入 pos，对应指针前移。',
            'm 或 n 为 0 时只处理另一方剩余元素。',
            'nums2 若有剩余，拷贝到 nums1 前部；nums1 剩余部分已在正确位置。',
        ],
        '链表',
        code_notes=[
            'pos = m + n - 1 — 写入位置，从尾部空位开始。',
            'while m > 0 and n > 0 — 两数组均还有未合并元素。',
            'if nums1[m - 1] < nums2[n - 1] — 取较大者 nums2[n-1]。',
            'nums1[pos] = nums2[n - 1]; n -= 1 — 写入并前移 n。',
            'else: nums1[pos] = nums1[m - 1]; m -= 1 — 写入 nums1 较大者。',
            'pos -= 1 — 写入位置左移。',
            'while n > 0 — 拷贝 nums2 剩余元素。',
        ],
        complexity='时间 O(m+n)，空间 O(1)。',
    ),
    'data_structures/matrix/matrix.py::search_matrix': _m(
        '240', '搜索二维矩阵 II',
        '编写一个高效的算法来搜索 m×n 矩阵 matrix 中的一个目标值 target。'
        '该矩阵具有以下特性：每行的元素从左到右升序排列；'
        '每列的元素从上到下升序排列。\n\n'
        '从矩阵左下角出发：当前元素左侧更小、上方更大，'
        '可据此每次排除一行或一列，类似「楼梯」搜索。\n\n'
        '约束：m == matrix.length；n == matrix[i].length；'
        '1 ≤ n, m ≤ 300；-10⁹ ≤ matrix[i][j], target ≤ 10⁹。',
        [
            '示例 1：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5 → true',
            '示例 2：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20 → false',
        ],
        [
            '若 matrix 为空返回 False；row 初始为最后一行，col 为第 0 列。',
            'while row >= 0 且 col < 列数：比较 matrix[row][col] 与 target。',
            '相等则返回 True；大于 target 则 row--（排除当前行）；小于则 col++。',
            '越界仍未找到则返回 False。',
        ],
        '矩阵',
        code_notes=[
            'if not matrix: return False — 空矩阵边界。',
            'row, col = len(matrix) - 1, 0 — 从左下角出发。',
            'while row >= 0 and col < len(matrix[0]) — 在矩阵范围内搜索。',
            'if matrix[row][col] == target: return True — 找到目标。',
            'if matrix[row][col] > target: row -= 1 — 当前值过大，上移一行。',
            'else: col += 1 — 当前值过小，右移一列。',
            'return False — 搜索完毕未找到。',
        ],
        complexity='时间 O(m+n)，空间 O(1)。',
    ),
    'data_structures/matrix/matrix.py::set_zeroes': _m(
        '73', '矩阵置零',
        '给定一个 m×n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。'
        '请使用原地算法。\n\n'
        '第一遍扫描记录哪些行、列出现过 0；'
        '第二遍按标记将对应行列全部置 0。'
        '（进阶可用首行首列作标记实现 O(1) 额外空间。）\n\n'
        '约束：m == matrix.length；n == matrix[0].length；1 ≤ m, n ≤ 200；'
        '-2³¹ ≤ matrix[i][j] ≤ 2³¹ - 1。',
        [
            '示例 1：matrix = [[1,1,1],[1,0,1],[1,1,1]] → [[1,0,1],[0,0,0],[1,0,1]]',
            '示例 2：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]] → [[0,0,0,0],[0,4,5,0],[0,3,1,0]]',
        ],
        [
            '初始化 zero_rows、zero_cols 两个集合记录需置零的行列号。',
            '第一遍双重循环：遇 matrix[i][j]==0 则将 i 加入 zero_rows、j 加入 zero_cols。',
            '第二遍遍历 zero_rows，将对应行的每个元素置 0。',
            '第三遍遍历 zero_cols，将对应列的每个元素置 0。',
        ],
        '矩阵',
        code_notes=[
            'zero_rows, zero_cols = set(), set() — 记录需置零的行列。',
            'for i, row in enumerate(matrix) — 逐行扫描。',
            'if value == 0: zero_rows.add(i); zero_cols.add(j) — 标记行列。',
            'for i in zero_rows — 将标记行全部置 0。',
            'for j in zero_cols — 将标记列全部置 0。',
        ],
        complexity='时间 O(m×n)，空间 O(m+n)（集合存储行列号）。',
    ),
    'patterns/two_pointers/array.py::sorted_squares': _m(
        '977', '有序数组的平方',
        '给你一个按非递减顺序排序的整数数组 nums，'
        '返回每个数字的平方组成的新数组，要求也按非递减顺序排序。\n\n'
        '平方后最大值必在数组两端（负数平方可能很大），'
        '双指针从两端向中间比较平方值，降序收集后反转即得升序结果。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁴；-10⁴ ≤ nums[i] ≤ 10⁴；nums 按非递减顺序排序。',
        [
            '示例 1：nums = [-4,-1,0,3,10] → [0,1,9,16,100]',
            '示例 2：nums = [-7,-3,2,3,11] → [4,9,9,49,121]',
        ],
        [
            'left=0、right=len-1 双指针从两端出发。',
            '比较 nums[left]² 与 nums[right]²，较大者 append 到 result。',
            '对应指针向内移动，直到 left > right。',
            'return result[::-1] 反转得到升序平方数组。',
        ],
        '双指针',
        code_notes=[
            'left, right = 0, len(nums) - 1 — 双指针初始化。',
            'left_sq, right_sq = nums[left]**2, nums[right]**2 — 计算两端平方。',
            'if left_sq <= right_sq — 右端平方更大或相等。',
            'result.append(right_sq); right -= 1 — 取右端并右指针左移。',
            'else: result.append(left_sq); left += 1 — 取左端并左指针右移。',
            'return result[::-1] — 降序收集后反转为升序。',
        ],
        complexity='时间 O(n)，空间 O(n)（结果数组）。',
    ),
    'patterns/two_pointers/array.py::move_zeros': _m(
        '283', '移动零',
        '给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，'
        '同时保持非零元素的相对顺序。\n\n'
        '请注意必须在不复制数组的情况下原地操作。\n\n'
        'slow 指向下一个非零应写入的位置，fast 扫描全数组，'
        '遇非零则与 slow 交换并 slow++。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁴；-2³¹ ≤ nums[i] ≤ 2³¹ - 1。',
        [
            '示例 1：nums = [0,1,0,3,12] → [1,3,12,0,0]',
            '示例 2：nums = [0] → [0]',
        ],
        [
            'slow 初始为 0，表示非零区写入位置。',
            'fast 从 0 扫描至末尾。',
            '若 nums[fast] != 0，与 nums[slow] 交换并 slow++。',
            '0 自然被挤到数组尾部，非零相对顺序不变。',
        ],
        '双指针',
        code_notes=[
            'slow = 0 — 下一个非零写入位置。',
            'for fast in range(len(nums)) — fast 扫描全数组。',
            'if nums[fast] != 0 — 发现非零元素。',
            'nums[slow], nums[fast] = nums[fast], nums[slow] — 交换到 slow 位置。',
            'slow += 1 — 非零区扩大。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'patterns/two_pointers/array.py::remove_element': _m(
        '27', '移除元素',
        '给你一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，'
        '元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。\n\n'
        'slow/fast 双指针：fast 扫描，非 val 元素交换到 slow 位置。\n\n'
        '约束：0 ≤ nums.length ≤ 100；0 ≤ nums[i] ≤ 50；0 ≤ val ≤ 100。',
        [
            '示例 1：nums = [3,2,2,3], val = 3 → 2，nums 前 2 个元素为 [2,2]',
            '示例 2：nums = [0,1,2,2,3,0,4,2], val = 2 → 5，nums 前 5 个元素为 [0,1,4,0,3]',
        ],
        [
            'slow 指向下一个保留元素应写入的位置。',
            'fast 扫描整个数组。',
            'nums[fast] != val 时交换到 slow 并 slow++。',
            '返回 slow 即为新长度。',
        ],
        '双指针',
        code_notes=[
            'slow = 0 — 保留区写入指针。',
            'for fast in range(len(nums)) — 扫描每个元素。',
            'if nums[fast] != val — 非目标值保留。',
            'nums[slow], nums[fast] = nums[fast], nums[slow] — 交换到保留区。',
            'slow += 1 — 保留区扩大。',
            'return slow — 新数组长度。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'patterns/two_pointers/array.py::remove_duplicates': _m(
        '26', '删除有序数组中的重复项',
        '给你一个非严格递增排列的数组 nums，请你原地删除重复出现的元素，'
        '使每个元素只出现一次，返回删除后数组的新长度。\n\n'
        'slow 指向已去重段末尾，fast 扫描；遇新值则 slow++ 并写入。\n\n'
        '约束：1 ≤ nums.length ≤ 3×10⁴；-100 ≤ nums[i] ≤ 100；nums 已按非严格递增排列。',
        [
            '示例 1：nums = [1,1,2] → 2，nums 前 2 个元素为 [1,2]',
            '示例 2：nums = [0,0,1,1,1,2,2,3,3,4] → 5，nums 前 5 个元素为 [0,1,2,3,4]',
        ],
        [
            '若 nums 为空返回 0；slow 初始为 0。',
            'fast 从 1 扫描至末尾。',
            '若 nums[fast] != nums[slow]，说明出现新值：slow++ 并 nums[slow] = nums[fast]。',
            '返回 slow+1 为新长度。',
        ],
        '双指针',
        code_notes=[
            'if not nums: return 0 — 空数组边界。',
            'slow = 0 — 已去重段最后一个元素下标。',
            'for fast in range(1, len(nums)) — 从第二个元素开始扫描。',
            'if nums[fast] != nums[slow] — 发现新值。',
            'slow += 1; nums[slow] = nums[fast] — 写入去重段。',
            'return slow + 1 — 新长度。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'patterns/two_pointers/array.py::remove_duplicates_allow_twice': _m(
        '80', '删除有序数组中的重复项 II',
        '给你一个有序数组 nums，请你原地删除重复出现的元素，'
        '使得出现次数超过两次的元素只出现两次，返回删除后数组的新长度。\n\n'
        'write 为写入指针；当前元素与 nums[write-2] 比较，'
        '不同则说明未超过两次，可写入。\n\n'
        '约束：1 ≤ nums.length ≤ 3×10⁴；-10⁴ ≤ nums[i] ≤ 10⁴；nums 已按非严格递增排列。',
        [
            '示例 1：nums = [1,1,1,2,2,3] → 5，nums 前 5 个元素为 [1,1,2,2,3]',
            '示例 2：nums = [0,0,1,1,1,1,2,3,3] → 7，nums 前 7 个元素为 [0,0,1,1,2,3,3]',
        ],
        [
            'write 初始为 0，遍历每个 num。',
            '若 write < 2（前两位直接写）或 num != nums[write-2]，则写入并 write++。',
            'write-2 保证同一值最多保留两个。',
            '返回 write 为新长度。',
        ],
        '双指针',
        code_notes=[
            'write = 0 — 写入指针。',
            'for num in nums — 遍历每个元素。',
            'if write < 2 — 前两位无条件写入。',
            'or num != nums[write - 2] — 与倒数第二个比较，不同则可写。',
            'nums[write] = num; write += 1 — 写入并前进。',
            'return write — 新长度。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'patterns/two_pointers/array.py::sort_colors': _m(
        '75', '颜色分类',
        '给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums，'
        '原地对它们进行排序，使得相同颜色的元素相邻，'
        '并按照红色、白色、蓝色顺序排列。\n\n'
        '用 0/1/2 表示三种颜色。本实现分两遍：'
        '第一遍把 0 交换到前面，第二遍把 1 交换到 0 区后面。\n\n'
        '约束：n == nums.length；1 ≤ n ≤ 300；nums[i] 为 0、1 或 2。',
        [
            '示例 1：nums = [2,0,2,1,1,0] → [0,0,1,1,2,2]',
            '示例 2：nums = [2,0,1] → [0,1,2]',
        ],
        [
            'write 初始为 0，表示下一个颜色块应写入的位置。',
            '第一遍：write 标记 0 区末尾，遇 0 则与 write 交换并 write++。',
            '第二遍：从 write 开始扫描，遇 1 则与 write 交换并 write++。',
            'write 之后剩余位置自然为 2，数组完成 0→1→2 排序。',
        ],
        '双指针',
        code_notes=[
            'write = 0 — 当前颜色区写入位置。',
            '第一遍 for i in range(len(nums)) — 处理 0。',
            'if nums[i] == 0: nums[i], nums[write] = nums[write], nums[i]; write += 1',
            '第二遍 for i in range(write, len(nums)) — 在 0 区之后处理 1。',
            'if nums[i] == 1 — 交换到 write 位置并 write++。',
            '两遍结束后剩余为 2。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'patterns/two_pointers/array.py::max_area': _m(
        '11', '盛最多水的容器',
        '给定一个长度为 n 的整数数组 height，有 n 条垂线，'
        '第 i 条线的两个端点是 (i, 0) 和 (i, height[i])。\n\n'
        '找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。'
        '返回容器可以储存的最大水量。\n\n'
        '约束：n == height.length；2 ≤ n ≤ 10⁵；0 ≤ height[i] ≤ 10⁴。',
        [
            '示例 1：height = [1,8,6,2,5,4,8,3,7] → 49',
            '示例 2：height = [1,1] → 1',
        ],
        [
            'left=0、right=n-1 双指针在两端。',
            '面积 = min(height[left], height[right]) × (right-left)，更新 best。',
            '移动较短一侧（只有提高短板才可能增大面积）。',
            'left < right 时循环直至相遇。',
        ],
        '双指针',
        code_notes=[
            'left, right = 0, len(height) - 1 — 双指针初始化。',
            'best = 0 — 最大面积。',
            'width = right - left — 当前宽度。',
            'h = min(height[left], height[right]) — 短板高度。',
            'best = max(best, h * width) — 更新最优。',
            'if height[left] <= height[right]: left += 1 else: right -= 1 — 移动短板。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'patterns/two_pointers/array.py::three_sum': _m(
        '15', '三数之和',
        '给你一个整数数组 nums，判断是否存在三元组 [nums[i], nums[j], nums[k]]'
        '满足 i != j、i != k 且 j != k，同时还满足 nums[i] + nums[j] + nums[k] == 0。'
        '请你返回所有和为 0 且不重复的三元组。\n\n'
        '先排序，固定 anchor 后在剩余区间用双指针找两数之和 = -anchor。\n\n'
        '约束：3 ≤ nums.length ≤ 3000；-10⁵ ≤ nums[i] ≤ 10⁵。',
        [
            '示例 1：nums = [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]',
            '示例 2：nums = [0,1,1] → []',
            '示例 3：nums = [0,0,0] → [[0,0,0]]',
        ],
        [
            'nums.sort() 升序排列。',
            '固定 i 的 anchor = nums[i]；anchor > 0 时可直接 break。',
            '同层去重：i > 0 且 anchor == nums[i-1] 时 skip。',
            '双指针 left=i+1、right=n-1 找 total = anchor + nums[left] + nums[right]。',
            'total==0 收集答案并跳过重复 left/right；total<0 则 left++，否则 right--。',
        ],
        '双指针',
        code_notes=[
            'nums.sort() — 排序便于双指针与去重。',
            'if anchor > 0: break — 最小值已正，不可能和为 0。',
            'if i > 0 and anchor == nums[i - 1]: continue — 同层去重。',
            'left, right = i + 1, len(nums) - 1 — 双指针区间。',
            'total == 0 时 result.append 并跳过重复 left/right。',
            'total < 0: left += 1; else: right -= 1 — 调整总和。',
        ],
        complexity='时间 O(n²)，空间 O(log n)（排序栈空间，不计结果）。',
    ),
    'patterns/two_pointers/array.py::four_sum': _m(
        '18', '四数之和',
        '给你一个由 n 个整数组成的数组 nums，和一个目标值 target。'
        '请你找出并返回满足下述全部条件且不重复的四元组 '
        '[nums[a], nums[b], nums[c], nums[d]]（a、b、c、d 互不相同）：'
        'nums[a] + nums[b] + nums[c] + nums[d] == target。\n\n'
        '排序后两重循环固定前两个数，内层双指针找后两个数。\n\n'
        '约束：1 ≤ nums.length ≤ 200；-10⁹ ≤ nums[i] ≤ 10⁹；-10⁹ ≤ target ≤ 10⁹。',
        [
            '示例 1：nums = [1,0,-1,0,-2,2], target = 0 → [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]',
            '示例 2：nums = [2,2,2,2,2], target = 8 → [[2,2,2,2]]',
        ],
        [
            'nums.sort()；两重循环固定 nums[i]、nums[j]。',
            'i、j 层分别同层去重；nums[i]+nums[j] 过大且 target>0 时可 break。',
            'left=j+1、right=n-1 双指针找四数之和 = target。',
            '找到时收集并跳过重复 left/right；否则移动指针调整总和。',
        ],
        '双指针',
        code_notes=[
            'nums.sort(); n = len(nums) — 排序与长度。',
            'i 层：if nums[i] > target and target > 0: break — 剪枝。',
            'if i > 0 and nums[i] == nums[i - 1]: continue — i 层去重。',
            'j 层：if nums[i] + nums[j] > target and target > 0: break。',
            'if j > i + 1 and nums[j] == nums[j - 1]: continue — j 层去重。',
            'left, right = j + 1, n - 1 — 内层双指针。',
            'total == target 时收集并跳过重复 left/right。',
        ],
        complexity='时间 O(n³)，空间 O(log n)（排序）。',
    ),
    'patterns/two_pointers/array.py::triangle_number': _m(
        '611', '有效三角形的个数',
        '给定一个包含非负整数的数组 nums，返回其中可以组成三角形三条边的三元组个数。\n\n'
        '三角形条件：任意两边之和大于第三边。排序后固定最短边 nums[i]，'
        '双指针 k 维护第三边上界，统计合法组合数。\n\n'
        '约束：1 ≤ nums.length ≤ 1000；0 ≤ nums[i] ≤ 1000。',
        [
            '示例 1：nums = [2,2,3,4] → 3（三元组 (2,3,4) 以不同下标出现 3 次）',
            '示例 2：nums = [4,2,3,4] → 4',
        ],
        [
            'nums.sort()；固定最短边 i，跳过 nums[i]==0。',
            'k 初始为 i+2；对每条边 j（j > i），扩展 k 使 nums[i]+nums[j] > nums[k]。',
            '以 i、j 为两条边的合法第三边个数为 k-j-1，累加到 count。',
            'j 递增时 k 单调不减，均摊 O(n)。',
        ],
        '双指针',
        code_notes=[
            'nums.sort() — 排序便于固定最短边。',
            'if nums[i] == 0: continue — 零边无法构成三角形。',
            'k = i + 2 — 第三边指针初始位置。',
            'for j in range(i + 1, len(nums) - 1) — 固定第二条边。',
            'while k < len(nums) and nums[i] + nums[j] > nums[k]: k += 1 — 扩展 k。',
            'count += k - j - 1 — 累加合法第三边数量。',
        ],
        complexity='时间 O(n²)，空间 O(log n)（排序）。',
    ),
    'patterns/sliding_window/window.py::min_sub_array_len': _m(
        '209', '长度最小的子数组',
        '给定一个含有 n 个正整数的数组和一个正整数 target，'
        '找出该数组中满足其总和大于等于 target 的长度最小的连续子数组 '
        '[nums_l, nums_l+1, ..., nums_r-1, nums_r]，并返回其长度。'
        '如果不存在符合条件的子数组，返回 0。\n\n'
        '滑动窗口：右指针扩展累加 window_sum，'
        '当 sum >= target 时左指针收缩求最短长度。\n\n'
        '约束：1 ≤ target ≤ 10⁹；1 ≤ nums.length ≤ 10⁵；1 ≤ nums[i] ≤ 10⁴。',
        [
            '示例 1：target = 7, nums = [2,3,1,2,4,3] → 2，子数组 [4,3]',
            '示例 2：target = 4, nums = [1,4,4] → 1',
            '示例 3：target = 11, nums = [1,1,1,1,1,1,1,1] → 0',
        ],
        [
            'left=0，window_sum=0，min_len=inf。',
            'right 遍历 nums，window_sum += nums[right] 扩展窗口。',
            'while window_sum >= target：更新 min_len，减去 nums[left] 并 left++ 收缩。',
            '若 min_len 仍为 inf 返回 0，否则返回 min_len。',
        ],
        '滑动窗口',
        code_notes=[
            'left = 0; window_sum = 0; min_len = float("inf") — 窗口状态。',
            'for right, value in enumerate(nums) — 右指针扩展。',
            'window_sum += value — 累加当前元素。',
            'while window_sum >= target — 窗口满足条件时收缩。',
            'min_len = min(min_len, right - left + 1) — 更新最短长度。',
            'window_sum -= nums[left]; left += 1 — 左边界右移。',
            'return 0 if min_len == float("inf") else min_len — 无解返回 0。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'patterns/sliding_window/window.py::character_replacement': _m(
        '424', '替换后的最长重复字符',
        '给你一个字符串 s 和一个整数 k。'
        '你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。'
        '该操作最多可执行 k 次。\n\n'
        '在执行上述操作后，返回包含相同字母的最长子字符串的长度。\n\n'
        '枚举目标字符 A-Z，对每个 ch 用滑动窗口求最多替换 k 次的最长子串。\n\n'
        '约束：1 ≤ s.length ≤ 10⁵；s 仅由大写英文字母组成；0 ≤ k ≤ s.length。',
        [
            '示例 1：s = "ABAB", k = 2 → 4，替换后全为 "A" 或 "B"',
            '示例 2：s = "AABABBA", k = 1 → 4，替换一个 "B" 得 "AAAA"',
        ],
        [
            '枚举 26 个大写字母作为目标字符 ch。',
            '滑动窗口 [left, right]：replacements 记录窗口内非 ch 字符个数。',
            'replacements > k 时 left 右移缩小窗口。',
            '窗口合法时更新 best；26 次枚举取最大值。',
        ],
        '滑动窗口',
        code_notes=[
            'for code in range(26): ch = chr(ord("A") + code) — 枚举目标字符。',
            'left = replacements = 0 — 窗口左边界与非目标字符计数。',
            'for right, cur in enumerate(s) — 右指针扩展。',
            'replacements += cur != ch — 非目标字符计入替换次数。',
            'while replacements > k — 窗口非法，收缩左边界。',
            'replacements -= s[left] != ch; left += 1',
            'best = max(best, right - left + 1) — 更新最长合法窗口。',
        ],
        complexity='时间 O(26×n) = O(n)，空间 O(1)。',
    ),
    'patterns/sliding_window/window.py::minimum_recolors': _m(
        '2379', '得到 K 个黑块的最少涂色次数',
        '给你一个长度为 n 下标从 0 开始的字符串 blocks，'
        'blocks[i] 要么是 "W" 要么是 "B"，分别表示白色和黑色色块。'
        '给你一个整数 k，表示想要连续黑色色块的数目。\n\n'
        '每一次操作中，可以选择某个白色色块将其涂成黑色。'
        '返回得到 k 个连续黑色色块需要的最少操作次数。\n\n'
        '约束：n == blocks.length；1 ≤ n ≤ 100；blocks[i] 为 "W" 或 "B"；1 ≤ k ≤ n。',
        [
            '示例 1：blocks = "WBBWWBBWBW", k = 7 → 3',
            '示例 2：blocks = "WBWBBBW", k = 2 → 0',
        ],
        [
            '固定窗口长度 k，white 记录窗口内 "W" 个数（即需涂色次数）。',
            '初始化第一个窗口的 white，best = white。',
            '窗口右移：加入 blocks[i+k]，移除 blocks[i]，更新 white 和 best。',
            '返回 best 即为最少涂色次数。',
        ],
        '滑动窗口',
        code_notes=[
            'white = sum(block == "W" for block in blocks[:k]) — 首窗口白块数。',
            'best = white — 最少涂色次数。',
            'for i in range(len(blocks) - k) — 窗口右移。',
            'if blocks[i + k] == "W": white += 1 — 新入窗口白块。',
            'if blocks[i] == "W": white -= 1 — 出窗口白块。',
            'best = min(best, white) — 更新最优。',
        ],
        complexity='时间 O(n)，空间 O(1)。',
    ),
    'patterns/prefix_sum/prefix.py::sub_array_sum': _m(
        '560', '和为 K 的子数组',
        '给你一个整数数组 nums 和一个整数 k，'
        '请你统计该数组中和为 k 的子数组的个数。\n\n'
        '子数组是数组中元素的连续非空序列。\n\n'
        '前缀和 + 哈希：子数组 nums[j+1..i] 和为 k 当且仅当 prefix[i] - prefix[j] = k，'
        '即统计有多少 j 满足 prefix[j] = prefix[i] - k。\n\n'
        '约束：1 ≤ nums.length ≤ 2×10⁴；-1000 ≤ nums[i] ≤ 1000；-10⁷ ≤ k ≤ 10⁷。',
        [
            '示例 1：nums = [1,1,1], k = 2 → 2',
            '示例 2：nums = [1,2,3], k = 3 → 2，子数组 [1,2] 和 [3]',
        ],
        [
            'prefix_count 哈希表记录各前缀和出现次数，初始化 {0: 1}。',
            '遍历累加 acc，将 prefix_count 中 acc-k 的出现次数累加到 count。',
            '更新 prefix_count[acc] += 1。',
            '返回 count。',
        ],
        '前缀和',
        code_notes=[
            'prefix_count = {0: 1} — 空前缀，便于统计从下标 0 开始的子数组。',
            'acc = count = 0 — 当前前缀和与答案。',
            'for num in nums: acc += num — 累加前缀和。',
            'count += prefix_count.get(acc - k, 0) — 统计满足条件的先前前缀。',
            'prefix_count[acc] = prefix_count.get(acc, 0) + 1 — 更新频次。',
        ],
        complexity='时间 O(n)，空间 O(n)。',
    ),
    'patterns/prefix_sum/prefix.py::find_max_length': _m(
        '525', '连续数组',
        '给定一个二进制数组 nums，找到含有相同数量的 0 和 1 的最长连续子数组，'
        '并返回该子数组的长度。\n\n'
        '将 0 映射为 -1、1 映射为 +1，问题转化为求和为 0 的最长子数组。'
        'first_index 记录每种前缀和最早出现位置以最大化长度。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁵；nums[i] 为 0 或 1。',
        [
            '示例 1：nums = [0,1] → 2',
            '示例 2：nums = [0,1,0] → 2',
        ],
        [
            'transformed 将 0→-1、1→+1；first_index[0]=-1 表示空前缀。',
            '遍历累加 acc；若 acc 已出现过，更新 best = max(best, i - first_index[acc])。',
            '否则 first_index[acc] = i 记录最早位置。',
            '返回 best。',
        ],
        '前缀和',
        code_notes=[
            'transformed = [1 if x == 1 else -1 for x in nums] — 0/1 转 ±1。',
            'first_index = {0: -1} — 空前缀下标 -1。',
            'acc = best = 0 — 前缀和与最长长度。',
            'acc += value — 累加当前元素。',
            'if acc in first_index: best = max(best, i - first_index[acc]) — 更新最长。',
            'else: first_index[acc] = i — 只记录最早出现位置。',
        ],
        complexity='时间 O(n)，空间 O(n)。',
    ),
    'patterns/prefix_sum/prefix.py::contains_nearby_duplicate': _m(
        '219', '存在重复元素 II',
        '给你一个整数数组 nums 和一个整数 k，'
        '判断数组中是否存在不同的两个下标 i 和 j，'
        '使得 nums[i] == nums[j] 且 abs(i - j) <= k。\n\n'
        '哈希表记录每个值最近出现的下标，'
        '扫描时若发现同值且距离 ≤ k 则立即返回 True。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁵；-10⁹ ≤ nums[i] ≤ 10⁹；0 ≤ k ≤ 10⁵。',
        [
            '示例 1：nums = [1,2,3,1], k = 3 → true，下标 0 与 3',
            '示例 2：nums = [1,0,1,1], k = 1 → true',
            '示例 3：nums = [1,2,3,1,2,3], k = 2 → false',
        ],
        [
            'last_index 字典记录每个值最近一次出现的下标。',
            '从左到右扫描：若 value 已存在且 index - last_index[value] <= k，返回 True。',
            '否则更新 last_index[value] = index。',
            '扫完返回 False。',
        ],
        '哈希表',
        code_notes=[
            'last_index: dict[int, int] — 数值 → 最近下标。',
            'for index, value in enumerate(nums) — 顺序扫描。',
            'if value in last_index — 该值之前出现过。',
            'index - last_index[value] <= k — 两次出现足够近。',
            'return True — 找到满足条件的配对。',
            'last_index[value] = index — 更新最近位置。',
        ],
        complexity='时间 O(n)，空间 O(n)。',
    ),
    'patterns/prefix_sum/min_subarray_divisible_by_p.py::min_sub_array': _m(
        '1590', '使数组和能被 P 整除的最短子数组',
        '给你一个正整数数组 nums，请你移除最短子数组（可以为空），'
        '使得剩余元素的和被 p 整除。不允许将整个数组都移除。\n\n'
        '返回需要移除的最短子数组的长度，如果无法满足则返回 -1。\n\n'
        '设 x = sum(nums) % p；删除子数组 b 后剩余和能被 p 整除 ⟺ sum(b) % p == x。'
        '转化为找最短连续子数组，其前缀和模 p 等于 x。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁵；1 ≤ nums[i] ≤ 10⁹；1 ≤ p ≤ 10⁹。',
        [
            '示例 1：nums = [3,1,4,2], p = 6 → 1，移除 [4]',
            '示例 2：nums = [6,3,5,2], p = 9 → 2，移除 [5,2]',
            '示例 3：nums = [1,2,3], p = 3 → 0，无需移除',
        ],
        [
            'x = sum(nums) % p；若 x == 0 直接返回 0。',
            'mapping 记录各前缀和模 p 最后出现的下标，初始化 {0: -1}。',
            '遍历累加 y = (y + value) % p。',
            '若 (y - x) % p 在 mapping 中，更新 res = min(res, index - mapping[(y-x)%p])。',
            'mapping[y] = index；若 res >= n 返回 -1，否则返回 res。',
        ],
        '前缀和',
        code_notes=[
            'x = sum(nums) % p — 需删除子数组的和模 p。',
            'if x == 0: return 0 — 已整除无需删除。',
            'mapping = {0: -1}; y = 0 — 前缀模 p 的最后下标。',
            'y = (y + value) % p — 累加当前前缀模 p。',
            'if (y - x) % p in mapping — 存在前缀使中间子数组模 p 为 x。',
            'res = min(res, index - mapping[(y - x) % p]) — 更新最短长度。',
            'mapping[y] = index — 更新前缀最后位置。',
        ],
        complexity='时间 O(n)，空间 O(min(n, p))。',
    ),
    'patterns/monotonic_stack.py::daily_temperatures': _m(
        '739', '每日温度',
        '给定一个整数数组 temperatures，表示每天的温度，'
        '返回一个数组 answer，其中 answer[i] 是指对于第 i 天，'
        '下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 代替。\n\n'
        '单调递减栈存下标：当前温度高于栈顶对应温度时，'
        '栈顶元素找到了下一个更高温，弹出并计算天数差。\n\n'
        '约束：1 ≤ temperatures.length ≤ 10⁵；30 ≤ temperatures[i] ≤ 100。',
        [
            '示例 1：temperatures = [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]',
            '示例 2：temperatures = [30,40,50,60] → [1,1,1,0]',
            '示例 3：temperatures = [30,60,90] → [1,1,0]',
        ],
        [
            'answer 初始全 0；stack 存待找更高温的下标。',
            '遍历 i 和 temp：while 栈非空且 temp > temperatures[stack[-1]]，弹出 prev。',
            'answer[prev] = i - prev 记录等待天数。',
            '将 i 压入栈。',
        ],
        '单调栈',
        code_notes=[
            'answer = [0] * len(temperatures) — 结果数组。',
            'stack: list[int] — 单调递减栈，存下标。',
            'while stack and temp > temperatures[stack[-1]] — 当前温度更高。',
            'prev = stack.pop() — 栈顶找到下一个更高温。',
            'answer[prev] = i - prev — 等待天数。',
            'stack.append(i) — 当前下标入栈。',
        ],
        complexity='时间 O(n)，空间 O(n)。',
    ),
    'patterns/monotonic_stack.py::next_greater_element': _m(
        '496', '下一个更大元素 I',
        'nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置右侧的'
        '第一个比 x 大的元素。给你两个没有重复元素的数组 nums1 和 nums2，'
        '其中 nums1 是 nums2 的子集。\n\n'
        '请你找出 nums1 中每个元素在 nums2 中的下一个更大元素。\n\n'
        '约束：1 ≤ nums1.length ≤ nums2.length ≤ 1000；'
        '0 ≤ nums1[i], nums2[i] ≤ 10⁴；nums1 和 nums2 中所有整数互不相同；'
        'nums2 中的元素都出现在 nums1 中。',
        [
            '示例 1：nums1 = [4,1,2], nums2 = [1,3,4,2] → [-1,3,-1]',
            '示例 2：nums1 = [2,4], nums2 = [1,2,3,4] → [3,-1]',
        ],
        [
            '对 nums2 用单调栈预处理 next_greater 数组。',
            'index_of 记录 nums2 中各值的下标。',
            '遍历 nums2：栈顶值小于当前 value 时弹出并更新 next_greater。',
            '按 nums1 顺序查 next_greater 返回结果。',
        ],
        '单调栈',
        code_notes=[
            'next_greater = [-1] * len(nums2) — 初始无更大元素。',
            'index_of = {value: index for ...} — 值到下标映射。',
            'while stack and value > stack[-1] — 当前值更大。',
            'next_greater[index_of[stack.pop()]] = value — 更新栈顶答案。',
            'stack.append(value) — 当前值入栈。',
            'return [next_greater[index_of[value]] for value in nums1]',
        ],
        complexity='时间 O(n+m)，空间 O(n+m)。',
    ),
    'patterns/monotonic_stack.py::next_greater_elements_circular': _m(
        '503', '下一个更大元素 II',
        '给定一个循环数组 nums，返回 nums 中每个元素的下一个更大元素。'
        '数字 x 的下一个更大元素是按数组遍历顺序，'
        '这个数字后面第一个比它更大的数，否则输出 -1。\n\n'
        '将数组遍历两遍（2×n）模拟循环，单调栈存下标。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁴；-10⁹ ≤ nums[i] ≤ 10⁹。',
        [
            '示例 1：nums = [1,2,1] → [2,-1,2]',
            '示例 2：nums = [1,2,3,4,3] → [2,3,4,-1,4]',
        ],
        [
            'answer 初始全 -1；stack 存下标。',
            '遍历 i 从 0 到 2n-1，value = nums[i % n]。',
            'while 栈非空且 value > nums[stack[-1]]，弹出并更新 answer。',
            '仅 i < n 时将 i 压栈（避免重复入栈）。',
        ],
        '单调栈',
        code_notes=[
            'answer = [-1] * len(nums) — 结果数组。',
            'for i in range(2 * len(nums)) — 模拟循环遍历两遍。',
            'value = nums[i % len(nums)] — 当前元素值。',
            'while stack and value > nums[stack[-1]] — 找到更大元素。',
            'answer[stack.pop()] = value — 更新栈顶答案。',
            'if i < len(nums): stack.append(i) — 第一遍才入栈。',
        ],
        complexity='时间 O(n)，空间 O(n)。',
    ),
    'patterns/monotonic_stack.py::trap_rain_water': _m(
        '42', '接雨水',
        '给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，'
        '计算按排列之后，该图能接的雨水总量。\n\n'
        '单调栈维护递增柱高下标：当前柱高于栈顶时弹出 bottom，'
        '若栈仍非空则计算以 bottom 为底的积水矩形。\n\n'
        '约束：n == height.length；1 ≤ n ≤ 2×10⁴；0 ≤ height[i] ≤ 10⁵。',
        [
            '示例 1：height = [0,1,0,2,1,0,1,3,2,1,2,1] → 6',
            '示例 2：height = [4,2,0,3,2,5] → 9',
        ],
        [
            'stack 初始 [0]；从 i=1 遍历 height。',
            'while 栈非空且 height[i] > height[stack[-1]]：弹出 bottom。',
            '若栈仍非空，h = min(左右墙) - height[bottom]，w = i - stack[-1] - 1，累加 water。',
            '将 i 压入栈。',
        ],
        '单调栈',
        code_notes=[
            'stack = [0]; water = 0 — 栈存柱下标，初始第一柱。',
            'for i in range(1, len(height)) — 从第二柱开始。',
            'while stack and height[i] > height[stack[-1]] — 当前柱更高。',
            'bottom = stack.pop() — 弹出较低柱作为槽底。',
            'if stack: h = min(height[stack[-1]], height[i]) - height[bottom]',
            'w = i - stack[-1] - 1; water += h * w — 累加积水。',
            'stack.append(i) — 当前柱入栈。',
        ],
        complexity='时间 O(n)，空间 O(n)。',
    ),
    'patterns/monotonic_stack.py::largest_rectangle_area': _m(
        '84', '柱状图中最大的矩形',
        '给定 n 个非负整数，用来表示柱状图中各个柱子的高度。'
        '每个柱子彼此相邻，且宽度为 1。\n\n'
        '求在该柱状图中，能够勾勒出来的矩形的最大面积。\n\n'
        '单调递增栈存下标；当前柱低于栈顶时弹出计算以弹出柱为高的矩形面积。\n\n'
        '约束：1 ≤ heights.length ≤ 10⁵；0 ≤ heights[i] ≤ 10⁴。',
        [
            '示例 1：heights = [2,1,5,6,2,3] → 10',
            '示例 2：heights = [2,4] → 4',
        ],
        [
            'padded = [0, *heights, 0] 首尾补 0 便于清空栈。',
            'stack 初始 [0]；遍历 i 从 1 到 len(padded)-1。',
            'while padded[i] < padded[stack[-1]]：弹出 height，width = i - stack[-1] - 1，更新 best。',
            '将 i 压栈。',
        ],
        '单调栈',
        code_notes=[
            'padded = [0, *heights, 0] — 哨兵确保栈清空。',
            'stack = [0]; best = 0 — 单调递增栈与最大面积。',
            'while stack and padded[i] < padded[stack[-1]] — 当前柱更低，弹出计算。',
            'height = padded[stack.pop()] — 弹出柱高度。',
            'width = i - stack[-1] - 1 — 矩形宽度。',
            'best = max(best, height * width) — 更新最大面积。',
            'stack.append(i) — 当前下标入栈。',
        ],
        complexity='时间 O(n)，空间 O(n)。',
    ),
    'patterns/monotonic_stack.py::find132pattern': _m(
        '456', '132 模式',
        '给你一个 n 个整数的数组 nums，检查是否存在下标 (i, j, k)，'
        '满足 i < j < k 且 nums[i] < nums[k] < nums[j]（132 模式）。\n\n'
        '从右向左扫描，stack 维护递减序列，second 记录已见过的「中间大值」。'
        '若当前 value < second 则存在 132 模式。\n\n'
        '约束：n == nums.length；1 ≤ n ≤ 2×10⁵；-10⁹ ≤ nums[i] ≤ 10⁹。',
        [
            '示例 1：nums = [3,1,4,2] → true，(0,2,3) 即 1<2<4',
            '示例 2：nums = [1,2,3,4] → false',
        ],
        [
            '从右向左遍历 value。',
            '若 value < second，说明找到 132 模式，返回 True。',
            'while 栈非空且 value > stack[-1]，弹出更新 second = stack.pop()。',
            '将 value 压入栈。',
            '遍历结束返回 False。',
        ],
        '单调栈',
        code_notes=[
            'stack: list[int] = []; second = float("-inf") — 递减栈与次大值。',
            'for value in reversed(nums) — 从右向左扫描。',
            'if value < second: return True — 找到 132 模式。',
            'while stack and value > stack[-1] — 维护递减栈。',
            'second = stack.pop() — 更新中间大值候选。',
            'stack.append(value) — 当前值入栈。',
        ],
        complexity='时间 O(n)，空间 O(n)。',
    ),
    'patterns/binary_search/basic.py::binary_search': _m(
        '704', '二分查找',
        '给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target，'
        '写一个函数搜索 nums 中的 target，如果目标存在返回下标，否则返回 -1。\n\n'
        '本实现采用左闭右开区间 [left, right)，'
        'mid 与 target 比较后收缩左边界或右边界。\n\n'
        '约束：1 ≤ nums.length ≤ 10⁴；-10⁴ < nums[i], target < 10⁴；nums 按升序排列。',
        [
            '示例 1：nums = [-1,0,3,5,9,12], target = 9 → 4',
            '示例 2：nums = [-1,0,3,5,9,12], target = 2 → -1',
        ],
        [
            'left=0, right=len(nums)，循环条件 left < right。',
            'mid = (left + right) // 2。',
            'nums[mid] > target 则 right = mid；nums[mid] < target 则 left = mid + 1。',
            '相等返回 mid；循环结束返回 -1。',
        ],
        '二分查找',
        code_notes=[
            'left, right = 0, len(nums) — 左闭右开区间。',
            'while left < right — 区间非空继续搜索。',
            'mid = (left + right) // 2 — 中点下标。',
            'if nums[mid] > target: right = mid — 收缩右边界。',
            'elif nums[mid] < target: left = mid + 1 — 收缩左边界。',
            'else: return mid — 找到目标。',
            'return -1 — 未找到。',
        ],
        complexity='时间 O(log n)，空间 O(1)。',
    ),
    'patterns/binary_search/basic.py::find_min_in_rotated_array': _m(
        '153', '寻找旋转排序数组中的最小值',
        '已知一个长度为 n 的数组，预先按照升序排列，'
        '经由 1 到 n 次旋转后，得到输入数组。'
        '例如，原数组 nums = [0,1,2,4,5,6,7] 旋转 4 次得到 [4,5,6,7,0,1,2]。'
        '给你一个元素值互不相同的数组 nums，它原来是一个升序排列的数组，'
        '请找出数组中的最小元素。\n\n'
        '约束：n == nums.length；1 ≤ n ≤ 5000；-5000 ≤ nums[i] ≤ 5000；'
        'nums 按升序排列后旋转；nums 中的所有整数互不相同。',
        [
            '示例 1：nums = [3,4,5,1,2] → 1',
            '示例 2：nums = [4,5,6,7,0,1,2] → 0',
            '示例 3：nums = [11,13,15,17] → 11',
        ],
        [
            'left=0, right=n-1；若 nums[left] < nums[right] 说明已有序，返回 nums[left]。',
            'mid = (left+right)//2；比较 nums[mid] 与 nums[right]。',
            'nums[mid] > nums[right] 说明最小值在右半，left = mid + 1。',
            '否则最小值在左半含 mid，right = mid。',
            '返回 nums[left]。',
        ],
        '二分查找',
        code_notes=[
            'left, right = 0, len(nums) - 1 — 闭区间二分。',
            'if nums[left] < nums[right]: return nums[left] — 未旋转直接返回。',
            'mid = (left + right) // 2 — 中点。',
            'if nums[mid] > nums[right]: left = mid + 1 — 最小值在右半。',
            'else: right = mid — 最小值在左半含 mid。',
            'return nums[left] — 收敛到最小值。',
        ],
        complexity='时间 O(log n)，空间 O(1)。',
    ),
    'patterns/binary_search/basic.py::kth_smallest_in_matrix': _m(
        '378', '有序矩阵中第 K 小的元素',
        '给你一个 n×n 矩阵 matrix，其中每行和每列元素均按升序排序，'
        '找到矩阵中第 k 小的元素。\n\n'
        '请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。\n\n'
        '对值域 [matrix[0][0], matrix[-1][-1]] 二分，'
        'count_le(mid) 统计矩阵中 ≤ mid 的元素个数。\n\n'
        '约束：n == matrix.length == matrix[i].length；1 ≤ n ≤ 300；'
        '-10⁹ ≤ matrix[i][j] ≤ 10⁹；1 ≤ k ≤ n²。',
        [
            '示例 1：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8 → 13',
            '示例 2：matrix = [[-5]], k = 1 → -5',
        ],
        [
            'count_le(mid) 从左下角出发，统计 ≤ mid 的元素个数。',
            'left=matrix[0][0], right=matrix[-1][-1] 对值域二分。',
            'count_le(mid) >= k 则 right = mid，否则 left = mid + 1。',
            '返回 left 即为第 k 小元素值。',
        ],
        '二分查找',
        code_notes=[
            'def count_le(mid) — 统计矩阵中 ≤ mid 的元素数。',
            'row, col = n - 1, 0 — 从左下角出发。',
            'if matrix[row][col] <= mid: total += row + 1; col += 1',
            'else: row -= 1 — 排除当前行。',
            'left, right = matrix[0][0], matrix[-1][-1] — 值域二分。',
            'if count_le(mid) >= k: right = mid else: left = mid + 1',
            'return left — 第 k 小元素值。',
        ],
        complexity='时间 O(n log(max-min))，空间 O(1)。',
    ),
    'patterns/binary_search/median_of_two_sorted_arrays.py::find_median_sorted_arrays': _m(
        '4', '寻找两个正序数组的中位数',
        '给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。'
        '请你找出并返回这两个正序数组的中位数。\n\n'
        '算法的时间复杂度应该为 O(log (m+n))。\n\n'
        '本实现通过 get_kth_element 每次比较两数组第 k/2 个候选元素，'
        '淘汰较小一侧的前 k/2 段，递归找第 k 小元素。\n\n'
        '约束：nums1.length == m；nums2.length == n；0 ≤ m, n ≤ 1000；'
        '1 ≤ m + n ≤ 2000；-10⁶ ≤ nums1[i], nums2[i] ≤ 10⁶。',
        [
            '示例 1：nums1 = [1,3], nums2 = [2] → 2.00000',
            '示例 2：nums1 = [1,2], nums2 = [3,4] → 2.50000',
        ],
        [
            'get_kth_element(k) 在两有序数组中找第 k 小（1-indexed）。',
            '取 pivot1 = nums1[index1 + k//2 - 1] 与 pivot2 比较（注意越界取末尾）。',
            '淘汰 pivot 较小一侧的前 k/2 段，k 减去淘汰个数，继续递归。',
            'k==1 时返回 min(nums1[index1], nums2[index2])。',
            '总长度奇数取第 (m+n+1)//2 小；偶数取第 m+n//2 与 //2+1 小的平均值。',
        ],
        '二分查找',
        code_notes=[
            'index1, index2 = 0, 0 — 两数组当前未淘汰的起始下标。',
            'if index1 == m: return nums2[index2 + k - 1] — 一方耗尽。',
            'if k == 1: return min(nums1[index1], nums2[index2]) — 基例。',
            'new_index1 = min(index1 + k // 2 - 1, m - 1) — 防越界取 pivot。',
            'pivot1, pivot2 = nums1[new_index1], nums2[new_index2]',
            'if pivot1 <= pivot2 — 淘汰 nums1 前段；else 淘汰 nums2 前段。',
            '偶数长度时两次 get_kth_element 取平均。',
        ],
        complexity='时间 O(log(m+n))，空间 O(1)。',
    ),
}
