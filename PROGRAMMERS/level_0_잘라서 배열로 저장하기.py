def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str),n)]

my_str = str(input())
n = int(input())
print(solution(my_str, n))