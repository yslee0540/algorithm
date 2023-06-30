# # 피보나치 수열
# d = [0] * 100

# def fibo(x):
#   if x == 1 or x == 2:
#     return 1
#   if d[x] != 0:
#     return d[x]
#   d[x] = fibo(x - 1) + fibo(x - 2)
#   return d[x]

# print(fibo(99))

# # 개미 전사
# # 1 3 1 5 / 8
# n = 4
# array = list(map(int, input().split()))

# d = [0] * 100

# d[0] = array[0]
# d[1] = max(array[0], array[1])
# for i in range(2, n):
#   d[i] = max(d[i - 1], d[i - 2] + array[i])

# print(d[n - 1])

# # 1로 만들기
# # 3
# x = 26

# d = [0] * 30001

# for i in range(2, x + 1):
#   d[i] = d[i - 1] + 1
#   if i % 2 == 0:
#     d[i] = min(d[i], d[i // 2] + 1)
#   if i % 3 == 0:
#     d[i] = min(d[i], d[i // 3] + 1)
#   if i % 5 == 0:
#     d[i] = min(d[i], d[i // 5] + 1)

# print(d[x])

# 효율적인 화폐 구성
# 2 / 3 / 5
# n = 2
# m = 15
# array = []

# for i in range(n):
#   array.append(int(input()))

# d = [10001] * (m + 1)

# d[0] = 0
# for i in range(n):
#   for j in range(array[i], m + 1):
#     if d[j - array[i]] != 10001:
#       d[j] = min(d[j], d[j - array[i]] + 1)

# if d[m] == 10001:
#   print(-1)
# else:
#   print(d[m])

# 금광
# 1 3 3 2 2 1 4 1 0 6 4 7 / 19
# n = 3
# m = 4
# array = list(map(int, input().split()))

# dp = []
# index = 0
# for i in range(n):
#   dp.append(array[index:index + m])
#   index += m

# for j in range(1, m):
#   for i in range(n):
#     #왼쪽 위에서
#     if i == 0:
#       left_up = 0
#     else:
#       left_up = dp[i - 1][j - 1]
#     #완쪽 아래에서
#     if i == n - 1:
#       left_down = 0
#     else:
#       left_down = dp[i + 1][j - 1]
#     #왼쪽에서
#     left = dp[i][j - 1]
#     dp[i][j] = dp[i][j] + max(left_up, left_down, left)
# result = 0
# for i in range(n):
#   result = max(result, dp[i][m - 1])

# print(result)

# 병사 배치하기
# 15 11 4 8 5 2 4 / 2
n = 7
array = list(map(int, input().split()))
array.reverse()

d = [1] * n
for i in range(1, n):
  for j in range(i):
    if array[j] < array[i]:
      d[i] = max(d[i], d[j] + 1)

print(n - max(d))