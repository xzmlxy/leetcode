# 在数组中寻找一个数，其左边的数字之和与右边的数字之和相等，存在返回该数位置，不存在返回-1（默认首个数字的左侧、最后数字的右侧为0）
def find_pivot(nums):
    if len(nums) > 0:
        total = sum(nums)
        left_sum = 0
        for i in range(0, len(nums)):
            if left_sum * 2 + nums[i] == total:
                return i
            left_sum += nums[i]
        return -1
    return -1
