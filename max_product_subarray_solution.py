# 寻找一个子列，使其乘积为最大（数据中不存在负数）,求此最大值
def max_product(nums):
    result = nums[0]
    before_max = result
    for i in range(1, len(nums)):
        # before_max是第i个数之前的最大乘积，判断这个乘积是否大于1
        before_max = max(nums[i], before_max * nums[i])
        result = max(result, before_max)
    return result
