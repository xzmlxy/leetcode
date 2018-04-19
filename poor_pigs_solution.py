# buckets个水桶中有一个有毒，一头猪喝了毒水后会在minutesToDie内死亡，求在minutesToTest内测出毒水的是哪一桶所需要的猪的头数
import math


def poor_pigs(buckets, minutesToDie, minutesToTest):
    # 一小时内一只猪能验5桶，那么用二维的思路，2只猪应该可以验5 * 5桶：
    # 猪A负责行，猪B负责列，通过2只猪上天的时间能推断出毒水在几行几列。
    # 1  2 3 4 5
    # 6 7 8 9 10
    # 11 12 13 14 15
    # 16 17 18 19 20
    # 21 22 23 24 25
    time = minutesToTest / minutesToDie + 1
    result = 0
    while buckets > math.pow(time, result):
        result += 1
    return result
