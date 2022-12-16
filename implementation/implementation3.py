# 왕실의 나이트

current = input()
x = int(ord(current[0]) - ord('a')) + 1
y = int(current[1])

count = 0
steps = [(-2, -1), (-2, 1), (2 , -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

for s in steps:
    nx = x + s[0]
    ny = y + s[1]
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <=8:
        count += 1

print(count)