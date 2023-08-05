#숫자 짝꿍
X = "12321"
Y = "42531"

def solution(X, Y):
    answer = []
    for i in (set(X)&set(Y)) :
        for j in range(min(X.count(i), Y.count(i))) :
            answer.append(i)
    if len(answer) == 0:
        return "-1"
    elif answer[0] == "0":
        return "0"
    return "".join(sorted(answer, reverse=True))

# print(solution(X, Y))
# print(set(X)&set(Y))

#완주하지 못한 선수
# import collections
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
# answer = collections.Counter(participant) - collections.Counter(completion)
# print(answer)
# print(list(answer.keys())[0])

#대충 만든 자판(딕셔너리)
keymap = ["ABACD", "BCEFD"]
keytable = {}
# for keys in keymap:
#   for i, key in enumerate(keys):
#     if key not in keytable:
#       keytable[key] = i + 1
#     else:
#       keytable[key] = min(keytable[key], i + 1)

# print(keytable)

#아스키코드
print(ord('a'))
print(chr(65))