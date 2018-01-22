# 把矩阵看成一个“漩涡”，寻找这个“漩涡”的中心
def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    if n == 0:
        return []
    if n == 1:
        return [1]

    data = []
    index = 0;
    for i in range(1, n * n + 1):
        data.append(i)

    begin = 0
    length = n

    result = [[0 for col in range(n)] for row in range(n)]

    while length > 1:
        end = begin + length - 1
        for j in range(begin, end):
            result[begin][j] = data[index]
            index += 1
        for k in range(begin, end):
            result[k][end] = data[index]
            index += 1
        for m in range(end, begin, -1):
            result[end][m] = data[index]
            index += 1
        for l in range(end, begin, -1):
            result[l][begin] = data[index]
            index += 1
        length -= 2
        begin += 1

    if length == 1:
        result[begin][begin] = data[-1]
    return result
