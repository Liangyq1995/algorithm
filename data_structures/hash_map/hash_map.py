"""哈希表相关题目。"""

from collections import Counter, defaultdict
from math import gcd


def is_anagram(s: str, t: str) -> bool:
    """242. 有效的字母异位词"""
    return Counter(s) == Counter(t)


def find_anagrams(s: str, p: str) -> list[int]:
    """438. 找到字符串中所有字母异位词"""
    if len(p) > len(s):
        return []
    need = [0] * 26
    window = [0] * 26
    for ch in p:
        need[ord(ch) - ord("a")] += 1
    for ch in s[: len(p)]:
        window[ord(ch) - ord("a")] += 1
    result = [0] if window == need else []
    for i in range(len(s) - len(p)):
        window[ord(s[i]) - ord("a")] -= 1
        window[ord(s[i + len(p)]) - ord("a")] += 1
        if window == need:
            result.append(i + 1)
    return result


def can_construct(ransom_note: str, magazine: str) -> bool:
    """383. 赎金信"""
    counts = Counter(magazine)
    for ch in ransom_note:
        counts[ch] -= 1
        if counts[ch] < 0:
            return False
    return True


def common_chars(words: list[str]) -> list[str]:
    """1002. 查找共用字符"""
    if not words:
        return []
    freq = [0] * 26
    for ch in words[0]:
        freq[ord(ch) - ord("a")] += 1
    for word in words[1:]:
        other = [0] * 26
        for ch in word:
            other[ord(ch) - ord("a")] += 1
        freq = [min(a, b) for a, b in zip(freq, other)]
    result: list[str] = []
    for i, count in enumerate(freq):
        result.extend(chr(i + ord("a")) * count)
    return result


def two_sum(nums: list[int], target: int) -> list[int]:
    """1. 两数之和"""
    seen: dict[int, int] = {}
    for index, value in enumerate(nums):
        if target - value in seen:
            return [seen[target - value], index]
        seen[value] = index
    return []


def first_uniq_char(s: str) -> int:
    """387. 字符串中的第一个唯一字符"""
    positions = defaultdict(list)
    for index, ch in enumerate(s):
        positions[ch].append(index)
    best = float("inf")
    for indices in positions.values():
        if len(indices) == 1:
            best = min(best, indices[0])
    return -1 if best == float("inf") else best


def length_of_longest_substring(s: str) -> int:
    """3. 无重复字符的最长子串"""
    last_index: dict[str, int] = {}
    start = best = 0
    for index, ch in enumerate(s):
        if ch in last_index and last_index[ch] >= start:
            start = last_index[ch] + 1
        best = max(best, index - start + 1)
        last_index[ch] = index
    return best


def _digit_square_sum(n: int) -> int:
    total = 0
    while n:
        n, rem = divmod(n, 10)
        total += rem ** 2
    return total


def is_happy(n: int) -> bool:
    """202. 快乐数"""
    seen: set[int] = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = _digit_square_sum(n)
    return n == 1


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """49. 字母异位词分组"""
    groups: dict[tuple[int, ...], list[str]] = defaultdict(list)
    for word in strs:
        signature = _anagram_key(word)
        groups[signature].append(word)
    return list(groups.values())


def _anagram_key(word: str) -> tuple[int, ...]:
    counts = [0] * 26
    for ch in word:
        counts[ord(ch) - 97] += 1
    return tuple(counts)


def contains_duplicate(nums: list[int]) -> bool:
    """217. 存在重复元素"""
    return len(nums) != len(set(nums))


def longest_consecutive(nums: list[int]) -> int:
    """128. 最长连续序列"""
    num_set = set(nums)
    best = 0
    for num in num_set:
        if num - 1 in num_set:
            continue
        length = 1
        while num + length in num_set:
            length += 1
        best = max(best, length)
    return best


def find_disappeared_numbers(nums: list[int]) -> list[int]:
    """448. 找到所有数组中消失的数字"""
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
    return [i + 1 for i, num in enumerate(nums) if num > 0]


def longest_palindrome(s: str) -> int:
    """409. 最长回文串"""
    from collections import Counter

    counts = Counter(s)
    length = 0
    odd = False
    for freq in counts.values():
        length += freq // 2 * 2
        if freq % 2:
            odd = True
    return length + (1 if odd else 0)


def max_points(points: list[list[int]]) -> int:
    """149. 直线上最多的点数"""
    if len(points) <= 2:
        return len(points)
    best = 0
    for i, (x1, y1) in enumerate(points):
        slopes: dict[tuple[int, int], int] = {}
        same = 1
        local_best = 0
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            if x1 == x2 and y1 == y2:
                same += 1
                continue
            dx, dy = x2 - x1, y2 - y1
            g = gcd(dx, dy)
            dx //= g
            dy //= g
            if dx < 0:
                dx, dy = -dx, -dy
            key = (dx, dy)
            slopes[key] = slopes.get(key, 0) + 1
            local_best = max(local_best, slopes[key])
        best = max(best, local_best + same)
    return best
