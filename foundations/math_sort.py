"""数学与排序基础。"""

from math import gcd


def fraction_to_decimal(numerator: int, denominator: int) -> str:
    """166. 分数到小数"""
    if numerator == 0:
        return "0"
    sign = "-" if (numerator < 0) ^ (denominator < 0) else ""
    num, den = abs(numerator), abs(denominator)
    integer = num // den
    remainder = num % den
    if remainder == 0:
        return sign + str(integer)
    result = f"{sign}{integer}."
    seen: dict[int, int] = {}
    while remainder:
        if remainder in seen:
            start = seen[remainder]
            return result[:start] + "(" + result[start:] + ")"
        seen[remainder] = len(result)
        remainder *= 10
        result += str(remainder // den)
        remainder %= den
    return result


def sort_array(nums: list[int]) -> list[int]:
    """912. 排序数组（归并排序）"""
    if len(nums) <= 1:
        return nums

    def merge(left: list[int], right: list[int]) -> list[int]:
        result: list[int] = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(nums) // 2
    return merge(sort_array(nums[:mid]), sort_array(nums[mid:]))
