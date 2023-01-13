# 게임 개발

n, m = map(int, input().split())
# 현재 위치와 바라보는 방향 북쪽(0), 동쪽(1), 남쪽(2), 서쪽(3)
x, y, direction = map(int, input().split())
# 맵 정보
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))
# 방문 정보와 현재 위치 방문 처리
v = [[0] * m for _ in range(n)]
v[x][y] = 1

# 방향(북동남서 순)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
#dx = [-1, 0, 1, 0]
#dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 캐릭터가 방문한 칸의 수
count = 1
# 현재 자리에서 회전한 수 
turn_time = 0

while True:
    turnLeft()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if v[nx][ny] == 0 and maps[nx][ny] == 0:
        v[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
        

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if maps[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
