#달리기 경주
callings = ["kai", "kai", "mine", "mine"]
players = ["mumu", "soe", "poe", "kai", "mine"]

answer = {player: i for i, player in enumerate(players)}
for calling in callings:
  i = answer[calling]
  answer[calling] -= 1
  answer[players[i - 1]] += 1
  players[i - 1], players[i] = players[i], players[i - 1]
print(players)