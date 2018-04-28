# 求单次最大收益
def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0
    profit = 0
    low = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < low:
            low = prices[i]
        elif prices[i] > low:
            temp = prices[i] - low
            if temp > profit:
                profit = temp
    return profit


# 求多次总收益
def all_max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) < 2:
        return 0
    profit = 0
    for i in range(1, len(prices)):
        temp = prices[i] - prices[i - 1]
        if temp > 0:
            profit += temp
    return profit


# 求两次最大收益（不重复）
def two_max_profit(prices):
    if len(prices) < 2:
        return 0
    profit_max = 0
    cursor = 0
    # 分别代表取单次最大差值时的买入日期和卖出日期
    max_left_num = 0
    max_right_num = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[cursor]:
            cursor = i
        elif prices[i] > prices[cursor]:
            temp = prices[i] - prices[cursor]
            if temp > profit_max:
                profit_max = temp
                max_left_num = cursor
                max_right_num = i
    if profit_max == 0:
        return 0
    # 分析可知，买入卖出两次的最大值，只可能存在于下述两种情况下:(1)两次最大收益包含了单次最大收益(2)两次最大收益处于单次最大收益之内。
    profit_left = max_profit(prices[0:max_left_num])
    profit_right = max_profit(prices[max_right_num:len(prices)])
    result = profit_max + max(profit_left, profit_right)
    if max_right_num - max_left_num > 2:
        profit_max2 = 0
        largest = prices[max_left_num + 1]
        for j in range(max_left_num + 2, max_right_num):
            if prices[j] < largest:
                temp = largest - prices[j]
                if temp > profit_max2:
                    profit_max2 = temp
            elif prices[j] > largest:
                largest = prices[j]
        profit_max2 += profit_max
        # 求这两种情况的大者即可
        result = max(result, profit_max2)
    return result


# 求K次最大收益（不重复）
def k_max_profit(k, prices):
    if len(prices) < 2 or k < 1:
        return 0
    if k >= len(prices) / 2:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        return profit

    table = [[0] * len(prices)]

    # table[i, j]代表了在前j天操作i次的最大收益
    # table[i, j] = max(table[i][ j - 1], prices[j] - prices[some] + table[i - 1, some])
    # max函数中的前者表示第j天不交易的情况，后者表示第j天交易的情况（some可为1到j-1的任意值）

    for i in range(1, k + 1):
        element_table = [0]
        # tmp_max 即为当前i和j下的max(table[i - 1, some] - prices[some])
        tmp_max = -prices[0]
        for j in range(1, len(prices)):
            element_table.append(max(element_table[j - 1], prices[j] + tmp_max))
            # 使用动态规划的关键，随着j的增加不断更新tmp_max
            tmp_max = max(tmp_max, table[i - 1][j] - prices[j])
        table.append(element_table)
    return table[k][len(prices) - 1]
