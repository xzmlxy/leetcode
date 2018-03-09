# 二维数组matrix由0或1组成，返回的二维数组，代表了每个元素距最近的0元素的距离
def calculate_distance(matrix):
    height = len(matrix)
    width = len(matrix[0])
    queue = []
    for i in range(0, height):
        for j in range(0, width):
            if matrix[i][j] == 0:
                queue.append([i, j])
            else:
                matrix[i][j] = -1
    for element in queue:
        if element[1] > 0 and matrix[element[0]][element[1] - 1] == -1:
            matrix[element[0]][element[1] - 1] = matrix[element[0]][element[1]] + 1
            queue.append([element[0], element[1] - 1])
        if element[1] < width - 1 and matrix[element[0]][element[1] + 1] == -1:
            matrix[element[0]][element[1] + 1] = matrix[element[0]][element[1]] + 1
            queue.append([element[0], element[1] + 1])
        if element[0] > 0 and matrix[element[0] - 1][element[1]] == -1:
            matrix[element[0] - 1][element[1]] = matrix[element[0]][element[1]] + 1
            queue.append([element[0] - 1, element[1]])
        if element[0] < height - 1 and matrix[element[0] + 1][element[1]] == -1:
            matrix[element[0] + 1][element[1]] = matrix[element[0]][element[1]] + 1
            queue.append([element[0] + 1, element[1]])
    return matrix
