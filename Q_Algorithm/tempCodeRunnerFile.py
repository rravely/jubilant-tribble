# 문자열 뒤집기

s = input()

cntOne = 0
cntZero = 0

for i in range(len(s) - 1):
    if s[i] == '0' and s[i+1] == '1':
        cntOne += 1
    elif s[i] == '1' and s[i+1] == '0':
        cntZero += 1

if cntZero == 0 and cntOne == 0:
    print(0)
elif cntOne * cntZero == 0:
    print(max(cntZero, cntOne))
else:
    print(min(cntOne, cntZero))