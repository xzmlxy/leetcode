# nums是一个整数序列，[lower,upper]是一个闭区间。求：在nums中存在多少个子序列，其元素之和落在该区间内（算法复杂度要求小于n平方）


def count_range_sum(nums, lower, upper):
    if upper < lower or len(nums) == 0:
        return 0
    sum_dict = {nums[0]: 1}
    sums = [nums[0]]
    temp_sum = nums[0]
    total = 0

    # 计算包含第1个元素的所有序列的和，放入字典
    for i in range(1, len(nums)):
        temp_sum += nums[i]
        sums.append(temp_sum)
        if temp_sum in sum_dict:
            sum_dict[temp_sum] += 1
        else:
            sum_dict[temp_sum] = 1

    for i in range(lower, upper + 1):
        if i in sum_dict:
            total += sum_dict[i]

    # 当需要求不包含第1个元素的子序列的和，并和区间上下限对比时，改变区间范围即可，本质上是一样的
    for i in range(0, len(nums) - 1):
        lower += nums[i]
        upper += nums[i]
        if sum_dict[sums[i]] > 0:
            sum_dict[sums[i]] -= 1
        else:
            sum_dict.pop(sums[i])
        for j in range(lower, upper + 1):
            if j in sum_dict:
                total += sum_dict[j]
    return total
