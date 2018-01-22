# 一段长为n的路，每次可走一步或两步，共有多少种不同走法
def step1or2(n):
    if n < 1:
        return 0
    result = 1
    last = 1
    # 走i次两步，n-2i次一步时，不同走法的种数，求和
    for i in range(1, int(n / 2) + 1):
        # 本质上是排列组合问题，此处推导出公式从而减少迭代计算量
        last = last * (n - 2 * i + 2) * (n - 2 * i + 1) / (n - i + 1) / i
        result += last
    return result
