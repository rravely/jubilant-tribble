# 곱하기 혹은 더하기 

n = str(int(input()))

result = int(n[0])

for i in range(1, len(n)):
    if n[i] == '0' or n[i] == '1': # 앞에 있는 0 없애지 않고 하려면 n[i] <= 1 or result <= 1
        result += int(n[i])
    else:
        result *= int(n[i])

print(result)