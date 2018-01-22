# 在一个m宽n长的矩形区域中，从左上角到达右下角的不同最短路径有多少（无法斜向运动）
class Solution(object):
    def num_of_paths(self, m, n):
        if m < 1 or n < 1:
            return 0
        path_gra = [[0] * n] * m
        for i in range(0, m):
            path_gra[i][0] = 1
        for i in range(1, n):
            path_gra[0][i] = 1
        # 每个节点的路径数都是左侧和上侧节点的路径数之和
        for i in range(1, m):
            for j in range(1, n):
                path_gra[i][j] = path_gra[i - 1][j] + path_gra[i][j - 1]
        return path_gra[m - 1][n - 1]
