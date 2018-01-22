from largest_rectangle_solution import find_largest_rectangle

# 给予一个又1和0组成的矩阵，求由1组成的最大长方形的面积
def find_largest(matrix):
    rows = len(matrix)
    if rows == 0:
        return 0
    columns = len(matrix[0])
    if columns == 0:
        return 0
    largest = 0

    # 方法1才需要的步骤
    height_of_1 = []
    last_row = [0] * columns
    for i in range(rows - 1, -1, -1):
        height_of_1_row = []
        for j in range(0, columns):
            if matrix[i][j] == "1":
                height_of_1_row.append(last_row[j] + 1)
            else:
                height_of_1_row.append(0)
        height_of_1.insert(0, height_of_1_row)
        last_row = height_of_1_row

    for i in range(0, rows):
        if (rows - i) * columns <= largest:
            break
        else:
            # 方法1：调用了其他函数,求以某一列为上沿边的矩阵的最大面积
            largest = max(largest, find_largest_rectangle(height_of_1[i]))

            # # 方法2，效率较低
            # j = 0
            # while j < columns:
            #     need_length = largest / (rows - i)
            #     if columns - j < need_length:
            #         break
            #     else:
            #         if matrix[i][j] == "1":
            #             largest = max(largest, find_point_largest(rows, columns, i, j, matrix))
            #         j += 1

    return largest


# 以某点为左上方点的最大长方形面积
def find_point_largest(rows, columns, point_row, point_column, nums):
    result = []
    max_wide = columns - point_column
    for i in range(point_row, rows):
        if nums[i][point_column] == "0":
            # 到达矩阵底部的终止行，则计算一次面积
            result.append(max_wide * (i - point_row))
            break
        temp_wide = 1
        for j in range(point_column + 1, point_column + max_wide):
            if nums[i][j] != "0":
                temp_wide += 1
            else:
                break
        if i == point_row:
            max_wide = temp_wide
        # 非终止行，则仅当“1”出现缩进时，才计算（未缩进行的最大）面积
        elif temp_wide < max_wide:
            result.append(max_wide * (i - point_row))
            max_wide = temp_wide
        # 到达矩阵底部的终止行，则计算一次面积
        if i == rows - 1:
            result.append(max_wide * (i - point_row + 1))
    return max(result)
