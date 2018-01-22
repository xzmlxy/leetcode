# 在一个环形公路上存在多个加油站，问能否驶完全程（起始点任选）
def can_complete_circuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    start = 0
    rest = gas[start] - cost[start]
    if len(gas) > 1:
        if rest < 0:
            start = len(gas) - 1
            end = 0
            forward = False
        else:
            start = 0
            end = 1
            forward = True
        while start != end:
            if forward:
                rest += gas[end] - cost[end]
            else:
                rest += gas[start] - cost[start]
            if rest < 0:
                forward = False
                if start == 0:
                    start = len(gas) - 1
                else:
                    start -= 1
            else:
                forward = True
                if end == len(gas) - 1:
                    end = 0
                else:
                    end += 1
    if rest >= 0:
        return start
    return -1
