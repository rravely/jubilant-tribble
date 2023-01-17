# 플로이드

n = int(input())
m = int(input())

INF = 1e9
bus = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            bus[a][b] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    if c < bus[a][b]:
        bus[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            bus[a][b] = min(bus[a][b], bus[a][k] + bus[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if bus[a][b] == INF:
            print(0, end=' ')
        else:
            print(bus[a][b], end=' ')
    print()



