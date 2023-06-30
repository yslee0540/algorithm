# a = 777
# print(a)

# b = int(1e9)
# print(b)

# a = 0.3 + 0.6
# if a == 0.9:
#   print(True)
# else:
#   print(a)

# # 리스트
# a = [1, 2, 3, 4, 5]
# print(a)

# print(a[-1])
# print(a[2])
# print(a[0:3])

# a[4] = 4
# print(a)

# n = 10
# a = [0] * n
# print(a)

# # 리스트 컴프리헨션
# array = [i for i in range(10)]
# print(array)

# array = [i for i in range(20) if i % 2 == 1]
# print(array)

# array = [[0] * 4 for _ in range(3)]
# print(array)

# array[1][1] = 5
# print(array)

# for _ in range(5):
#   print('Hello World')

# # 기타 메서드
# a = [1, 4, 3]
# print(a)

# a.append(2)
# print(a)

# a.sort()
# print(a)

# a.sort(reverse = True)
# print(a)

# a.insert(2, 3)
# print(a)

# print(a.count(3))

# a.remove(1)
# print(a)

# a = [1, 2, 3, 4, 5, 5, 5]
# remove_set = {3, 5}

# result = [i for i in a if i not in remove_set]
# print(result)

# 문자열
# data = "Don't you know \"Python\"?"
# print(data)

# # 사전 자료형
# data = dict()
# data['사과'] = 'Apple'
# data['바나나'] = 'Banana'
# data['코코넛'] = 'Coconut'
# print(data)

# if '사과' in data:
#   print('"사과"를 키로 가지는 데이터 존재')

# print(data.keys())
# print(data.values())
# print(list(data.keys()))
# print(data['사과'])

# # 집합 자료형
# data = set([1, 1, 2, 3, 4, 5, 5])
# print(data)

# data.update([6, 7])
# print(data)

# # 기본 입출력
# n = int(input())
# data = list(map(int, input().split()))
# data.sort(reverse=True)
# print(data)

# a, b, c = map(int, input().split())
# print(a, b, c)

# import sys

# data = sys.stdin.readline().rstrip()
# print(data)

# answer = 7
# print(f"정답은 {answer}입니다")

# # 조건문
# a = -15

# if a >= 0:
#   print('a >= 0')
# elif a >= -10:
#   print('0 > a >= -10')
# else:
#   print("-10 > a")

# # 반복문
# a = [9, 8, 7, 6, 5]
# for i in a:
#   print(i)

# result = 0
# for i in range(1, 10):
#   if i % 2 == 0:
#     continue
#   result += i
# print(result)

# scores = [90, 85, 77, 65, 97]
# cheating_student = {2, 4}

# for i in range(5):
#     if i + 1 in cheating_student:
#       continue
#     if scores[i] >= 80:
#       print(i + 1, '번 학생은 합격입니다')

# # 함수
# def add(a, b):
#   return a + b
# print(add(3, 7))

# a = 0
# def func():
#   global a
#   a += 1

# for i in range(10):
#   func()

# print(a)

# array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
# result = sorted(array, key=lambda x: x[1])
# print(result)

# 순열
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

# 조합
from itertools import combinations

result = list(combinations(data, 2))
print(result)