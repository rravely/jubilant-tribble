# 성적이 낮은 순서로 학생 출력하기

N = int(input())
data = []
for i in range(N):
    tmp = input().split()
    data.append([tmp[0], int(tmp[1])])
        

data = sorted(data, key = lambda x: x[1])

for j in range(N):
    print(data[j][0], end=' ')