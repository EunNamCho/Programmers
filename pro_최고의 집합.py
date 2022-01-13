import sys
import math

def solution(n, s):
    if n > s:
        return [-1]
    q = s // n
    r = s % n
    answer = [q] * n
    i = -1
    while r:
        answer[i] += 1
        i -= 1
        r -= 1
    return answer