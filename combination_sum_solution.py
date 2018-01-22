# 将一个数n展开为k个1到9的和，这k个数不可重复，找到所有的展开方式
def combination_sum(k, n):
    if k > 9 or k < 0:
        return []
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    small_total = 0
    for i in range(0, k):
        small_total += num_list[i]
    if small_total > n:
        return []
    if small_total == n:
        return [num_list[0:k]]
    big_total = 0
    for i in range(8, 8 - k, -1):
        big_total += num_list[i]
    if big_total < n:
        return []
    if big_total == n:
        return [num_list[8 - k:9]]
    return move_nums(n - small_total, num_list[0:k], min(n - small_total, 9 - k))


# num_of_increase为需要增加的总增幅，part_of_digits为当前子数列，max_increase为子数列的最后单元的最大增幅
def move_nums(num_of_increase, part_of_digits, max_increase):
    if num_of_increase == 0:
        return [part_of_digits]
    if len(part_of_digits) == 1:
        return [[part_of_digits[0] + num_of_increase]]
    result = []
    min_increase = 1
    # 求出最后单元的最小增幅
    while min_increase * len(part_of_digits) < num_of_increase:
        min_increase += 1
    # 遍历最后单元的不同取值，求此时剩余k-1个单元的组合方式，递归调用之
    while min_increase <= max_increase:
        next_num_of_increase = num_of_increase - min_increase
        temp_result = move_nums(next_num_of_increase, part_of_digits[0:-1],
                                min(next_num_of_increase, min_increase))
        for i in range(0, len(temp_result)):
            temp_result[i].append(min_increase + part_of_digits[-1])
        result.extend(temp_result)
        min_increase += 1
    return result
