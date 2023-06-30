array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# # 선택 정렬
# for i in range(len(array)):
#   min_index = i
#   for j in range(i + 1, len(array)):
#     if array[min_index] > array[j]:
#       min_index = j
#   array[i], array[min_index] = array[min_index], array[i]

# print(array)

# # 삽입 정렬
# for i in range(1, len(array)):
#   for j in range(i, 0, -1):
#     if array[j] < array[j - 1]:
#       array[j], array[j - 1] = array[j - 1], array[j]
#     else:
#       break
# print(array)

# 퀵 정렬
def quick_sort(array, start, end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  while(left <= right):
    while(left <= end and array[left] <= array[pivot]):
      left += 1
    while(right > start and array[right] >= array[pivot]):
      right -= 1
    if(left > right):
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

# quick_sort(array, 0, len(array) - 1)
# print(array)

def quick_sort2(array):
  if len(array) <= 1:
    return array
  pivot = array[0]
  tail = array[1:] # 피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

# print(quick_sort2(array))

# # 계수 정렬
# array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# count = [0] * (max(array) + 1)

# for i in range(len(array)):
#   count[array[i]] += 1

# for i in range(len(count)):
#   for j in range(count[i]):
#     print(i, end=' ')

# 두 배열의 원소 교체
# 1 2 5 4 3 / 5 5 6 6 5 / 26
k = 3
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
   a[i] = b[i]
  else:
    break

print(sum(a))