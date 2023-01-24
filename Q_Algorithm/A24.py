# 안테나

n = int(input())
data = list(map(int, input().split()))

data.sort()

# 중간값에서 벗어나면 거리의 총합이 증가. 따라서 정렬 후 중간값을 출력하면 됨
# print(data[(n - 1) // 2])

def sumLength(targetIndex, data):
    sum = 0
    for d in data:
        sum += abs(d - data[targetIndex])
    return sum

def findMinSum(targetIndex):
    minSum = sumLength(targetIndex, data)
    
    if sumLength(targetIndex - 1, data) < minSum:
        return findMinSum(targetIndex - 1)
    elif sumLength(targetIndex + 1, data) < minSum:
        return findMinSum(targetIndex + 1)
    else:
        return data[targetIndex]

if n == 1:
    print(data[0])
else:
    print(findMinSum(n // 2 - 1))
