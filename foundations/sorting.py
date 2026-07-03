def quick_sort(array: list[int], left: int, right: int) -> None:
    if left >= right:
        return
    low = left
    high = right
    key = array[low]   # 设置一个key存储
    while left < right:
        while left < right and array[right] > key:  # 找到第一个小于key的index
            right -= 1
        array[left] = array[right]  # 将index移到左边
        while left < right and array[left] <= key:  # 找到第一个大于key的index
            left += 1
        array[right] = array[left]  # 将index移到右边
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


if __name__ == "__main__":
    nums = [2, 4, 1, 5, 7, 3, 8, 2]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)



