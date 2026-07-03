"""滑动窗口相关题目。"""


def min_sub_array_len(target: int, nums: list[int]) -> int:
    """209. 长度最小的子数组"""
    left = 0
    window_sum = 0
    min_len = float("inf")
    for right, value in enumerate(nums):
        window_sum += value
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return 0 if min_len == float("inf") else min_len


def character_replacement(s: str, k: int) -> int:
    """424. 替换后的最长重复字符"""
    best = 0
    for code in range(26):
        ch = chr(ord("A") + code)
        left = replacements = 0
        for right, cur in enumerate(s):
            replacements += cur != ch
            while replacements > k:
                replacements -= s[left] != ch
                left += 1
            best = max(best, right - left + 1)
    return best


def minimum_recolors(blocks: str, k: int) -> int:
    """2379. 得到 K 个黑块的最少涂色次数"""
    white = sum(block == "W" for block in blocks[:k])
    best = white
    for i in range(len(blocks) - k):
        if blocks[i + k] == "W":
            white += 1
        if blocks[i] == "W":
            white -= 1
        best = min(best, white)
    return best


def min_window(s: str, t: str) -> str:
    """76. 最小覆盖子串"""
    if not t:
        return ""
    need: dict[str, int] = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    missing = len(t)
    left = start = 0
    best_len = float("inf")
    for right, ch in enumerate(s):
        if ch in need:
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best_len:
                best_len = right - left + 1
                start = left
            left_ch = s[left]
            if left_ch in need:
                need[left_ch] += 1
                if need[left_ch] > 0:
                    missing += 1
            left += 1
    return "" if best_len == float("inf") else s[start : start + best_len]
