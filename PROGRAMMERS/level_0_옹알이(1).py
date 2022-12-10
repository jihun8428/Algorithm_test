def solution(babbling):
    a = ["aya", "ye", "woo", "ma"]

    answer = 0
    for i in babbling:
        for j in a:
            if i.__contains__(j):
                i = i.replace(j,' ')
        i = i.strip()
        if i == '':
            answer += 1
    return answer

babbling = list(map(str, input().split(',')))
print(solution(babbling))
