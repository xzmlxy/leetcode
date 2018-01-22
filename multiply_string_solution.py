# 两个极长数字（字符串）相乘
def multiply_string(s1, s2):
    if s1 == "" or s1 == "0" or s2 == "" or s2 == "0":
        return "0"
    num_list1 = []
    num_list2 = []
    temp_result = [0] * (len(s1) + len(s2))
    true_result = [""] * (len(s1) + len(s2))
    for c in s1:
        num_list1.insert(0, int(c))
    for c in s2:
        num_list2.insert(0, int(c))
    for i in range(0, len(num_list1)):
        for j in range(0, len(num_list2)):
            temp_result[i + j] += num_list1[i] * num_list2[j]
    temp = len(temp_result) - 1
    for i in range(0, temp):
        temp_result[i + 1] += int(temp_result[i] / 10)
        true_result[temp - i] = str(temp_result[i] % 10)
    true_result[0] = str(temp_result[temp])
    result = "".join(true_result)
    if result.startswith("0"):
        result = result[1:]
    return result
