# 寻找重复的数字（仅一个）
def find_duplicate(nums):
    if len(nums) < 2:
        return -1
    map_num = {}
    for i in range(0, len(nums)):
        if nums[i] in map_num:
            return nums[i]
        else:
            map_num[nums[i]] = 1
    return -1
