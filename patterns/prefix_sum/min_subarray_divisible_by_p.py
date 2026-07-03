"""
给你一个正整数数组nums，请你移除 最短子数组（可以为 空），使得剩余元素的 和能被 p整除。 不允许将整个数组都移除。
请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 -1。子数组定义为原数组中连续的一组元素。

示例 1：
输入：nums = [3,1,4,2], p = 6
输出：1
解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。
示例 2：
输入：nums = [6,3,5,2], p = 9
输出：2
解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。
"""


def min_sub_array(nums: list[int], p: int) -> int:
    x = sum(nums) % p
    # 子数组把数组分为3段，a, b, c如果删除b使得(sum(a) + sum(c))%p =0, 那么需要sum(b) % p = sum(nums) % p
    if x == 0:
        return 0
    res = len(nums)
    mapping = {0: -1}
    y = 0
    for index, value in enumerate(nums):
        y = (y + value) % p
        if (y - x) % p in mapping:  # sum(a) +sum(b) % p = y 要满足sum(b) % p = x, sum(a) % p = y - x
            res = min(res, index - mapping[(y - x) % p])
        mapping[y] = index
    return res if res < len(nums) else -1


    
