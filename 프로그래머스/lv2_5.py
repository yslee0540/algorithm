#파일명 정렬
answer = []
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

# for file in files:
#   number_check = False
#   head, num, tail = '', '', ''
#   for i in range(len(file)):
#     if file[i].isdigit():
#       num += file[i]
#       number_check = True
#     elif not number_check:
#       head += file[i]
#     else:
#       tail = file[i:]
#       break
#   answer.append((head, num, tail))

# answer.sort(key=lambda x: (x[0].upper(), int(x[1])))
# print([''.join(i) for i in answer])

#숫자 변환하기
def change_num(x, y, n):
  answer = 0
  s = set()
  s.add(x)

  while s:
    if y in s:
      return answer

    nxt = set()
    for i in s:
      if i+n <= y:
        nxt.add(i+n)
      if i*2 <= y:
        nxt.add(i*2)
      if i*3 <= y:
        nxt.add(i*3)
    s = nxt
    print(s)
    answer+=1

  return -1
print(change_num(10, 70, 5))

#전력망을 둘로 나누기
from collections import deque
def bfs(graph, start, visited):
  q = deque([start])
  visited[start] = True
  cnt = 0
  
  while q:
    v = q.popleft()
    cnt += 1
    for i in graph[v]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
  return cnt

def divide_wire(n, wires):
  answer = n - 2
  for i in range(len(wires)):
    tmp = wires.copy()
    graph = [[] for i in range(n+1)]
    visited = [False] * (n+1)
    tmp.pop(i)
    for wire in tmp:
      x, y = wire
      graph[x].append(y)
      graph[y].append(x)
    
    for idx, g in enumerate(graph):
      if g != []:
        start = idx
        break
         
    cnt = bfs(graph, start, visited)
    if abs(n - 2 * cnt) < answer:
        answer = abs(n - 2 * cnt)
  return answer

wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
# print(divide_wire(9, wires))

#줄 서는 방법(순열)
import math
def arrange(n, k):
  answer = []
  n_list = [i for i in range(1, n + 1)]
  k -= 1
  
  while n_list:
    a = k // math.factorial(n - 1)
    answer.append(n_list[a])
    del n_list[a]

    k = k % math.factorial(n - 1)
    n -= 1
  
  return answer

print(arrange(3, 5))

#배달(다익스트라)
import heapq

def delivery(N, road, K):
  answer = 0
  
  graph = [[] for _ in range(N+1)]
  distance = [500001] * (N+1)
  
  for r in road:
    x, y, c = r
    graph[x].append((y, c))
    graph[y].append((x, c))
  
  q = []
  heapq.heappush(q, (0, 1))
  distance[1] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      hr = dist + i[1]
      if hr < distance[i[0]]:
        distance[i[0]] = hr
        heapq.heappush(q, (hr, i[0]))
  
  for d in distance:
    if d <= K:
      answer += 1
  return answer

road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
print(delivery(5, road, 3))

#최대공약수
def gcd(a, b):
  r = b % a
  if r == 0:
      return a
  return gcd(r, a)