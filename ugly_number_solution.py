# ugly number 是只由2,3,5乘得的数字，寻找第n大的ugly number（假设不超过int 范围）
def nth_ugly_number(n):
    ugly = [1]
    index2 = 0
    index3 = 0
    index5 = 0
    factor2 = 2
    factor3 = 3
    factor5 = 5
    for i in range(1, n):
        min_ugly = min(min(factor2, factor3), factor5)
        ugly.append(min_ugly)
        # 可能有多个值都等于min_ugly
        if factor2 == min_ugly:
            index2 += 1
            factor2 = 2 * ugly[index2]
        if factor3 == min_ugly:
            index3 += 1
            factor3 = 3 * ugly[index3]
        if factor5 == min_ugly:
            index5 += 1
            factor5 = 5 * ugly[index5]
    return ugly[n - 1]
