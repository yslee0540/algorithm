#멀쩡한 사각형
import math
def find_square(w,h):
  return w * h - (w + h - math.gcd(w, h))

print(find_square(8, 12))

#하노이탑
def get_hanoi(n):
  answer = []
  def hanoi(n, start, end, sub):
    if n == 1:
      answer.append([start, end])
      return
    else:
      hanoi(n - 1, start, sub, end)
      #가장 큰 원반
      answer.append([start, end])
      hanoi(n - 1, sub, end, start)
  hanoi(n, 1, 3, 2)        
  return answer

print(get_hanoi(3))

#미로탈출
# from collections import deque
def bfs(start, end, maps):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  n = len(maps)
  m = len(maps[0])
  visited = [[False] * m for _ in range(n)]
  q = deque()
  
  for i in range(n):
    for j in range(m):
      if maps[i][j] == start:
        q.append([i, j, 0])
        visited[i][j] = True
        break
    if q:
      break
  
  while q:
    y, x, cnt = q.popleft()
    if maps[y][x] == end:
      return cnt
    
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      
      if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X':
        if not visited[ny][nx]:
          q.append([ny, nx, cnt+1])
          visited[ny][nx] = True
  return -1

def escape(maps):
  path1 = bfs('S', 'L', maps)
  path2 = bfs('L', 'E', maps)
  
  if path1 == -1 or path2 == -1:
    return -1
  return path1 + path2

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
# print(escape(maps))

#리코쳇 로봇
from collections import deque
def ricochet(board):
  n = len(board)
  m = len(board[0])
  
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  q = deque()
  visited = [[False] * m for _ in range(n)]
  
  for i in range(n):
    for j in range(m):
      if board[i][j] == 'R':
        q.append((i, j, 0))
        visited[i][j] = True
  
  while q:
    print(q)
    x, y, cnt = q.popleft()
    if board[x][y] == 'G':
      return cnt
    
    for i in range(4):
      scope = 1
      while True:
        nx = x + dx[i] * scope
        ny = y + dy[i] * scope

        if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] == 'D':
          if not visited[nx-dx[i]][ny-dy[i]]:
            visited[nx-dx[i]][ny-dy[i]] = True
            q.append([nx-dx[i], ny-dy[i], cnt+1])
          break
        scope += 1
  return -1

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(ricochet(board))

#후보키
from itertools import combinations
def candidate(relation):
  row = len(relation)
  col = len(relation[0])
  
  combi = []
  for i in range(1, col+1):
    combi.extend(combinations(range(col), i))
    
  unique = []
  for c in combi:
    tmp = [tuple([item[i] for i in c]) for item in relation]
    if len(set(tmp)) == row:
      unique.append(c)
  
  answer = set(unique)
  for i in range(len(unique)):
    for j in range(i+1, len(unique)):
      if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
        answer.discard(unique[j])
  return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(candidate(relation))