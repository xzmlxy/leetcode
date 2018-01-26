# 有一个m*n的矩阵，每个元素的值为当前行数与当前列数的乘积，求第K大的值


def find_k_number(m, n, k):
    if k <= 1:
        return 1
    if k >= m * n:
        return m * n

    # 以最右边的一列数字作为划分数值区间的标准，求出第K小的数所在的区间
    above_row_index = 0
    below_row_index = m
    index = int((m + 1) / 2)
    while index != below_row_index and index != above_row_index:
        temp = n * index
        number_count = index * n
        if number_count > k:
            below_row_index = index
        else:
            for i in range(index + 1, min(m, temp) + 1):
                number_count += int(temp / i)
            if number_count > k:
                below_row_index = index
            elif number_count < k:
                above_row_index = index
            else:
                return temp
        index = int((above_row_index + below_row_index) / 2)

    # start和end分别代表该区间的数在每一行的开始位置和结束位置，用于辅助获取该区间的所有数
    start = list()
    end = [n]
    if below_row_index == 1:
        for i in range(2, min(m, n) + 1):
            end.append(int(n / i))
        start = [0] * len(end)
        true_k = k
    else:
        temp = above_row_index * n
        for i in range(above_row_index + 1, min(m, temp) + 1):
            start.append(int(temp / i))
        temp += n
        for i in range(below_row_index + 1, min(m, temp) + 1):
            end.append(int(temp / i))
        true_k = k - sum(start) - n * above_row_index
        start.extend([0] * (len(end) - len(start)))

    # 获取该区间的所有数并排序
    count_map = {}
    index = above_row_index
    for i in range(0, len(start)):
        index += 1
        for j in range(start[i] + 1, end[i] + 1):
            temp = j * index
            if temp in count_map:
                count_map[temp] += 1
            else:
                count_map[temp] = 1
    count_list = sorted(count_map.keys())
    total = 0

    for k in count_list:
        total += count_map[k]
        if total >= true_k:
            return k
