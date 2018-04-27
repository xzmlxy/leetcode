# 给定一个字符串和一个字符C，求S中各个字符到C的最近距离（S中必然包含）


def shortest_to_char(S, C):
    result = [0] * len(S)
    first_c = 0
    while S[first_c] != C:
        first_c += 1
    result[first_c] = 0
    for i in range(0, first_c):
        result[i] = first_c - i
    for i in range(first_c + 1, len(S)):
        if S[i] != C:
            result[i] = result[i - 1] + 1
        else:
            for j in range(int((first_c + i + 1) / 2), i):
                result[j] = i - j
            result[i] = 0
            first_c = i
    return result
