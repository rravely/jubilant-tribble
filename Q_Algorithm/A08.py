# 문자열 재정렬

string = input()
slist = []
sum = 0

for s in string:
    if 65 <= ord(s) <= 90: # 또는 s.isalpha() 
        slist.append(s)
    else:
        sum += int(s)

slist.sort()

for i in slist:
    print(i, end='')
if sum != 0: print(str(sum))

'''
if sum != 0:
    slist.append(str(sum))

print(''.join(slist))
'''