# 이진 탐색
def binary(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary(array, target, start, mid - 1)
  else:
    return binary(array, target, mid + 1, end)

# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary(array, target, 0, n - 1)
# if result == None:
#   print('원소가 존재하지 않음')
# else:
#   print(result + 1)

def binary2(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1

# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary2(array, target, 0, n - 1)
# if result == None:
#   print('원소가 존재하지 않음')
# else:
#   print(result + 1)

# from bisect import bisect_left, bisect_right

# a = [1, 2, 4, 4, 8]
# x = 4

# print(bisect_left(a, x))
# print(bisect_right(a, x))

# 떡볶이 떡 만들기
# 19 15 10 17 / 15
# n = 4
# m = 6
# array = list(map(int, input().split()))

# start = 0
# end = max(array)

# result = 0
# while(start <= end):
#   total = 0
#   mid = (start + end) // 2
#   for x in array:
#     if x > mid:
#       total += x - mid
#   if total < m:
#     end = mid - 1
#   else:
#     result = mid
#     start = mid + 1

# print(result)

# 정렬된 배열에서 특정 수의 개수 구하기
# 1 1 2 2 2 2 3 / 4
n = 7
x = 2

from bisect import bisect_left, bisect_right

def count(array, left, right):
  right_index = bisect_right(array, right)
  left_index = bisect_left(array, left)
  return right_index - left_index

array = list(map(int, input().split()))
count = count(array, x, x)

if count == 0:
  print(-1)
else:
  print(count)