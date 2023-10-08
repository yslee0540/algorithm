#프로세스
priorities = [2, 1, 3, 2]
location = 2

queue =  [(i,p) for i,p in enumerate(priorities)]
print(queue)
answer = 0
while True:
  cur = queue.pop(0)
  print(cur)
  if any(cur[1] < q[1] for q in queue):
    queue.append(cur)
  else:
    answer += 1
    if cur[0] == location:
      print(answer)
      break

#순위 검색(이진 탐색)
from itertools import combinations
from bisect import bisect_left

def rank(info, query):
  answer = []
  info_dict = {}
  
  for i in range(len(info)):
    info2 = info[i].split()
    condition = info2[:-1]
    score = int(info2[-1])
    
    for j in range(5):
      for c in combinations(condition, j):
        tmp = ''.join(c)
        if tmp in info_dict:
          info_dict[tmp].append(score)
        else:
          info_dict[tmp] = [score]
  
  for k in info_dict:
    info_dict[k].sort()
  
  for q in query:
    q = q.replace("and ", "").replace("- ", "")
    q2 = q.split()
    key = ''.join(q2[:-1])
    target_score = int(q2[-1])
    
    count = 0
    if key in info_dict:
      scores = info_dict[key]
      idx = bisect_left(scores, target_score)
      count = len(scores) - idx
    answer.append(count)
  return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(rank(info, query))