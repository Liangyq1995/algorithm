"""KMP 字符串匹配公共实现。"""


def build_next(pattern: str) -> list[int]:
    """构建 next / lps 数组。"""
    nxt = [0]
    prefix_len = 0
    i = 1
    while i < len(pattern):
        if pattern[prefix_len] == pattern[i]:
            prefix_len += 1
            nxt.append(prefix_len)
            i += 1
        elif prefix_len == 0:
            nxt.append(0)
            i += 1
        else:
            prefix_len = nxt[prefix_len - 1]
    return nxt


def kmp_search(text: str, pattern: str) -> int:
    """在 text 中查找 pattern 首次出现位置，未找到返回 -1。"""
    if not pattern:
        return 0
    nxt = build_next(pattern)
    j = 0
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = nxt[j - 1]
        if ch == pattern[j]:
            j += 1
        if j == len(pattern):
            return i - len(pattern) + 1
    return -1


def str_str(haystack: str, needle: str) -> int:
    return kmp_search(haystack, needle)
