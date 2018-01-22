# 数组中每个数字意味着当前位置往后跳跃的最大步数（所以可以小于），是否能从第一个元素开始抵达最后一个元素
def can_jump(nums):
    if len(nums) < 2:
        return True
    else:
        # 从终点开始反推途经点，如果最后的途经点为第一个元素，则返回真
        pass_point_location = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            distance = pass_point_location - i
            if nums[i] >= distance:
                pass_point_location = i
        if pass_point_location == 0:
            return True
        else:
            return False
