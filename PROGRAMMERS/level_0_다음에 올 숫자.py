common = []
def solution(common):
    answer = 0
    a = common[1] - common[0]
    if common[1] + a == common[2]:
        answer = common[len(common)-1] + a
    else:
        a = common[1] // common[0]
        answer = common[len(common)-1] * a
    return answer

common = list(map(int, input().split(" ")))
print(solution(common))

#a = [1,2,3,4,5]
#print(len(a))
