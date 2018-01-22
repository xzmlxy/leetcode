# 一个已排序（递增）的数列，可能会在某个位置将其分为二两部分并对调位置，寻找该数列的最小值
# 该数列不存在相等的元素


def find_minimum(nums):
    if len(nums) == 1:
        return nums[0]
    left = 0
    right = len(nums) - 1
    if nums[left] < nums[right]:
        return nums[left]
    while True:
        if right - left == 1:
            return nums[right]
        center = int((right + left) / 2)
        if nums[center] > nums[left]:
            left = center
        else:
            right = center
