"""栈、队列、堆相关题目。"""

from collections import OrderedDict, deque
from operator import add, mul, sub
from typing import Optional

import heapq


def is_valid_parentheses(s: str) -> bool:
    """20. 有效的括号"""
    stack: list[str] = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch not in pairs:
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack


def remove_adjacent_duplicates(s: str) -> str:
    """1047. 删除字符串中的所有相邻重复项"""
    stack: list[str] = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)


def eval_rpn(tokens: list[str]) -> int:
    """150. 逆波兰表达式求值"""
    ops = {"+": add, "-": sub, "*": mul, "/": lambda x, y: int(x / y)}
    stack: list[int] = []
    for token in tokens:
        if token in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[token](a, b))
        else:
            stack.append(int(token))
    return stack.pop()


def decode_string(s: str) -> str:
    """394. 字符串解码"""
    stack: list[str | int] = []
    for ch in s:
        if ch == "]":
            repeat_str = ""
            while stack and stack[-1] != "[":
                repeat_str = str(stack.pop()) + repeat_str
            stack.pop()
            repeat_count = ""
            while stack and isinstance(stack[-1], str) and stack[-1].isdigit():
                repeat_count = str(stack.pop()) + repeat_count
            stack.append(repeat_str * int(repeat_count))
        else:
            stack.append(ch)
    return "".join(str(x) for x in stack)


class MonotonicQueue:
    """239. 滑动窗口最大值使用的单调队列。"""

    def __init__(self) -> None:
        self.queue: deque[int] = deque()

    def push(self, value: int) -> None:
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def pop(self, value: int) -> None:
        if self.queue and self.queue[0] == value:
            self.queue.popleft()

    def front(self) -> int:
        return self.queue[0]


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """239. 滑动窗口最大值"""
    queue = MonotonicQueue()
    result: list[int] = []
    for i, value in enumerate(nums):
        queue.push(value)
        if i >= k - 1:
            result.append(queue.front())
            queue.pop(nums[i - k + 1])
    return result


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """347. 前 K 个高频元素"""
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    heap: list[tuple[int, int]] = []
    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in sorted(heap, reverse=True)]


def find_kth_largest(nums: list[int], k: int) -> int:
    """215. 数组中的第 K 个最大元素"""
    heap: list[int] = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def asteroid_collision(asteroids: list[int]) -> list[int]:
    """735. 小行星碰撞"""
    stack: list[int] = []
    for asteroid in asteroids:
        if asteroid > 0 or not stack or stack[-1] < 0:
            stack.append(asteroid)
            continue
        while stack and stack[-1] > 0:
            if stack[-1] + asteroid > 0:
                break
            if stack[-1] + asteroid < 0:
                stack.pop()
                continue
            stack.pop()
            break
        else:
            stack.append(asteroid)
    return stack


class QueueUsingStack:
    """232. 用栈实现队列"""

    def __init__(self) -> None:
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move(self) -> None:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


class StackUsingQueue:
    """225. 用队列实现栈"""

    def __init__(self) -> None:
        self.queue: deque[int] = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> Optional[int]:
        if not self.queue:
            return None
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> Optional[int]:
        return self.queue[-1] if self.queue else None

    def empty(self) -> bool:
        return not self.queue


class MinStack:
    """155. 最小栈"""

    def __init__(self) -> None:
        self.stack: list[int] = []
        self.min_stack: list[int] = [float("inf")]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class LRUCache:
    """146. LRU 缓存"""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


class MedianFinder:
    """295. 数据流的中位数"""

    def __init__(self) -> None:
        self.small: list[int] = []  # max-heap via negation
        self.large: list[int] = []  # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    """253. 会议室 II"""
    if not intervals:
        return 0
    starts = sorted(start for start, _ in intervals)
    ends = sorted(end for _, end in intervals)
    rooms = max_rooms = 0
    i = j = 0
    while i < len(starts):
        if starts[i] < ends[j]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            i += 1
        else:
            rooms -= 1
            j += 1
    return max_rooms


def simplify_path(path: str) -> str:
    """71. 简化路径"""
    stack: list[str] = []
    for part in path.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return "/" + "/".join(stack)
