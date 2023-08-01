# #자릿수 더하기
# n = 123
# answer = list(map(int, str(n)))
# print(answer)
# print(sum(answer))

# #평균 구하기
# arr = [1,2,3,4]
# print(sum(arr) / len(arr))

# #자연수 뒤집어 배열로 만들기
# n = 12345
# print(list(map(int, reversed(str(n)))))

# #문자열 내 p와 y의 개수
# s = "pPoooyY"
# print(s.lower().count('p') == s.lower().count('y'))

#정수 제곱근 판별
# import math
# n = 121
# print(n**(1/2))
# print(math.sqrt(n))

# #정수 내림차순으로 배치하기
# n = 118372
# n = list(str(n))
# n.sort(reverse=True)
# answer = int("".join(n))
# print(answer)

#두 정수 사이의 합
# a = 5
# b = 3
# if a > b:
#     a, b = b, a
# print(sum(range(a, b + 1)))

# #서울에서 김서방 찾기
# seoul = ["Jane", "Kim"]
# for i in range(len(seoul)):
#   if seoul[i] == 'Kim':
#     print('김서방은 ' + str(i) + '에 있다')

# print("김서방은 {}에 있다".format(seoul.index('Kim')))

#없는 숫자 더하기
numbers = [1,2,3,4,6,7,8,0]
answer = 0
for i in range(10):
  if i not in numbers:
    answer += i
print(answer)