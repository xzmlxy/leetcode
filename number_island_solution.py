# 一个矩阵是0的海洋，在这个“海洋”中漂浮着一些1,称之为“岛屿”。相连（上下左右不包括斜线）的1为同一个岛屿，求岛屿的个数
def num_of_islands(grid):
    if grid is None or len(grid) == 0 or grid[0] is None:
        return 0
    m = len(grid) - 1
    n = len(grid[0]) - 1
    islands = 0
    cursor__x = -1
    while cursor__x != m:
        cursor__x += 1
        cursor__y = -1
        while cursor__y != n:
            cursor__y += 1
            if grid[cursor__x][cursor__y] == "1":
                convert(grid, cursor__x, cursor__y, m, n, cursor__x)
                islands += 1

    return islands


def convert(grid, x, y, limit_x, limit_y, min_x):
    grid[x][y] = "0"
    if y < limit_y and grid[x][y + 1] == "1":
        convert(grid, x, y + 1, limit_x, limit_y, min_x)
    if y > 0 and grid[x][y - 1] == "1":
        convert(grid, x, y - 1, limit_x, limit_y, min_x)
    if x < limit_x and grid[x + 1][y] == "1":
        convert(grid, x + 1, y, limit_x, limit_y, min_x)
    if x > min_x and grid[x - 1][y] == "1":
        convert(grid, x - 1, y, limit_x, limit_y, min_x)
