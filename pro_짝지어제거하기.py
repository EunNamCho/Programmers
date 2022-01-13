def solution(s):
    stack = []
    for char in s:
        try:
            if stack[-1] == char:
                del stack[-1]
            else:
                stack.append(char)
        except:
            stack.append(char)
    if stack:
        return 0
    else:
        return 1
