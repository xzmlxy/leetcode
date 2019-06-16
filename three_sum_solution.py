# 找出nums中所有相加为0的三个数
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    data = {}
    length = len(nums)
    for n in range(0, length):
        key = nums[n]
        if key not in data:
            data[key] = [n]
        else:
            data[key].append(n)
    result = []
    k = 0
    old_first = 0
    old_second = 0
    while k < (length - 2):
        first = nums[k]
        if k == 0 or first > old_first:
            old_first = first
            for i in range(k + 1, length - 1):
                second = nums[i]
                if i == (k + 1) or second > old_second:
                    old_second = second
                    third = -first - second
                    if third in data:
                        numbers = data[third]
                        for number in numbers:
                            if number > i:
                                result.append([first, second, third])
                                break
            del data[first]
        k += 1
    return result
