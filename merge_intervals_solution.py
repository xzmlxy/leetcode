# 给予一组区间，合并其中重合的部分，返回合并后的区间列表


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge(intervals):
    result = []
    if intervals is not None and len(intervals) > 0:
        intervals.sort(key=cmp_interval)
        count = 0
        result.append(intervals[0])
        for interval in intervals[1:]:
            if result[count].end >= interval.start:
                if result[count].end < interval.end:
                    result[count].end = interval.end
            else:
                result.append(interval)
                count += 1
    return result


def cmp_interval(x):
    return x.start
