def solution(A, B):
    answer = 0
    a = list(A)
    for i in range(len(a)):
        if "".join(a) == B:
            return answer
        else:
            a.insert(0, a.pop())
            answer += 1
    return -1
A = str(input())
B = str(input())
print(solution(A, B))

