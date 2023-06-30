# # 거스름돈
# n = 1260
# count = 0

# array = [500, 100, 50, 10]

# for coin in array:
#   count += n // coin
#   n %= coin

# print(count)

# # 1이 될 때까지
# n = 25
# k = 3
# count = 0

# while True:
#   target = (n // k) * k
#   count += (n - target)
#   n = target
#   if n < k:
#     break
#   count += 1
#   n //= k

# count += (n - 1)
# print(count)

# # 곱하기 혹은 더하기
# data = input()
# result = int(data[0])

# for i in range(1, len(data)):
#   num = int(data[i])
#   if num <= 1 or result <= 1:
#     result += num
#   else:
#     result *= num

# print(result)

# #모험가 길드
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# result = 0
# count = 0 #현재 그룹에 포함된 모험가의 수

# for i in data:
#   count += 1
#   if count >= i:
#     result += 1
#     count = 0
# print(result)

# # 상하좌우
# # 5 / R R R U D D
# # 3 4

# n = int(input())
# x, y = 1, 1
# plans = input().split()

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# for plan in plans:
#   for i in range(len(move_types)):
#     if plan == move_types[i]:
#       nx = x + dx[i]
#       ny = y + dy[i]
#   if nx < 1 or ny < 1 or nx > n or ny > n:
#     continue
#   x, y = nx, ny

# print(x, y)

# # 시각
# # 11475
# n = 5

# count = 0
# for i in range(n + 1):
#   for j in range(60):
#     for k in range(60):
#       if '3' in str(i) + str(j) + str(k):
#         count += 1
# print(count)

# #왕실의 나이트
# #2
# data = 'a1'
# row = int(data[1])
# column = int(ord(data[0]) - int(ord('a'))) + 1

# steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]
# result = 0

# for step in steps:
#   next_row = row + step[0]
#   next_column = column + step[1]
#   if 1 <= next_row <= 8 and 1 <= next_column <= 8:
#     result += 1

# print(result)

#문자열 재정렬
#ABCKK13
data = 'K1KA5CB7'
result = []
value = 0

for x in data:
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)

result.sort()
if value != 0:
  result.append(str(value))

print(''.join(result))