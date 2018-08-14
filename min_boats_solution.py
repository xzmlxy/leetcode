def numRescueBoats(people, limit):
    people.sort()
    i = 0
    j = len(people) - 1
    while i < j:
        temp = limit - people[i]
        if people[j] <= temp:
            i += 1
            j -= 1
        else:
            if temp < people[i + 1]:
                break
            else:
                left = i
                right = j
                while left + 1 < right:
                    mid = int((left + right) / 2)
                    if temp < people[mid]:
                        right = mid
                    else:
                        left = mid
                j = left
    return len(people) - i

