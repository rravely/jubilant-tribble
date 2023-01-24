# 고정점 찾기

n = int(input())
data = list(map(int, input().split()))

def findFixedPoint(data, start, end):
    while start <=  end:
        mid = (start + end) // 2
        if mid == data[mid]:
            return mid
        elif mid < data[mid]:
            end = mid - 1
        elif mid > data[mid]:
            start = mid + 1
    return -1

print(findFixedPoint(data, 0, n - 1))