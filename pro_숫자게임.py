def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    answer = 0
    while B:
        if B[-1] > A[-1]:
            answer += 1
            B.pop()
            A.pop()
        else:
            B.pop()
    return answer
