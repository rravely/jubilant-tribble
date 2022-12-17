# 음료수 얼려 먹기

# 얼음틀 입력받기
n, m = map(int, input().split())
iceFrame = []
for i in range(n):
    iceFrame.append(list(map(int, input().split())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 만약 방문하지 않았다면
    if iceFrame[x][y] == 0:
        iceFrame[x][y] = 1 # 방문처리하고
        
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False

answer = 0
for j in range(n):
    for k in range(m):
        if dfs(j, k) == True:
            answer += 1

print(answer)