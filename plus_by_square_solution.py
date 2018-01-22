# 任何正整数都可以由多个数的平方和（可重复）相加而得，求n最少需要由多少个平方和相加得到
def num_squares(self, n):
    if n < 2:
        return n
    elements = []
    i = 1
    while i * i <= n:
        elements.append(i * i)
        i += 1
    cnt = 0
    to_check = {n}
    # 不断获取to_check和各个平方数的残差（保存回to_check）,直至残差为0
    while to_check:
        cnt += 1
        temp = set()
        for x in to_check:
            for y in elements:
                if x == y:
                    return cnt
                if x < y:
                    break
                temp.add(x - y)
        to_check = temp

    return cnt
