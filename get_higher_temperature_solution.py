# 数组代表了连续多日的气温，找出再隔多少天的气温会比今天高（否则为0）
def get_high_temperature(temperatures):
    result = [0] * len(temperatures)
    if len(temperatures) > 1:
        # 倒序设置每个值
        for i in range(len(temperatures) - 2, -1, -1):
            compare_day = i + 1
            while temperatures[i] > temperatures[compare_day] and result[compare_day] != 0:
                compare_day += result[compare_day]
                if i == 2:
                    print(str(compare_day))
            if temperatures[i] < temperatures[compare_day]:
                result[i] = compare_day - i
            elif temperatures[i] == temperatures[compare_day]:
                if result[compare_day] == 0:
                    result[i] = 0
                else:
                    result[i] = result[compare_day] + compare_day - i
            else:
                result[i] = 0
    return result
