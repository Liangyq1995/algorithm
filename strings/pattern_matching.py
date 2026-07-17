"""KMP 与重复子串。"""

from common.kmp import build_next


def is_match(s: str, p: str) -> bool:
    """10. 正则表达式匹配"""
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(2, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            elif p[j - 1] == "." or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]


def repeat_substring_pattern(s: str) -> bool:
    """459. 重复的子字符串（拼接法）"""
    return s in (s + s)[1:-1]


def repeat_substring_pattern_by_kmp(s: str) -> bool:
    """459. 重复的子字符串（KMP）"""
    nxt = build_next(s)
    border = nxt[-1]
    return border != 0 and len(s) % (len(s) - border) == 0
