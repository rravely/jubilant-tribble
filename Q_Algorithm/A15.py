# 특정 거리의 도시 찾기

n, m, k, x = map(int, input().split())
data = []
path = [0] * (n + 1)
v = [0] * (n + 1)

# 단방향 도로 정보 입력받기
for i in range(m):
    tmp = list(map(int, input().split()))
    data.append(tmp)

stack = []
stack.append(x)

while len(stack) != 0:
    tmp = stack.pop()

    for i in data:
        if tmp == i[0] and v[i[1]] == 0:
            stack.append(i[1])
            path[i[1]] = path[i[0]] + 1
            v[i[1]] = 1

result = []

for i in range(len(path)):
    if path[i] == k:
        result.append(i)

if len(result) == 0:
    print('-1')
else:
    for i in result:
        print(i, end='\n')
