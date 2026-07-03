"""线性 DP：打家劫舍、爬楼梯、最大子数组等。"""


def max_subarray(nums: list[int]) -> int:
    """53. 最大子数组和"""
    best = cur = nums[0]
    for value in nums[1:]:
        cur = max(value, cur + value)
        best = max(best, cur)
    return best


def climbing_stairs(n: int) -> int:
    """70. 爬楼梯"""
    if n <= 2:
        return n
    prev, cur = 1, 2
    for _ in range(3, n + 1):
        prev, cur = cur, prev + cur
    return cur


def house_robber(nums: list[int]) -> int:
    """198. 打家劫舍"""
    prev, cur = 0, 0
    for value in nums:
        prev, cur = cur, max(cur, prev + value)
    return cur


def house_robber_ii(nums: list[int]) -> int:
    """213. 打家劫舍 II"""
    if len(nums) == 1:
        return nums[0]

    def rob_range(start: int, end: int) -> int:
        prev, cur = 0, 0
        for i in range(start, end):
            prev, cur = cur, max(cur, prev + nums[i])
        return cur

    return max(rob_range(0, len(nums) - 1), rob_range(1, len(nums)))
