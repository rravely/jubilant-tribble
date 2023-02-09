# 탑승구  

g = int(input())
p = int(input())
parent = [0] * (g + 1)

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(1, g + 1):
    parent[i] = i

result = 0
for _ in range(p): # i 대신에 _를 쓰는 이유? i를 이용하지 않아서 
    data = findParent(parent, int(input()))
    if data == 0:
        break
    unionParent(parent, data, data - 1)
    result += 1

print(result)