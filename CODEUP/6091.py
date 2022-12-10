def solution(a, b, c):
    d=1
    while d%a!=0 or d%b!=0 or d%c!=0:
        d+=1
    return d

a, b, c = map(int, input().split(" "))
print(solution(a, b, c))
