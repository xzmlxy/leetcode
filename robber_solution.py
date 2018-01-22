# 从一个数列中取一些数，这些数必须不能相邻，求这些数的和的最大值
def rob(nums):
    if nums is None or len(nums) == 0:
        return 0
    # 推理可知，该问题的解可按如下过程从1递推至n
    max_list = [nums[0]]
    for i in range(1, len(nums)):
        if i > 2:
            max_list.append(max(nums[i - 1] + max_list[i - 3], nums[i] + max_list[i - 2]))
        elif i == 1:
            max_list.append(max(nums[0], nums[1]))
        elif i == 2:
            max_list.append(max(max_list[1], nums[2] + max_list[0]))
    return max_list[len(nums) - 1]
