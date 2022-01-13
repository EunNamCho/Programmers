def solution(n, works):
    import heapq
    answer = 0
    heap = []
    for work in works:
        heapq.heappush(heap, (-work, work))
    while n:
        rank, value = heapq.heappop(heap)
        if value > 0:
            value -= 1
            rank = -value
        heapq.heappush(heap, (rank, value))
        n -= 1
    for elem in heap:
        if elem[1] > 0:
            answer += elem[1] ** 2
    return answer


print(solution(4, [3,1,4,5,2]))
