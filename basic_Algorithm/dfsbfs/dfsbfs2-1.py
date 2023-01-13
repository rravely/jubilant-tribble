# 미로 탈출
# 방문하지 않은 곳의 값이 1이므로 꼭 확인하지 않아도 된다 => 2-2

from collections import deque


# 미로 정보 입력받기
n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))

# 방문확인
v = [[0] * m for _ in range(n)]
v[0][0] = 1

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

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if v[nx][ny] == 0 and maze[nx][ny] == 1:
                maze[nx][ny] += maze[x][y]
                v[nx][ny] = 1
                q.append((nx, ny))
              
print(maze[-1][-1])