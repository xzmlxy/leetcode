# 判断是否能完成24点
def judge_point24(nums):
    if len(nums) != 4:
        return False
    for i in range(1, len(nums)):
        factor1 = result_of_four([nums[0]], [nums[i]])
        if i == 1:
            other = [nums[2], nums[3]]
        elif i == 2:
            other = [nums[1], nums[3]]
        else:
            other = [nums[1], nums[2]]
        factor2 = result_of_four([other[0]], [other[1]])
        # 当选定的两个数先进行运算后，存在以下三种情况
        if judge_of_four(factor1, factor2):
            return True
        factor3 = result_of_four(factor1, [other[0]])
        if judge_of_four(factor3, [other[1]]):
            return True
        factor3 = result_of_four(factor1, [other[1]])
        if judge_of_four(factor3, [other[0]]):
            return True
        # 当不被选定的另两个数先进行运算后，（排除已被检查过的情况）还存在以下两种情况
        factor3 = result_of_four(factor2, [nums[0]])
        if judge_of_four(factor3, [nums[i]]):
            return True
        factor3 = result_of_four(factor2, [nums[i]])
        if judge_of_four(factor3, [nums[0]]):
            return True
    return False


def result_of_four(a, b):
    result = []
    for i in a:
        for j in b:
            result.extend(four(i, j))
    return result


# 计算合成的两个数能否得到24点
def judge_of_four(a, b):
    for i in a:
        for j in b:
            temp = four(i, j)
            for num in temp:
                # 因为在除的过程中可能出现小数，所以最后的结果也可能是不精确的小数
                if abs(24 - num) < 0.01:
                    return True
    return False


# 四则运算的6个不同结果
def four(a, b):
    temp = [a + b, a * b, a - b, b - a]
    if a != 0:
        temp.append(b / a)
    if b != 0:
        temp.append(a / b)
    return temp
