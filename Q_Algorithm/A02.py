# 곱하기 혹은 더하기 

s = str(int(input()))

result = int(s[0])

for i in range(1, len(s)):
    if s[i] == '0' or s[i] == '1': # 앞에 있는 0 없애지 않고 하려면 s[i] <= 1 or result <= 1
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)