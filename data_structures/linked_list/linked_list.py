"""链表相关题目。"""

from functools import reduce
from typing import Optional

from algorithm.common.nodes import ListNode, RandomListNode


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """203. 移除链表元素"""
    dummy = ListNode(0, head)
    cur = dummy
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """206. 反转链表"""
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """92. 反转链表 II"""
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next
    cur = prev.next
    for _ in range(right - left):
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt
    return dummy.next


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """328. 奇偶链表"""
    if not head:
        return head
    odd, even = head, head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """2. 两数相加"""
    dummy = ListNode()
    carry = 0
    cur = dummy
    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        carry, digit = divmod(total, 10)
        cur.next = ListNode(digit)
        cur = cur.next
    return dummy.next


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """24. 两两交换链表中的节点"""
    dummy = ListNode(0, head)
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """19. 删除链表的倒数第 N 个结点"""
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


def get_intersection_node(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    """160. 相交链表"""
    pa, pb = head_a, head_b
    while pa != pb:
        pa = pa.next if pa else head_b
        pb = pb.next if pb else head_a
    return pa


def partition_list(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    """86. 分隔链表"""
    before_dummy = before = ListNode()
    after_dummy = after = ListNode()
    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    after.next = None
    before.next = after_dummy.next
    return before_dummy.next


def reorder_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """143. 重排链表"""
    if not head:
        return head
    nodes: list[ListNode] = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    left, right = 0, len(nodes) - 1
    while left < right:
        nodes[left].next = nodes[right]
        left += 1
        if left == right:
            break
        nodes[right].next = nodes[left]
        right -= 1
    nodes[left].next = None
    return nodes[0]


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """83. 删除排序链表中的重复元素"""
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


def delete_all_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """82. 删除排序链表中的重复元素 II"""
    dummy = ListNode(0, head)
    prev = dummy
    while prev.next and prev.next.next:
        if prev.next.val == prev.next.next.val:
            val = prev.next.val
            while prev.next and prev.next.val == val:
                prev.next = prev.next.next
        else:
            prev = prev.next
    return dummy.next


def has_cycle(head: Optional[ListNode]) -> bool:
    """141. 环形链表"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """61. 旋转链表"""
    if not head or not head.next:
        return head
    length = 1
    tail = head
    while tail.next:
        length += 1
        tail = tail.next
    k %= length
    if k == 0:
        return head
    tail.next = head
    steps = length - k
    new_tail = head
    for _ in range(steps - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    """142. 环形链表 II"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """21. 合并两个有序链表"""
    dummy = ListNode()
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """23. 合并 K 个升序链表"""
    lists = [node for node in lists if node]
    if not lists:
        return None
    return reduce(merge_two_lists, lists)


def insertion_sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """147. 对链表进行插入排序"""
    dummy = ListNode(float("-inf"))
    while head:
        nxt = head.next
        prev = dummy
        while prev.next and prev.next.val < head.val:
            prev = prev.next
        head.next = prev.next
        prev.next = head
        head = nxt
    return dummy.next


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """88. 合并两个有序数组（原地）"""
    pos = m + n - 1
    while m > 0 and n > 0:
        if nums1[m - 1] < nums2[n - 1]:
            nums1[pos] = nums2[n - 1]
            n -= 1
        else:
            nums1[pos] = nums1[m - 1]
            m -= 1
        pos -= 1
    while n > 0:
        nums1[pos] = nums2[n - 1]
        n -= 1
        pos -= 1


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """25. K 个一组翻转链表"""
    dummy = ListNode(0, head)
    prev_group = dummy
    while True:
        kth = prev_group
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
        group_next = kth.next
        prev, cur = kth.next, prev_group.next
        while cur != group_next:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        tail = prev_group.next
        prev_group.next = kth
        prev_group = tail


def copy_random_list(head: Optional[RandomListNode]) -> Optional[RandomListNode]:
    """138. 复制带随机指针的链表"""
    if not head:
        return None
    cur = head
    while cur:
        copy = RandomListNode(cur.val, cur.next)
        cur.next = copy
        cur = copy.next
    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    dummy = RandomListNode()
    prev, cur = dummy, head
    while cur:
        clone = cur.next
        cur.next = clone.next
        prev.next = clone
        prev = clone
        cur = cur.next
    return dummy.next


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """148. 排序链表"""

    def merge(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    return merge(sort_list(head), sort_list(mid))


def is_palindrome_list(head: Optional[ListNode]) -> bool:
    """234. 回文链表"""
    if not head or not head.next:
        return True
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True


def delete_node(node: ListNode) -> None:
    """237. 删除链表中的节点"""
    node.val = node.next.val
    node.next = node.next.next
