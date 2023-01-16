from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

N, x = map(int, input().split())
data = list(map(int, input().split()))

count = count_by_range(data, x, x)

if count == 0:
    print(-1)
else:
    print(count)