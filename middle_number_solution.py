# 寻找另个已排列列表的中位数
def find_median_sorted_arrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # 当某个数据为空时
    length1 = len(nums1)
    length2 = len(nums2)
    if length1 == 0 or length2 == 0:
        if length1 == 0 and length2 == 0:
            return None
        if length1 == 0:
            numbers = nums2
        else:
            numbers = nums1
        if len(numbers) % 2 == 0:
            temp = len(numbers) / 2
            return (numbers[temp] + numbers[temp - 1]) / 2
        else:
            return numbers[int(len(numbers) / 2)]

    # 将两列数据等长
    start1 = 0
    start2 = 0
    max_small = None
    min_large = None
    d_value = int(abs(length2 - length1) / 2)
    if length1 > length2:
        short = nums2
        long = nums1
    else:
        short = nums1
        long = nums2
    end1 = len(short) - 1
    end2 = len(long) - 1
    if d_value > 0:
        start2 = d_value
        end2 -= d_value
        max_small = long[start2 - 1]
        min_large = long[end2 + 1]
    # 循环缩短
    while end1 != start1:
        temp = (end1 - start1 + 1)
        decrease = int(temp / 2)
        if temp % 2 == 0:
            middle1 = (short[start1 + decrease - 1] + short[start1 + decrease]) / 2
        else:
            middle1 = short[start1 + decrease]
        temp = (end2 - start2 + 1)
        temp2 = int(temp / 2)
        if temp % 2 == 0:
            middle2 = (long[start2 + temp2 - 1] + long[start2 + temp2]) / 2
        else:
            middle2 = long[start2 + temp2]
        if middle1 == middle2:
            return middle1
        else:
            if middle1 > middle2:
                end1 -= decrease
                start2 += decrease
                if max_small is None:
                    max_small = long[start2 - 1]
                    min_large = short[end1 + 1]
                else:
                    max_small = max(long[start2 - 1], max_small)
                    min_large = min(short[end1 + 1], min_large)
            else:
                start1 += decrease
                end2 -= decrease
                if max_small is None:
                    max_small = short[start1 - 1]
                    min_large = long[end2 + 1]
                else:
                    max_small = max(short[start1 - 1], max_small)
                    min_large = min(long[end2 + 1], min_large)
    # 获取中位数
    if end2 != start2:
        if short[start1] <= long[start2]:
            return long[start2]
        elif long[end2] <= short[start1]:
            return long[end2]
        else:
            return short[start1]
    else:
        if min_large is None:
            return (short[start1] + long[start2]) / 2
        else:
            max_small = max(min(short[start1], long[start2]), max_small)
            min_large = min(max(short[start1], long[start2]), min_large)
            return (max_small + min_large) / 2
