# 정렬된 배열에서 특정 수의 개수 구하기
# 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과.
# count 함수의 시간 복잡도는 O(N)

N, x = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

result = binary_search(data, x, 0, N - 1)

cnt = 1
front, back = result, result

if result == None:
    print(-1)
else:
    while (data[front] == x or data[back] == x):
        front -= 1
        back += 1
        if data[front] == x:
            cnt += 1
        if data[back] == x:
            cnt += 1

    print(cnt)
