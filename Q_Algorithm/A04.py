# 만들 수 없는 금액
# 시간 엄청 오래 걸림
from itertools import combinations

n = int(input())
coins = list(map(int, input().split()))
coins.sort()
data = set()

for i in range(1, len(coins) + 1):
    for j in combinations(coins, i):
        data.add(sum(j))

result = 1
while True:
    if result in data:
        result += 1
    else:
        break

print(result)