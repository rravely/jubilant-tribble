# 상하좌우
# 5개의 계획이면 1이 2보다 빠르다
import time
t1 = time.time()

N = int(input())
x, y = 1, 1
plan = list(map(str, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for i in plan:
    for j in range(4):
        if i == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny

t2 = time.time()

print(x, y, t2 - t1)