#딕셔너리
t = [1, 3, 2, 5, 4, 5, 2, 3]
# d = {x : t.count(x) for x in t}
# d = sorted(d.items(), key=lambda x: x[1], reverse=True)
# print(d)

#연속 부분 수열 합의 개수
elements = [7,9,1,1,4]
ll = len(elements)
res = set()

for i in range(ll):
  ssum = elements[i]
  res.add(ssum)
  for j in range(i+1, i+ll):
    ssum += elements[j%ll]
    res.add(ssum)

print(res)