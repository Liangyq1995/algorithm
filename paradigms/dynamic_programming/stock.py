"""股票买卖系列 DP。"""


def max_profit_once(prices: list[int]) -> int:
    """121. 买卖股票的最佳时机"""
    min_price = prices[0]
    best = 0
    for price in prices[1:]:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best


def max_profit_unlimited(prices: list[int]) -> int:
    """122. 买卖股票的最佳时机 II"""
    hold, cash = -prices[0], 0
    for price in prices[1:]:
        hold = max(hold, cash - price)
        cash = max(cash, hold + price)
    return cash


def max_profit_twice(prices: list[int]) -> int:
    """123. 买卖股票的最佳时机 III"""
    if not prices:
        return 0
    dp = [0, -prices[0], 0, -prices[0], 0]
    for price in prices[1:]:
        dp[1] = max(dp[1], dp[0] - price)
        dp[2] = max(dp[2], dp[1] + price)
        dp[3] = max(dp[3], dp[2] - price)
        dp[4] = max(dp[4], dp[3] + price)
    return dp[4]


def max_profit_k_transactions(k: int, prices: list[int]) -> int:
    """188. 买卖股票的最佳时机 IV"""
    if not prices or k == 0:
        return 0
    dp = [[0] * (2 * k + 1) for _ in range(len(prices))]
    for j in range(1, 2 * k, 2):
        dp[0][j] = -prices[0]
    for i in range(1, len(prices)):
        for j in range(0, 2 * k - 1, 2):
            dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
            dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])
    return dp[-1][2 * k]


def max_profit_with_cooldown(prices: list[int]) -> int:
    """309. 最佳买卖股票时机含冷冻期"""
    hold, sold, rest = -prices[0], 0, 0
    for price in prices[1:]:
        hold, sold, rest = max(hold, rest - price), hold + price, max(rest, sold)
    return max(sold, rest)


def max_profit_with_fee(prices: list[int], fee: int) -> int:
    """714. 买卖股票含手续费"""
    hold, cash = -prices[0], 0
    for price in prices[1:]:
        hold = max(hold, cash - price)
        cash = max(cash, hold + price - fee)
    return cash
