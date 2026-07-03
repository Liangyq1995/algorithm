"""单调栈相关题目。"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """739. 每日温度"""
    answer = [0] * len(temperatures)
    stack: list[int] = []
    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)
    return answer


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    """496. 下一个更大元素 I"""
    next_greater = [-1] * len(nums2)
    index_of = {value: index for index, value in enumerate(nums2)}
    stack: list[int] = []
    for value in nums2:
        while stack and value > stack[-1]:
            next_greater[index_of[stack.pop()]] = value
        stack.append(value)
    return [next_greater[index_of[value]] for value in nums1]


def next_greater_elements_circular(nums: list[int]) -> list[int]:
    """503. 下一个更大元素 II"""
    answer = [-1] * len(nums)
    stack: list[int] = []
    for i in range(2 * len(nums)):
        value = nums[i % len(nums)]
        while stack and value > nums[stack[-1]]:
            answer[stack.pop()] = value
        if i < len(nums):
            stack.append(i)
    return answer


def trap_rain_water(height: list[int]) -> int:
    """42. 接雨水"""
    stack = [0]
    water = 0
    for i in range(1, len(height)):
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop()
            if stack:
                h = min(height[stack[-1]], height[i]) - height[bottom]
                w = i - stack[-1] - 1
                water += h * w
        stack.append(i)
    return water


def largest_rectangle_area(heights: list[int]) -> int:
    """84. 柱状图中最大的矩形"""
    padded = [0, *heights, 0]
    stack = [0]
    best = 0
    for i in range(1, len(padded)):
        while stack and padded[i] < padded[stack[-1]]:
            height = padded[stack.pop()]
            width = i - stack[-1] - 1
            best = max(best, height * width)
        stack.append(i)
    return best


def find132pattern(nums: list[int]) -> bool:
    """456. 132 模式"""
    stack: list[int] = []
    second = float("-inf")
    for value in reversed(nums):
        if value < second:
            return True
        while stack and value > stack[-1]:
            second = stack.pop()
        stack.append(value)
    return False


def maximal_rectangle(matrix: list[list[str]]) -> int:
    """85. 最大矩形"""
    if not matrix:
        return 0
    cols = len(matrix[0])
    heights = [0] * cols
    best = 0
    for row in matrix:
        for j in range(cols):
            heights[j] = heights[j] + 1 if row[j] == "1" else 0
        best = max(best, largest_rectangle_area(heights))
    return best
