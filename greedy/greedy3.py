# 숫자 카드 게임

n, m = map(int, input().split())
v, answer = 0, 0
for i in range(n):
    v = min(list(map(int, input().split())))
    if v > answer:
        answer = v

print(answer)
