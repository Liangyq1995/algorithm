"""子序列、编辑距离、回文相关 DP。"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    """1143. 最长公共子序列"""
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def longest_common_subarray(nums1: list[int], nums2: list[int]) -> int:
    """718. 最长重复子数组"""
    dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
    best = 0
    for i in range(1, len(nums1) + 1):
        for j in range(1, len(nums2) + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                best = max(best, dp[i][j])
    return best


def max_uncrossed_lines(nums1: list[int], nums2: list[int]) -> int:
    """1035. 不相交的线"""
    dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
    for i in range(1, len(nums1) + 1):
        for j in range(1, len(nums2) + 1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def is_subsequence(s: str, t: str) -> bool:
    """392. 判断子序列"""
    i = 0
    for ch in t:
        if i < len(s) and s[i] == ch:
            i += 1
    return i == len(s)


def num_distinct(s: str, t: str) -> int:
    """115. 不同的子序列"""
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(len(s) + 1):
        dp[i][0] = 1
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


def min_delete_distance(word1: str, word2: str) -> int:
    """583. 两个字符串的删除操作"""
    lcs = longest_common_subsequence(word1, word2)
    return len(word1) + len(word2) - 2 * lcs


def min_edit_distance(word1: str, word2: str) -> int:
    """72. 编辑距离"""
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
        dp[i][0] = i
    for j in range(len(word2) + 1):
        dp[0][j] = j
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    return dp[-1][-1]


def longest_palindrome_subseq(s: str) -> int:
    """516. 最长回文子序列"""
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]


def longest_palindrome(s: str) -> str:
    """5. 最长回文子串"""
    if len(s) < 2:
        return s
    best_start, best_len = 0, 1
    dp = [[False] * len(s) for _ in range(len(s))]
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                dp[i][j] = True
                if j - i + 1 > best_len:
                    best_start, best_len = i, j - i + 1
    return s[best_start : best_start + best_len]


def count_substrings(s: str) -> int:
    """647. 回文子串"""
    count = 0
    dp = [[False] * len(s) for _ in range(len(s))]
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s)):
            if s[i] == s[j] and (j - i <= 1 or dp[i + 1][j - 1]):
                dp[i][j] = True
                count += 1
    return count


def num_decodings(s: str) -> int:
    """91. 解码方法"""
    if not s or s[0] == "0":
        return 0
    dp = [0] * (len(s) + 1)
    dp[0] = dp[1] = 1
    for i in range(2, len(s) + 1):
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]
        two_digit = int(s[i - 2 : i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    return dp[-1]


def length_of_lis(nums: list[int]) -> int:
    """300. 最长递增子序列"""
    piles: list[int] = []
    for num in nums:
        lo, hi = 0, len(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if piles[mid] < num:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(piles):
            piles.append(num)
        else:
            piles[lo] = num
    return len(piles)


def num_trees(n: int) -> int:
    """96. 不同的二叉搜索树"""
    dp = [0] * (n + 1)
    dp[0] = 1
    for nodes in range(1, n + 1):
        for root in range(1, nodes + 1):
            dp[nodes] += dp[root - 1] * dp[nodes - root]
    return dp[n]


def is_interleave(s1: str, s2: str, s3: str) -> bool:
    """97. 交错字符串"""
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0 and s1[i - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]
            if j > 0 and s2[j - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i][j - 1]
    return dp[m][n]


def predict_the_winner(nums: list[int]) -> bool:
    """486. 预测赢家"""
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = nums[i]
    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            dp[left][right] = max(
                nums[left] - dp[left + 1][right],
                nums[right] - dp[left][right - 1],
            )
    return dp[0][n - 1] >= 0
