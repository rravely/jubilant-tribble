# 효율적인 화폐 구성
# 1 <= n <= 100, 1 <= m <= 10,000

n, m = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))

money.sort()

# dp 테이블 생성
dp = [0] * (m + 1) # 범위가 10000 이하라고 꼭 10001개 만들 필요는 없음
for i in range(len(money)):
    dp[money[i]] = 1


for i in range(money[0], m + 1):
    if dp[i-money[0]] != 0:
        dp[i] = dp[i-money[0]] + 1
    for j in range(len(money)):
        if i % money[j] == 0:
            dp[i] = min(dp[i], i // money[j])

if dp[m] == 0:
    print(-1)
else:
    print(dp[m])