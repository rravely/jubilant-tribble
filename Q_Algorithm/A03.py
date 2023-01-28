# 문자열 뒤집기

s = input()

cntOne = 0
cntZero = 0

if s[0] == '1':
    cntOne += 1
else:
    cntZero += 1

for i in range(len(s) - 1):
    if s[i] == '0' and s[i+1] == '1':
        cntOne += 1
    elif s[i] == '1' and s[i+1] == '0':
        cntZero += 1

print(min(cntZero, cntOne))