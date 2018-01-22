# 输入数组代表了一系列的直方柱，所有直方柱宽度相同，寻找由直方柱组成的最大矩阵的面积
def find_largest_rectangle(heights):
    if len(heights) < 1:
        return 0
    largest = 0
    # 记录所有未计算矩阵的的左上升沿
    wait_calculate_left = [[0, heights[0]]]
    for i in range(1, len(heights)):
        if heights[i] > heights[i - 1]:
            wait_calculate_left.append([i, heights[i]])
        # 当发现下降沿时：(1)计算所有可计算的未计算矩阵;(2)计算低边所代表的矩阵的左沿，并加入到未计算矩阵行列
        elif heights[i] < heights[i - 1]:
            last_left = None
            while len(wait_calculate_left) > 0:
                if heights[i] < wait_calculate_left[-1][1]:
                    area = (i - wait_calculate_left[-1][0]) * wait_calculate_left[-1][1]
                    largest = max(largest, area)
                    last_left = wait_calculate_left.pop()
                else:
                    break
            if len(wait_calculate_left) == 0:
                wait_calculate_left.append([0, heights[i]])
            elif heights[i] != wait_calculate_left[-1][1]:
                wait_calculate_left.append([last_left[0], heights[i]])
    for column in wait_calculate_left:
        area = (len(heights) - column[0]) * column[1]
        largest = max(largest, area)
    return largest


