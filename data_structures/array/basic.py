"""数组基础操作（非特定模式）。"""

import math


def plus_one(digits: list[int]) -> list[int]:
    """66. 加一"""
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        carry, digits[i] = divmod(digits[i] + carry, 10)
    return [1] + digits if carry else digits


def merge_sorted_arrays(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """88. 合并两个有序数组"""
    pos = m + n - 1
    while m > 0 and n > 0:
        if nums1[m - 1] < nums2[n - 1]:
            nums1[pos] = nums2[n - 1]
            n -= 1
        else:
            nums1[pos] = nums1[m - 1]
            m -= 1
        pos -= 1
    while n > 0:
        nums1[pos] = nums2[n - 1]
        n -= 1
        pos -= 1


def majority_element(nums: list[int]) -> int:
    """169. 多数元素（Boyer-Moore 投票）"""
    count = 0
    candidate = nums[0]
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate


def find_unsorted_subarray(nums: list[int]) -> int:
    """581. 最短无序连续子数组"""
    n = len(nums)
    max_left, min_right = float("-inf"), float("inf")
    left, right = -1, -1
    for i in range(n):
        if max_left > nums[i]:
            right = i
        else:
            max_left = nums[i]
        if min_right < nums[n - i - 1]:
            left = n - i - 1
        else:
            min_right = nums[n - i - 1]
    return 0 if right == -1 else right - left + 1


def increasing_triplet(nums: list[int]) -> bool:
    """334. 递增的三元子序列"""
    first = second = float("inf")
    for num in nums:
        if num > second:
            return True
        if num > first:
            second = num
        else:
            first = num
    return False


def check_possibility(nums: list[int]) -> bool:
    """665. 非递减数列"""
    changes = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            changes += 1
            if changes > 1:
                return False
            if i > 0 and nums[i + 1] < nums[i - 1]:
                nums[i + 1] = nums[i]
    return True


def dist_money(money: int, children: int) -> int:
    """2591. 分发糖果"""
    if money < children:
        return -1
    money -= children
    count = min(money // 7, children)
    money -= count * 7
    children -= count
    if (children == 0 and money > 0) or (children == 1 and money == 3):
        count -= 1
    return count


def convert_to_base7(num: int) -> str:
    """504. 七进制数"""
    if num == 0:
        return "0"
    negative = num < 0
    num = abs(num)
    digits: list[str] = []
    while num:
        digits.append(str(num % 7))
        num //= 7
    if negative:
        digits.append("-")
    return "".join(reversed(digits))


def get_permutation(n: int, k: int) -> str:
    """60. 排列序列"""
    nums = [str(i) for i in range(1, n + 1)]
    result = []
    k -= 1
    while n > 0:
        n -= 1
        index, k = divmod(k, math.factorial(n))
        result.append(nums.pop(index))
    return "".join(result)


def max_subarray_sum_circular(nums: list[int]) -> int:
    """918. 环形子数组最大和"""
    def min_subarray(arr: list[int]) -> int:
        dp = best = arr[0]
        for value in arr[1:]:
            dp = min(value, dp + value)
            best = min(best, dp)
        return best

    def max_subarray(arr: list[int]) -> int:
        dp = best = arr[0]
        for value in arr[1:]:
            dp = max(value, dp + value)
            best = max(best, dp)
        return best

    total = sum(nums)
    min_sum = min_subarray(nums)
    max_sum = max_subarray(nums)
    if min_sum == total:
        return max(nums)
    return max(max_sum, total - min_sum)


def max_product_subarray(nums: list[int]) -> int:
    """152. 乘积最大子数组"""
    best = cur_max = cur_min = nums[0]
    for value in nums[1:]:
        if value < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(value, cur_max * value)
        cur_min = min(value, cur_min * value)
        best = max(best, cur_max)
    return best


def next_permutation(nums: list[int]) -> None:
    """31. 下一个排列"""
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    left, right = i + 1, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def first_missing_positive(nums: list[int]) -> int:
    """41. 缺失的第一个正数"""
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


def rotate_array(nums: list[int], k: int) -> None:
    """189. 轮转数组"""

    def reverse(lo: int, hi: int) -> None:
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    k %= len(nums)
    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)


def find_duplicate(nums: list[int]) -> int:
    """287. 寻找重复数"""
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


def pascal_triangle(num_rows: int) -> list[list[int]]:
    """118. 杨辉三角"""
    result: list[list[int]] = []
    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result


def my_pow(x: float, n: int) -> float:
    """50. Pow(x, n)"""
    if n < 0:
        x, n = 1 / x, -n
    result = 1.0
    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result


def product_except_self(nums: list[int]) -> list[int]:
    """238. 除自身以外数组的乘积"""
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result


def is_palindrome_number(x: int) -> bool:
    """9. 回文数"""
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    return x == reversed_half or x == reversed_half // 10


def divide(dividend: int, divisor: int) -> int:
    """29. 两数相除"""
    if dividend == -2 ** 31 and divisor == -1:
        return 2 ** 31 - 1
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
    a, b = abs(dividend), abs(divisor)
    result = 0
    for i in range(31, -1, -1):
        if (a >> i) >= b:
            result += 1 << i
            a -= b << i
    return sign * result
