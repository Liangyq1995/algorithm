"""二分查找相关题目。"""


def binary_search(nums: list[int], target: int) -> int:
    """704. 二分查找（左闭右开）"""
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


def find_min_in_rotated_array(nums: list[int]) -> int:
    """153. 旋转数组最小值"""
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] < nums[right]:
            return nums[left]
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


def kth_smallest_in_matrix(matrix: list[list[int]], k: int) -> int:
    """378. 有序矩阵第 k 小"""
    n = len(matrix)

    def count_le(mid: int) -> int:
        row, col = n - 1, 0
        total = 0
        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                total += row + 1
                col += 1
            else:
                row -= 1
        return total

    left, right = matrix[0][0], matrix[-1][-1]
    while left < right:
        mid = (left + right) // 2
        if count_le(mid) >= k:
            right = mid
        else:
            left = mid + 1
    return left


def search_rotated(nums: list[int], target: int) -> int:
    """33. 搜索旋转排序数组"""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def search_range(nums: list[int], target: int) -> list[int]:
    """34. 在排序数组中查找元素的第一个和最后一个位置"""

    def lower_bound() -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def upper_bound() -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    left = lower_bound()
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    return [left, upper_bound() - 1]


def search_insert_position(nums: list[int], target: int) -> int:
    """35. 搜索插入位置"""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def my_sqrt(x: int) -> int:
    """69. x 的平方根"""
    if x < 2:
        return x
    lo, hi = 1, x // 2
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi


def find_peak_element(nums: list[int]) -> int:
    """162. 寻找峰值"""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


def split_array_largest_sum(nums: list[int], k: int) -> int:
    """410. 分割数组的最大值"""

    def can_split(limit: int) -> bool:
        parts = 1
        current = 0
        for num in nums:
            if current + num > limit:
                parts += 1
                current = num
            else:
                current += num
        return parts <= k

    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_split(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
