# 럭키 스트레이트

n = input()

right, left = 0, 0

for i in range(int(len(n) / 2)):
    right += int(n[i])
    left += int(n[-(i + 1)])
    
if right == left:
    print('LUCKY')
else:
    print('READY')


