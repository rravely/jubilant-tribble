# 위에서 아래로

# 정렬할 수 입력받기
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

# 정렬
data = sorted(data, reverse=True)

# 출력
for j in data:
    print(j, end=' ')