# envelopes是一系列套娃的大小，求最多可将多少个套娃套在一起
from time import time


def max_envelopes(envelopes):
    start = time()
    result = 0
    if len(envelopes) > 0:
        result = 1
        # 使用动态规划
        if len(envelopes) > 1:
            envelopes.sort()
            print(envelopes)
            print(time() - start)
            # 以下本质上类似查找最长递增子序列（宽度），网上看到的算法，复杂度为nlgn
            # tails[i]代表将i+1个套娃套一起时，最外层套娃的最小宽度
            tails = []
            i = 0
            while i < len(envelopes):
                # 对高度相同的套娃，按照宽度反序排列，是此处使用查找最长递增子序列算法的关键（防止高度相同但宽度不同的套娃发生嵌套）
                first = i
                while i < len(envelopes) - 1 and envelopes[i + 1][0] == envelopes[first][0]:
                    i += 1
                for j in range(i, first - 1, -1):
                    envelope = envelopes[j]
                    if len(tails) == 0:
                        tails = [envelope[1]]
                        continue
                    left = 0
                    right = len(tails) - 1
                    if envelope[1] > tails[-1]:
                        tails.append(envelope[1])
                    elif envelope[1] <= tails[0]:
                        tails[0] = envelope[1]
                    else:
                        while True:
                            index = int((left + right) / 2)
                            if envelope[1] < tails[index]:
                                right = index
                            elif envelope[1] > tails[index]:
                                left = index
                            else:
                                right = -1
                                break
                            if left == right - 1 or left == right:
                                break
                        if right != -1:
                            tails[right] = envelope[1]
                i += 1
            result = len(tails)
            print(time() - start)
    return result
