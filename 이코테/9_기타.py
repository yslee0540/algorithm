# 소수 판별
# import math

# def is_prime_number(x):
#     # 2부터 x의 제곱근까지의 모든 수를 확인하며
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True

# print(is_prime_number(4)) # 4는 소수가 아님
# print(is_prime_number(7)) # 7은 소수임


# 에라토스테네스의 체
# n보다 작은 소수
# import math

# n = 1000
# array = [True for i in range(n + 1)]

# for i in range(2, int(math.sqrt(n)) + 1):
#   if array[i] == True:
#     j = 2
#     while i * j <= n:
#       array[i * j] = False
#       j += 1

# for i in range(2, n + 1):
#   if array[i]:
#     print(i, end=" ")


# 투포인터
# n = 5
# m = 5 # 찾고자 하는 부분합
# data = [1, 2, 3, 2, 5]

# count = 0
# interval_sum = 0
# end = 0

# for start in range(n):
#   while interval_sum < m and end < n:
#     interval_sum += data[end]
#     end += 1
#   if interval_sum == m:
#     count += 1
#   interval_sum -= data[start]

# print(count)


# 구간 합
n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]
for i in data:
  sum_value += i
  prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])