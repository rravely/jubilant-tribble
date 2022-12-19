# 떡볶이 떡 만들기

N, M = map(int, input().split())
dduck = list(map(int, input().split()))


def dduckLength(start, end):
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in dduck:
            if i > mid: # 이거 안하면 음수도 합해져서 구할 수 없음
                total += i - mid

        if total == M:
            return mid
        elif total > M:
            start = mid + 1
        else:
            end = mid - 1

print(dduckLength(0, max(dduck)))
