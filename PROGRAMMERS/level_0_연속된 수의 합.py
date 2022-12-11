def solution(num, total):
    average = total // num
    return [i for i in range(average - (num-1)//2, average + (num + 1)//2)]

num = int(input())
total = int(input())
print(solution(num, total))
