# 국영수 

n = int(input())
students = []

for i in range(n):
    tmp = list(map(str, input().split()))
    tmp[1] = int(tmp[1])
    tmp[2] = int(tmp[2])
    tmp[3] = int(tmp[3])
    students.append(tmp)

students.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
# student.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(students[i][0])
