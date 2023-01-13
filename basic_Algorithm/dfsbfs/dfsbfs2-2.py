# 미로 탈출

from collections import deque


# 미로 정보 입력받기
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Queue 생성
q = deque()
q.append((0, 0)) # 처음 위치 추가

while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if maze[nx][ny] == 0:
            continue
            
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            q.append((nx, ny))
              
print(maze[-1][-1])