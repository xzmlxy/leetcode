# height代表一组高低不平的地面，问最大的积水量是多少
def calculate_water(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) < 3:
        return 0

    # manager right end
    last_island = []
    right = 0
    for i in range(len(height) - 2, 0, -1):
        if height[i] < height[i + 1]:
            last_island = [i + 1, -1, height[i + 1]]
            right = i + 1
            break

    if right == 0:
        return 0

    result = 0
    islands = []
    left_edge = 0
    highest = 0
    highest_island_location = []

    for i in range(1, right):
        if height[i] < height[i - 1] and left_edge != -1:
            new_island = [left_edge, i, height[i - 1]]
            islands.append(new_island)
            if height[i - 1] > highest:
                highest_island_location = []
                highest = height[i - 1]
            if height[i - 1] == highest:
                highest_island_location.append(len(islands) - 1)
            left_edge = -1
        elif height[i] > height[i - 1]:
            left_edge = i

    islands.append(last_island)
    if last_island[2] > highest:
        highest_island_location = []
        highest = last_island[2]
    if last_island[2] == highest:
        highest_island_location.append(len(islands) - 1)

    print(highest_island_location)
    print(islands)

    if len(islands) > 1:

        if highest_island_location[0] != 0:
            left_island = islands[0]
            for i in range(1, highest_island_location[0] + 1):
                if islands[i][2] >= left_island[2]:
                    water_height = min(left_island[2], islands[i][2])
                    for j in range(left_island[1], islands[i][0]):
                        cell = water_height - height[j]
                        if cell > 0:
                            result += (water_height - height[j])
                    left_island = islands[i]

        if highest_island_location[-1] != len(islands) - 1:
            right_island = islands[-1]
            for i in range(len(islands) - 2, highest_island_location[-1] - 1, -1):
                if islands[i][2] >= right_island[2]:
                    water_height = min(right_island[2], islands[i][2])
                    for j in range(islands[i][1], right_island[0]):
                        cell = water_height - height[j]
                        if cell > 0:
                            result += (water_height - height[j])
                    right_island = islands[i]

        if len(highest_island_location) > 1:
            start = islands[highest_island_location[0]][1]
            end = islands[highest_island_location[-1]][0]
            for j in range(start, end):
                result += (highest - height[j])

    return result
