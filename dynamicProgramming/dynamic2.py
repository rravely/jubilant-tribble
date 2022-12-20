# 개미 전사

N = int(input())
data = list(map(int, input().split()))

# DP 테이블 초기화
dp = [0] * 100

dp[0] = data[0]
dp[1] = max(data[0], data[1])
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + data[i])

print(dp[N-1])