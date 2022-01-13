import itertools
import time
def solution(n, k):
    t = time.time()
    answer = [i for i in range(1, n+1)]
    answer = itertools.permutations(answer)
    for i in range(k-1):
        next(answer)
    print(time.time()-t)
    return next(answer)

print(solution(1000,10002010))