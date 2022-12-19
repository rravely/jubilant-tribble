# 부품 찾기
# 이진탐색 코드 외워두기

N = int(input())
part = list(map(int, input().split()))
part.sort()

M = int(input())
customer = list(map(int, input().split()))

answer = []

def checkPart(lst, n, start, end):
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == n:
            return mid
        elif lst[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in customer:
    if checkPart(part, i, 0, N -1) == None:
        answer.append('No')
    else:
        answer.append('yes')
    


for i in answer:
    print(i, end=' ')
