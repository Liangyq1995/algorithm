"""二叉树相关题目。"""

import collections
from collections import defaultdict, deque
from typing import List, Optional

from common.nodes import ConnectNode, ListNode, TreeNode

WHITE, GRAY = 0, 1


def _iterative_order(root: Optional[TreeNode], order: str) -> list[int]:
    stack = [(WHITE, root)]
    result: list[int] = []
    while stack:
        color, node = stack.pop()
        if not node:
            continue
        if color == WHITE:
            if order == "pre":
                stack.extend([(WHITE, node.right), (WHITE, node.left), (GRAY, node)])
            elif order == "in":
                stack.extend([(WHITE, node.right), (GRAY, node), (WHITE, node.left)])
            else:
                stack.extend([(GRAY, node), (WHITE, node.right), (WHITE, node.left)])
        else:
            result.append(node.val)
    return result


def preorder_traversal(root: Optional[TreeNode]) -> list[int]:
    return _iterative_order(root, "pre")


def inorder_traversal(root: Optional[TreeNode]) -> list[int]:
    return _iterative_order(root, "in")


def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
    return _iterative_order(root, "post")


def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    queue = deque([root])
    result: list[list[int]] = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


def right_side_view(root: Optional[TreeNode]) -> list[int]:
    return [level[-1] for level in level_order(root)]


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if not node:
            continue
        if color == WHITE:
            stack.extend([(WHITE, node.right), (GRAY, node), (WHITE, node.left)])
        else:
            k -= 1
            if k == 0:
                return node.val
    raise ValueError("k out of range")


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def tree_to_string(root: Optional[TreeNode]) -> str:
    if not root:
        return ""
    left = tree_to_string(root.left)
    right = tree_to_string(root.right)
    if right:
        return f"{root.val}({left})({right})"
    if left:
        return f"{root.val}({left})"
    return str(root.val)


def is_symmetric(root: Optional[TreeNode]) -> bool:
    def mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        return mirror(left.left, right.right) and mirror(left.right, right.left)

    return not root or mirror(root.left, root.right)


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def min_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))


def count_nodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    depth = 0
    left, right = root.left, root.right
    while left and right:
        depth += 1
        left, right = left.left, right.right
    if not left and not right:
        return 2 ** (depth + 1) - 1
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def is_balanced(root: Optional[TreeNode]) -> bool:
    def height(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1


def binary_tree_paths(root: Optional[TreeNode]) -> list[str]:
    if not root:
        return []
    paths: list[str] = []
    stack = [(root, str(root.val))]
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            paths.append(path)
            continue
        if node.right:
            stack.append((node.right, f"{path}->{node.right.val}"))
        if node.left:
            stack.append((node.left, f"{path}->{node.left.val}"))
    return paths


def sum_of_left_leaves(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    total = 0
    if root.left and not root.left.left and not root.left.right:
        total += root.left.val
    return total + sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)


def find_bottom_left_value(root: Optional[TreeNode]) -> int:
    if not root:
        raise ValueError("empty tree")
    result = root.val
    for level in level_order(root):
        result = level[0]
    return result


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    def dfs(node: TreeNode, remain: int) -> bool:
        if not node.left and not node.right:
            return remain == 0
        if node.left and dfs(node.left, remain - node.left.val):
            return True
        if node.right and dfs(node.right, remain - node.right.val):
            return True
        return False

    return dfs(root, target_sum - root.val)


def path_sum(root: Optional[TreeNode], target_sum: int) -> list[list[int]]:
    result: list[list[int]] = []

    def dfs(node: Optional[TreeNode], path: list[int], remain: int) -> None:
        if not node:
            return
        if not node.left and not node.right and remain == 0:
            result.append(path[:])
            return
        if node.left:
            path.append(node.left.val)
            dfs(node.left, path, remain - node.left.val)
            path.pop()
        if node.right:
            path.append(node.right.val)
            dfs(node.right, path, remain - node.right.val)
            path.pop()

    if root:
        dfs(root, [root.val], target_sum - root.val)
    return result


def path_sum_3(root: Optional[TreeNode], target_sum: int) -> int:
    prefix = defaultdict(int)
    prefix[0] = 1

    def dfs(node: Optional[TreeNode], acc: int) -> int:
        if not node:
            return 0
        acc += node.val
        count = prefix[acc - target_sum]
        prefix[acc] += 1
        count += dfs(node.left, acc)
        count += dfs(node.right, acc)
        prefix[acc] -= 1
        return count

    return dfs(root, 0)


def sum_numbers(root: Optional[TreeNode]) -> int:
    total = 0

    def dfs(node: Optional[TreeNode], value: int) -> None:
        nonlocal total
        if not node:
            return
        value = value * 10 + node.val
        if not node.left and not node.right:
            total += value
            return
        dfs(node.left, value)
        dfs(node.right, value)

    dfs(root, 0)
    return total


def build_tree_pre_in(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if not preorder:
        return None
    root_val = preorder[0]
    split = inorder.index(root_val)
    root = TreeNode(root_val)
    root.left = build_tree_pre_in(preorder[1 : 1 + split], inorder[:split])
    root.right = build_tree_pre_in(preorder[1 + split :], inorder[split + 1 :])
    return root


def build_tree_in_post(inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
    if not postorder:
        return None
    root_val = postorder[-1]
    split = inorder.index(root_val)
    root = TreeNode(root_val)
    root.left = build_tree_in_post(inorder[:split], postorder[:split])
    root.right = build_tree_in_post(inorder[split + 1 :], postorder[split:-1])
    return root


def merge_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1:
        return root2
    if not root2:
        return root1
    root = TreeNode(root1.val + root2.val)
    root.left = merge_trees(root1.left, root2.left)
    root.right = merge_trees(root1.right, root2.right)
    return root


def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    prev = float("-inf")
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if not node:
            continue
        if color == WHITE:
            stack.extend([(WHITE, node.right), (GRAY, node), (WHITE, node.left)])
        elif node.val <= prev:
            return False
        else:
            prev = node.val
    return True


def get_minimum_difference(root: Optional[TreeNode]) -> int:
    prev: Optional[TreeNode] = None
    best = float("inf")
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if not node:
            continue
        if color == WHITE:
            stack.extend([(WHITE, node.right), (GRAY, node), (WHITE, node.left)])
        else:
            if prev:
                best = min(best, node.val - prev.val)
            prev = node
    return best


def find_mode(root: Optional[TreeNode]) -> list[int]:
    prev: Optional[TreeNode] = None
    count = max_count = 0
    result: list[int] = []
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if not node:
            continue
        if color == WHITE:
            stack.extend([(WHITE, node.right), (GRAY, node), (WHITE, node.left)])
        else:
            if not prev or prev.val != node.val:
                count = 1
            else:
                count += 1
            if count == max_count:
                result.append(node.val)
            elif count > max_count:
                max_count = count
                result = [node.val]
            prev = node
    return result


def sorted_array_to_bst(nums: list[int]) -> Optional[TreeNode]:
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1 :])
    return root


def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    if not root or root in (p, q):
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


def lowest_common_ancestor_bst(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
    return None


def insert_into_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root


def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return None
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    elif not root.left or not root.right:
        return root.left or root.right
    else:
        successor = root.right
        while successor.left:
            successor = successor.left
        successor.right = delete_node(root.right, successor.val)
        successor.left = root.left
        return successor
    return root


def trim_bst(root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val < low:
        return trim_bst(root.right, low, high)
    if root.val > high:
        return trim_bst(root.left, low, high)
    root.left = trim_bst(root.left, low, high)
    root.right = trim_bst(root.right, low, high)
    return root


def convert_bst(root: Optional[TreeNode]) -> Optional[TreeNode]:
    total = 0
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if not node:
            continue
        if color == WHITE:
            stack.extend([(WHITE, node.left), (GRAY, node), (WHITE, node.right)])
        else:
            total += node.val
            node.val = total
    return root


def prune_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left = prune_tree(root.left)
    root.right = prune_tree(root.right)
    if not root.left and not root.right and root.val == 0:
        return None
    return root


def generate_trees(n: int) -> list[Optional[TreeNode]]:
    if n == 0:
        return []

    def build(start: int, end: int) -> list[Optional[TreeNode]]:
        if start > end:
            return [None]
        trees: list[Optional[TreeNode]] = []
        for root_val in range(start, end + 1):
            for left in build(start, root_val - 1):
                for right in build(root_val + 1, end):
                    node = TreeNode(root_val, left, right)
                    trees.append(node)
        return trees

    return build(1, n)


def min_camera_cover(root: Optional[TreeNode]) -> int:
    UNWATCHED, WATCHED, CAMERA = 0, 1, 2
    cameras = 0

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal cameras
        if not node:
            return WATCHED
        left = dfs(node.left)
        right = dfs(node.right)
        if left == UNWATCHED or right == UNWATCHED:
            cameras += 1
            return CAMERA
        if left == CAMERA or right == CAMERA:
            return WATCHED
        return UNWATCHED

    if dfs(root) == UNWATCHED:
        cameras += 1
    return cameras


def vertical_traversal(root: Optional[TreeNode]) -> list[list[int]]:
    columns: dict[int, dict[int, list[int]]] = defaultdict(lambda: defaultdict(list))

    def dfs(node: Optional[TreeNode], x: int = 0, y: int = 0) -> None:
        if not node:
            return
        columns[x][y].append(node.val)
        dfs(node.left, x - 1, y + 1)
        dfs(node.right, x + 1, y + 1)

    dfs(root)
    result: list[list[int]] = []
    for x in sorted(columns):
        level: list[int] = []
        for y in sorted(columns[x]):
            level.extend(sorted(columns[x][y]))
        result.append(level)
    return result


def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """100. 相同的树"""
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)


def max_path_sum_binary_tree(root: Optional[TreeNode]) -> int:
    """124. 二叉树中的最大路径和"""
    best = float("-inf")

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal best
        if not node:
            return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        best = max(best, node.val + left + right)
        return node.val + max(left, right)

    dfs(root)
    return int(best)


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """543. 二叉树的直径"""
    best = 0

    def depth(node: Optional[TreeNode]) -> int:
        nonlocal best
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        best = max(best, left + right)
        return 1 + max(left, right)

    depth(root)
    return best


def zigzag_level_order(root: Optional[TreeNode]) -> list[list[int]]:
    """103. 二叉树的锯齿形层序遍历"""
    if not root:
        return []
    queue = deque([root])
    result: list[list[int]] = []
    left_to_right = True
    while queue:
        level: list[int] = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level if left_to_right else level[::-1])
        left_to_right = not left_to_right
    return result


def flatten(root: Optional[TreeNode]) -> None:
    """114. 展开二叉树为链表"""
    cur = root
    while cur:
        if cur.left:
            tail = cur.left
            while tail.right:
                tail = tail.right
            tail.right = cur.right
            cur.right = cur.left
            cur.left = None
        cur = cur.right


def rob_tree(root: Optional[TreeNode]) -> int:
    """337. 打家劫舍 III"""

    def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
        if not node:
            return 0, 0
        left_rob, left_skip = dfs(node.left)
        right_rob, right_skip = dfs(node.right)
        rob = node.val + left_skip + right_skip
        skip = max(left_rob, left_skip) + max(right_rob, right_skip)
        return rob, skip

    return max(dfs(root))


class Codec:
    """297. 二叉树的序列化与反序列化"""

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        parts: list[str] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                parts.append("#")
                return
            parts.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(parts)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        tokens = iter(data.split(","))

        def build() -> Optional[TreeNode]:
            val = next(tokens)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()


def level_order_bottom(root: Optional[TreeNode]) -> list[list[int]]:
    """107. 二叉树的层序遍历 II"""
    return list(reversed(level_order(root)))


def sorted_list_to_bst(head: Optional[ListNode]) -> Optional[TreeNode]:
    """109. 有序链表转换二叉搜索树"""
    values: list[int] = []
    cur = head
    while cur:
        values.append(cur.val)
        cur = cur.next

    def build(lo: int, hi: int) -> Optional[TreeNode]:
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = TreeNode(values[mid])
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(values) - 1)


def recover_tree(root: Optional[TreeNode]) -> None:
    """99. 恢复二叉搜索树"""
    first = second = prev = None

    def inorder(node: Optional[TreeNode]) -> None:
        nonlocal first, second, prev
        if not node:
            return
        inorder(node.left)
        if prev and node.val < prev.val:
            if not first:
                first = prev
            second = node
        prev = node
        inorder(node.right)

    inorder(root)
    if first and second:
        first.val, second.val = second.val, first.val


def connect(root: Optional[ConnectNode]) -> Optional[ConnectNode]:
    """116/117. 填充每个节点的下一个右侧节点指针"""
    if not root:
        return None
    leftmost = root
    while leftmost.left:
        head = tail = ConnectNode()
        cur = leftmost
        while cur:
            for child in (cur.left, cur.right):
                if child:
                    tail.next = child
                    tail = child
            cur = cur.next
        leftmost = leftmost.left
    return root


def connect_ii(root: Optional[ConnectNode]) -> Optional[ConnectNode]:
    """117. 填充每个节点的下一个右侧节点指针 II"""
    return connect(root)


def distance_k(root: Optional[TreeNode], target: TreeNode, k: int) -> list[int]:
    """863. 二叉树中所有距离为 K 的结点"""
    parent: dict[TreeNode, Optional[TreeNode]] = {root: None}

    def build(node: Optional[TreeNode]) -> None:
        if not node:
            return
        if node.left:
            parent[node.left] = node
            build(node.left)
        if node.right:
            parent[node.right] = node
            build(node.right)

    build(root)
    queue = deque([(target, 0)])
    visited = {target}
    result: list[int] = []
    while queue:
        node, dist = queue.popleft()
        if dist == k:
            result.append(node.val)
            continue
        for nxt in (node.left, node.right, parent.get(node)):
            if nxt and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, dist + 1))
    return result
