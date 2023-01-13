# 상하좌우

import time
t1 = time.time()

N = int(input())
plan = list(map(str, input().split()))

current = [1, 1]

for i in range(len(plan)):
    if plan[i] == 'L' and current[1] != 1:
        current[1] -= 1
    elif plan[i] == 'R' and current[1] != N:
        current[1] += 1
    elif plan[i] == 'U' and current[0] != 1:
        current[0] -= 1
    elif plan[i] == 'D' and current[0] != N:
        current[0] += 1

t2 = time.time()

print(current, t2 - t1)