from collections import deque
import pprint
def solution(N, road, K):
    def bfs(town, time, K):
        D = deque()
        t = deque()
        for i in range(N):
            if matrix[town][i] and time + matrix[town][i] <= K:
                try:
                    if visited[i]:
                        if visited[i] > time + matrix[town][i]:
                            visited[i] = time+matrix[town][i]
                            t.append(time+matrix[town][i])
                            D.append(i)
                except:
                    visited[i] = time+matrix[town][i]
                    t.append(time+matrix[town][i])
                    D.append(i)
        for i in range(len(D)):
            bfs(D[i], t[i], K)
    visited = dict()
    visited[0] = 0
    matrix = [[0]*N for _ in range(N)]
    for path in road:
        if matrix[path[1]-1][path[0]-1]:
            matrix[path[0]-1][path[1]-1] = min(matrix[path[0]-1][path[1]-1],path[2])
            matrix[path[1]-1][path[0]-1] = min(matrix[path[1]-1][path[0]-1],path[2])
        else:
            matrix[path[0] - 1][path[1] - 1] = path[2]
            matrix[path[1] - 1][path[0] - 1] = path[2]
    bfs(0,0,K)
    return len(visited)

print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))