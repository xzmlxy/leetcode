# 判断数组中的所有矩阵是否可以组成一个大矩阵
def isRectangleCover(rectangles):
    """
    :type rectangles: List[List[int]]
    :rtype: bool
    """
    if len(rectangles) == 0:
        return False
    left = rectangles[0][0]
    right = rectangles[0][2]
    top = rectangles[0][3]
    bottom = rectangles[0][1]
    areas = (right - left) * (top - bottom)
    edge_top = [left, right]
    edge_bottom = [left, right]
    dic_list = [{top: [edge_top]}, {bottom: [edge_bottom]}]
    for cell in rectangles[1:]:
        left = min(cell[0], left)
        right = max(cell[2], right)
        bottom = min(cell[1], bottom)
        top = max(cell[3], top)
        areas += (cell[2] - cell[0]) * (cell[3] - cell[1])
        edge_top = [cell[0], cell[2]]
        edge_bottom = [cell[0], cell[2]]
        if cell[3] in dic_list[0]:
            dic_list[0][cell[3]].append(edge_top)
        else:
            dic_list[0][cell[3]] = [edge_top]
        if cell[1] in dic_list[1]:
            dic_list[1][cell[1]].append(edge_bottom)
        else:
            dic_list[1][cell[1]] = [edge_bottom]
    all_area = (right - left) * (top - bottom)
    # 当面积相等时，所有小矩阵的上沿等于所有小矩阵的下沿，则必可组成大矩阵
    if all_area == areas:
        for dic in dic_list:
            for value in dic.values():
                value.sort()
                i = 1
                while i < len(value):
                    if value[i][0] == value[i - 1][1]:
                        value[i - 1][1] = value[i][1]
                        value.pop(i)
                    else:
                        i += 1
        if top in dic_list[0] and bottom in dic_list[1]:
            top_edge = dic_list[0].pop(top)
            bottom_edge = dic_list[1].pop(bottom)
            if top_edge == [[left, right]] == bottom_edge:
                for key in dic_list[0]:
                    if key not in dic_list[1] or dic_list[1][key] != dic_list[0][key]:
                        return False
                return True
    return False
