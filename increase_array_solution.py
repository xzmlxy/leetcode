# 找到输入数组的最长单调递增数列(算法导论题目)
def find_increase_array(data):
    if len(data) < 2:
        return []
    # 记录当前位置下，最长单调递增子序列的长度
    increase_array_length = [1]
    # 以及该子序列的前一个元素的位置
    last_num_position = [-1]
    max_length = 1
    max_length_position = 0

    for i in range(1, len(data)):
        length = 1
        last_num = -1
        for j in range(0, i):
            if data[i] > data[j]:
                temp = increase_array_length[j] + 1
                if temp > length:
                    last_num = j
                    length = temp
        increase_array_length.append(length)
        last_num_position.append(last_num)
        if length > max_length:
            max_length = length
            max_length_position = i

    result = []
    if max_length > 1:
        result.append(data[max_length_position])
        next_position = last_num_position[max_length_position]
        while next_position != -1:
            result.append(data[next_position])
            next_position = last_num_position[next_position]
        result.reverse()


    print("the sub array is:")
    print(result)
    return result
