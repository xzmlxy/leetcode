# 判断数组中是否按序存在这样的三个数组合：第一个最小，第二个最大而第三个居中，这个三数位置无需紧邻


def find132pattern(nums):
    if len(nums) < 3:
        return False
    # 典型的堆栈应用思维，储存满足动态阙值的数据（不断的pop和push）
    second_stack = []
    third = min(nums)
    # 随着数据的反向遍历，不断提升third的大小；stack起到了记录seconds的作用，当发现更大的数时，second即可转变为third
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < third:
            return True
        elif nums[i] > third:
            while len(second_stack) > 0 and second_stack[-1] < nums[i]:
                third = second_stack.pop()
            second_stack.append(nums[i])
    return False
