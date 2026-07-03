"""前缀和 + 哈希相关题目。"""


def sub_array_sum(nums: list[int], k: int) -> int:
    """560. 和为 K 的子数组"""
    prefix_count = {0: 1}
    acc = count = 0
    for num in nums:
        acc += num
        count += prefix_count.get(acc - k, 0)
        prefix_count[acc] = prefix_count.get(acc, 0) + 1
    return count


def find_max_length(nums: list[int]) -> int:
    """525. 连续数组（0/1 变 ±1）"""
    transformed = [1 if x == 1 else -1 for x in nums]
    first_index = {0: -1}
    acc = best = 0
    for i, value in enumerate(transformed):
        acc += value
        if acc in first_index:
            best = max(best, i - first_index[acc])
        else:
            first_index[acc] = i
    return best


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    """219. 存在重复元素 II"""
    last_index: dict[int, int] = {}
    for index, value in enumerate(nums):
        if value in last_index and index - last_index[value] <= k:
            return True
        last_index[value] = index
    return False
