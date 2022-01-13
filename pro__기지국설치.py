def solution(n, stations, w):
    import math
    answer = 0
    start = 1
    end = n
    for idx, station in enumerate(stations):
        end = station-w-1
        if start == end+1:
            pass
        else:
            length = end - start + 1
            answer += math.ceil(length / (w + w + 1))
        start = station+w+1
        if idx==len(stations)-1:
            length = n - start + 1
            answer += math.ceil(length / (w + w + 1))

    return answer


print(solution(16,[9],2))