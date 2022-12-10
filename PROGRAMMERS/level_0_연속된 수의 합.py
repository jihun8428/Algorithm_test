def solution(num, total):
    answer = []
    for i in range(num):
        answer.append(0)
        for j in range(num):
            answer[j] += 1

    return answer
num = int(input())
total = int(input())
print(solution(num, total))