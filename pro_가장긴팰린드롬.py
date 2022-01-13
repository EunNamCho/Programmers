def solution(s):
    answer = 1
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            front, back = i-1, i+2
            temp = 2
            while front >= 0 and back <= len(s) - 1:
                if s[front] == s[back]:
                    front -= 1
                    back += 1
                    temp += 2
                else:
                    break
            answer = max(answer, temp)
        front, back = i - 1, i + 1
        temp = 1
        while front >= 0 and back <= len(s) - 1:
            if s[front] == s[back]:
                front -= 1
                back += 1
                temp += 2
            else:
                break
        answer = max(answer, temp)
    return answer

