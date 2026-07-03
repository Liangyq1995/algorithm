from __future__ import annotations

from typing import Optional


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


class TreeNode:
    __slots__ = ("val", "left", "right")

    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class ConnectNode:
    __slots__ = ("val", "left", "right", "next")

    def __init__(
        self,
        val: int = 0,
        left: Optional[ConnectNode] = None,
        right: Optional[ConnectNode] = None,
        next: Optional[ConnectNode] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class RandomListNode:
    __slots__ = ("val", "next", "random")

    def __init__(
        self,
        val: int = 0,
        next: Optional[RandomListNode] = None,
        random: Optional[RandomListNode] = None,
    ) -> None:
        self.val = val
        self.next = next
        self.random = random


class GraphNode:
    __slots__ = ("val", "neighbors")

    def __init__(self, val: int = 0, neighbors: list[GraphNode] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
