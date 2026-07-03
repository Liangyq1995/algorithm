"""位运算相关题目。"""


def single_number(nums: list[int]) -> int:
    """136. 只出现一次的数字"""
    result = 0
    for num in nums:
        result ^= num
    return result


def hamming_weight(n: int) -> int:
    """191. 位1的个数"""
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def reverse_bits(n: int) -> int:
    """190. 颠倒二进制位"""
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


def trailing_zeros(n: int) -> int:
    """172. 阶乘后的零"""
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


def count_bits(n: int) -> list[int]:
    """338. 比特位计数"""
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


def hamming_distance(x: int, y: int) -> int:
    """461. 汉明距离"""
    xor = x ^ y
    count = 0
    while xor:
        xor &= xor - 1
        count += 1
    return count


def gray_code(n: int) -> list[int]:
    """89. 格雷编码"""
    result = [0]
    for i in range(n):
        for j in range(len(result) - 1, -1, -1):
            result.append(result[j] | (1 << i))
    return result
