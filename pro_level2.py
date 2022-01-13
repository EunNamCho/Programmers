from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        if len(people) == 1:
            answer += 1
            break
        elif people[-1] + people[0] <= limit:
            del people[-1]
            del people[0]
            answer += 1
        else:
            del people[-1]
            answer += 1
    return answer

print(solution([70, 50, 80],100))