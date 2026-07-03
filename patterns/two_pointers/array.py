"""双指针相关题目。"""


def sorted_squares(nums: list[int]) -> list[int]:
    """977. 有序数组的平方"""
    result: list[int] = []
    left, right = 0, len(nums) - 1
    while left <= right:
        left_sq, right_sq = nums[left] ** 2, nums[right] ** 2
        if left_sq <= right_sq:
            result.append(right_sq)
            right -= 1
        else:
            result.append(left_sq)
            left += 1
    return result[::-1]


def move_zeros(nums: list[int]) -> None:
    """283. 移动零"""
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


def remove_element(nums: list[int], val: int) -> int:
    """27. 移除元素"""
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return slow


def remove_duplicates(nums: list[int]) -> int:
    """26. 删除有序数组重复项"""
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


def remove_duplicates_allow_twice(nums: list[int]) -> int:
    """80. 删除有序数组重复项 II"""
    write = 0
    for num in nums:
        if write < 2 or num != nums[write - 2]:
            nums[write] = num
            write += 1
    return write


def sort_colors(nums: list[int]) -> None:
    """75. 颜色分类（两次遍历版）"""
    write = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i], nums[write] = nums[write], nums[i]
            write += 1
    for i in range(write, len(nums)):
        if nums[i] == 1:
            nums[i], nums[write] = nums[write], nums[i]
            write += 1


def max_area(height: list[int]) -> int:
    """11. 盛最多水的容器"""
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        best = max(best, h * width)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return best


def three_sum(nums: list[int]) -> list[list[int]]:
    """15. 三数之和"""
    nums.sort()
    result: list[list[int]] = []
    for i, anchor in enumerate(nums):
        if anchor > 0:
            break
        if i > 0 and anchor == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = anchor + nums[left] + nums[right]
            if total == 0:
                result.append([anchor, nums[left], nums[right]])
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    """18. 四数之和"""
    nums.sort()
    n = len(nums)
    result: list[list[int]] = []
    for i in range(n):
        if nums[i] > target and nums[i] > 0 and target > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if nums[i] + nums[j] > target and target > 0:
                break
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result


def three_sum_closest(nums: list[int], target: int) -> int:
    """16. 最接近的三数之和"""
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(total - target) < abs(closest - target):
                closest = total
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total
    return closest


def triangle_number(nums: list[int]) -> int:
    """611. 有效三角形的个数"""
    nums.sort()
    count = 0
    for i in range(len(nums) - 2):
        if nums[i] == 0:
            continue
        k = i + 2
        for j in range(i + 1, len(nums) - 1):
            while k < len(nums) and nums[i] + nums[j] > nums[k]:
                k += 1
            count += k - j - 1
    return count


def two_sum_ii(numbers: list[int], target: int) -> list[int]:
    """167. 两数之和 II"""
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1
    return []
