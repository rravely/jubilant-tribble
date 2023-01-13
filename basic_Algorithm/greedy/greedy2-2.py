# 2<=N<=1000, 1<=M<=10000, 1<=K<=10000인 자연수
# N개의 자연수가 주어지는데 1 이상 10000 이하
# 입력으로 주어지는 K는 항상 M보다 작거나 같다
# 2-1보다 느리다

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

result = 0

count = int(m / (k + 1)) * k
count += m % (k + 1)

result += (count) * first
result += (m - count) * second

print(result)
