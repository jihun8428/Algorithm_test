def solution(n):
    ans = 0
    for i in range(1,n+1):
        while i != 0:
            a = i % 10
            if a != 0 and a % 3 == 0:
                ans += 1
            i //= 10

    return ans

n = int(input())
print(solution(n))