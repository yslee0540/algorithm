#문자열 내 마음대로 정렬하기
s = ["sun", "bed", "car"]
n = 1
# print(sorted(s, key = lambda x: (x[n], x)))

#문자열 거꾸로
answer = "332211"
# print(answer[::-1])

#가장 가까운 같은 글자
answer = []
d = dict()
s = "banana"
# for i in range(len(s)):
#   if s[i] not in d:
#     answer.append(-1)
#   else:
#     answer.append(i - d[s[i]])
#   d[s[i]] = i

# print(answer)

#추억 점수
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
answer = []
# info = dict(zip(name, yearning))
# for people in photo:
#   score = 0
#   for person in people:
#     score += info.get(person, 0)
#   answer.append(score)
# print(answer)

#카드 뭉치
cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
answer = 'Yes'
# for i in goal:
#   if len(cards1) > 0 and cards1[0] == i:
#     cards1.pop(0)
#   elif len(cards2) > 0 and cards2[0] == i:
#     cards2.pop(0)
#   else:
#     answer = 'No'

# print(answer)

#소수 판별
import math
def is_prime_number(num):
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      return False
  return True

#기사 단원의 무리
number = 5
power = 2
limit = 3

n = []
for i in range(1, number + 1):
  cnt = 0
  for j in range(1, int(i**(1/2)) + 1):
    if i % j == 0:
      cnt += 1 
      if ((j**2) != i) : 
        cnt += 1 
  n.append(cnt)
n = [power if x > limit else x for x in n]
print(sum(n))