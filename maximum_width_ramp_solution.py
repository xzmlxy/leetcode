# 给定一个数列A，如果存在A[j]>=A[i] and j > i;求max(j-i)
def max_width_ramp(A):
    # heads代表了所有可能的i
    heads = [0]
    for i in range(1, len(A)):
        if A[i] <= A[heads[-1]]:
            heads.append(i)
    i = len(heads) - 1
    j = len(A) - 1
    result = 0
    print(heads)
    # 如果A[j] < A[head]，则j-=1，否则满足了条件A[j]>=A[i]；此时如果还满足j > i则计算一次结果，否则i-=1
    while i >= 0:
        if A[heads[i]] <= A[j]:
            if i < j:
                result = max(result, j - heads[i])
            i -= 1
        else:
            j -= 1
    return result
