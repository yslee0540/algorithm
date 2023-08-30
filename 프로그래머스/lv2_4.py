#타겟 넘버
# from itertools import product
# numbers = [1, 1, 1, 1, 1]
# target = 3

# l = [(x, -x) for x in numbers]
# s = list(map(sum, product(*l)))
# print(s)
# print(s.count(target))

#10진수 - k진수
n = 437674
k = 3
rev_base = ''
# while n > 0:
#     rev_base += str(n % k)
#     n //= k
# print(rev_base[::-1])

def convert(num, base):
  arr = "0123456789ABCDEF"
  q, r = divmod(num, base)
  if q == 0:
    return arr[r]
  else:
    return convert(q, base) + arr[r]

# print(convert(15, 16))

#더 맵게(힙)
import heapq
sc = [1, 2, 9, 3, 10, 12]
K = 7
heapq.heapify(sc)
print(sc)

answer = 0
while sc[0] < K:
    heapq.heappush(sc, heapq.heappop(sc) + heapq.heappop(sc) * 2)
    answer += 1
    
    if len(sc) == 1 and sc[0] < K:
      print(-1)
      break
print(answer)