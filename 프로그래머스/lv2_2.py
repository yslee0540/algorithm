#할인 행사
# from collections import Counter

discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]

answer = 0
# check = {}
# for w, n in zip(want, number):
#   check[w] = n

# for i in range(len(discount)-9):
#   c = Counter(discount[i:i+10])
#   if c == check:
#     answer += 1

#위장
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
hash_map = {}
# for clothe, type in clothes:
#   hash_map[type] = hash_map.get(type, 0) + 1
# print(hash_map)

#튜플
answer = []
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s1 = s.lstrip('{').rstrip('}').split('},{')
print(s1)
new_s = []
for i in s1:
  new_s.append(i.split(','))
print(new_s)
new_s.sort(key = len)

for i in new_s:
  for j in range(len(i)):
    if int(i[j]) not in answer:
      answer.append(int(i[j]))