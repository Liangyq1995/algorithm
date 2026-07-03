"""背包问题相关 DP。"""


def zero_one_knapsack(weight: list[int], value: list[int], capacity: int) -> int:
    """01 背包（滚动数组）"""
    dp = [0] * (capacity + 1)
    for i in range(len(weight)):
        for j in range(capacity, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    return dp[capacity]


def complete_knapsack(weight: list[int], value: list[int], capacity: int) -> int:
    """完全背包"""
    dp = [0] * (capacity + 1)
    for i in range(len(weight)):
        for j in range(weight[i], capacity + 1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    return dp[capacity]


def can_partition(nums: list[int]) -> bool:
    """416. 分割等和子集"""
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[target]


def last_stone_weight_ii(stones: list[int]) -> int:
    """1049. 最后一块石头的重量 II"""
    total = sum(stones)
    target = total // 2
    dp = [0] * (target + 1)
    for stone in stones:
        for j in range(target, stone - 1, -1):
            dp[j] = max(dp[j], dp[j - stone] + stone)
    return total - 2 * dp[target]


def target_sum_ways(nums: list[int], target: int) -> int:
    """494. 目标和"""
    total = sum(nums)
    if abs(target) > total or (target + total) % 2:
        return 0
    bag_size = (target + total) // 2
    dp = [0] * (bag_size + 1)
    dp[0] = 1
    for num in nums:
        for j in range(bag_size, num - 1, -1):
            dp[j] += dp[j - num]
    return dp[bag_size]


def coin_change_combinations(amount: int, coins: list[int]) -> int:
    """518. 零钱兑换 II"""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] += dp[j - coin]
    return dp[amount]


def combination_sum4(nums: list[int], target: int) -> int:
    """377. 组合总和 IV"""
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[target]


def coin_change_min(amount: int, coins: list[int]) -> int:
    """322. 零钱兑换"""
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    return -1 if dp[amount] == float("inf") else dp[amount]


def num_squares(n: int) -> int:
    """279. 完全平方数"""
    dp = [float("inf")] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[n]


def word_break(s: str, word_dict: list[str]) -> bool:
    """139. 单词拆分"""
    dp = [False] * (len(s) + 1)
    dp[0] = True
    words = set(word_dict)
    for j in range(1, len(s) + 1):
        for word in words:
            if j >= len(word) and dp[j - len(word)] and s[j - len(word) : j] == word:
                dp[j] = True
                break
    return dp[len(s)]


def find_max_form(strs: list[str], m: int, n: int) -> int:
    """474. 一和零"""
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for s in strs:
        zeros = s.count("0")
        ones = s.count("1")
        for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
    return dp[m][n]
