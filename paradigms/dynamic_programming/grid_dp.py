"""网格 DP。"""


def unique_paths(m: int, n: int) -> int:
    """62. 不同路径"""
    row = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[-1]


def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:
    """63. 不同路径 II"""
    if obstacle_grid[0][0] == 1:
        return 0
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    dp = [0] * n
    for j in range(n):
        if obstacle_grid[0][j] == 1:
            break
        dp[j] = 1
    for i in range(1, m):
        if obstacle_grid[i][0] == 1:
            dp[0] = 0
        for j in range(1, n):
            if obstacle_grid[i][j] == 1:
                dp[j] = 0
            else:
                dp[j] += dp[j - 1]
    return dp[-1]


def min_path_sum(grid: list[list[int]]) -> int:
    """64. 最小路径和"""
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    for i in range(m):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
    return dp[-1]


def max_path_sum(grid: list[list[int]]) -> int:
    """扩展：最大路径和"""
    m, n = len(grid), len(grid[0])
    dp = [0] * n
    for i in range(m):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = max(dp[j - 1], dp[j]) + grid[i][j]
    return dp[-1]


def minimal_triangle_path(triangle: list[list[int]]) -> int:
    """120. 三角形最小路径和"""
    if not triangle:
        return 0
    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            left = triangle[row - 1][col - 1] if col > 0 else triangle[row - 1][0]
            right = triangle[row - 1][col] if col < len(triangle[row - 1]) else triangle[row - 1][-1]
            triangle[row][col] += min(left, right)
    return min(triangle[-1])


def maximal_square(matrix: list[list[str]]) -> int:
    """221. 最大正方形"""
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    best = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] == "1":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                best = max(best, dp[i][j])
    return best * best


def min_swap(nums1: list[int], nums2: list[int]) -> int:
    """801. 使序列递增的最小交换次数"""
    n = len(nums1)
    keep, swap = 0, 1
    for i in range(1, n):
        keep2, swap2 = n, n
        if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
            keep2 = min(keep2, keep)
            swap2 = min(swap2, swap + 1)
        if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
            keep2 = min(keep2, swap)
            swap2 = min(swap2, keep + 1)
        keep, swap = keep2, swap2
    return min(keep, swap)


def stone_game(piles: list[int]) -> bool:
    """877. 石子游戏"""
    n = len(piles)
    dp = [[0] * n for _ in range(n)]
    for i, pile in enumerate(piles):
        dp[i][i] = pile
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
    return dp[0][n - 1] > 0


def num_tilings(n: int) -> int:
    """790. 多米诺和托米诺平铺"""
    mod = 10 ** 9 + 7
    if n == 1:
        return 1
    complete = [1, 2] + [0] * (n - 2)
    partial = [0, 1] + [0] * (n - 2)
    for i in range(2, n):
        complete[i] = (complete[i - 1] + complete[i - 2] + 2 * partial[i - 1]) % mod
        partial[i] = (partial[i - 1] + complete[i - 2]) % mod
    return complete[n - 1]
