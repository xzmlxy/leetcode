import heapq


# target为目的地的距离, startFuel为开始时携带的油量, stations为路过的加油站的位置以及可加的油量，求最少需要停车加油多少次能到达目的地
def min_refuel_stops(target, startFuel, stations):
    currentFuel = startFuel
    can_reach_stations = []
    reached_stations_num = 0
    result = 0
    # 不断寻找在可达范围内加油最多的加油站
    while currentFuel < target:
        for i in range(reached_stations_num, len(stations)):
            if stations[i][0] <= currentFuel:
                heapq.heappush(can_reach_stations, -stations[i][1])
                # can_reach_stations.append(stations[i][1])
                reached_stations_num += 1
        if len(can_reach_stations) == 0:
            return -1
        currentFuel += -heapq.heappop(can_reach_stations)
        # temp = max(can_reach_stations)
        # currentFuel += temp
        # can_reach_stations.remove(temp)
        result += 1
    return result
