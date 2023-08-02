#가운데 글자 가져오기
# s = "qwer"
# print(s[0] + s[1])
# answer = ''
# l = int(len(s) / 2)
# if len(s) % 2 == 0:
#     answer = s[l - 1] + s[l]
# else:
#     answer = s[l]

# print(answer)

#내적
# a = [1,2,3,4]
# b = [-3,-1,0,2]

# print(sum([x*y for x, y in zip(a,b)]))

# for i in range(len(a)):
#   a[i] = a[i] * b[i]
#   print(a)
# print(sum(a))

#약수의 개수와 덧셈
# answer = 0
# left = 13
# right = 17
# for i in range(left, right + 1):
#   num = 0
#   for j in range(1, i + 1):
#       if i % j == 0:
#           num += 1
#   if num % 2 == 0:
#     answer += i
#   else:
#     answer -= i

# print(answer)

#문자열 내림차순
# s = "Zbcdefg"
# print(''.join(reversed(sorted(s))))
# print(''.join(sorted(s, reverse=True)))

#문자열 확인
# s = "a123"
# print(s.isdigit())

#행렬의 덧셈
# A = [[1,2],[2,3]]
# B = [[3,4],[5,6]]
# print(len(A))
# print([[c + d for c, d in zip(a,b)] for a, b in zip(A,B)])

# #최소공배수, 최대공약수
# gcd = lambda a,b : b if not a%b else gcd(b, a%b)
# lcm = lambda a,b : a*b//gcd(a,b)
# print([gcd(2, 5), lcm(2, 5)])

#3진법 뒤집기
# n = 125
# tmp = ''
# while n:
#     tmp += str(n % 3)
#     n = n // 3

# answer = int(tmp, 3)
# print(tmp)
# print(answer)

#시저 암호(아스키코드)
# s = "AB"
# n = 1
# s = list(s)
# for i in range(len(s)):
#     if s[i].isupper():
#         s[i] = chr((ord(s[i]) - ord('A')+ n) % 26 + ord('A'))
#     elif s[i].islower():
#         s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

# print( "".join(s))

#숫자 문자열과 영단어
# s = "one4seveneight"

# num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# for i in range(len(num)):
#     s = s.replace(num[i], str(i))
# print(int(s))

#비밀지도(십진수 - 이진수)
print(format(16, 'b'))
print(bin(16)[2:])