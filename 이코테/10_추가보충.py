# 우선순위 큐
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

# n = int(input())
# arr = []

# for i in range(n):
#   arr.append(int(input()))

# res = heapsort(arr)
# for i in range(n):
#   print(res[i])


# 트리
'''
[예시 입력]
7
A B C
B D E
C F G
D None None
E None None
F None None
G None None
[예시 출력]
A B D E C F G / D B E A F C G / D E B F G C A 
'''
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# # 전위 순회(Preorder Traversal)
# def pre_order(node):
#     print(node.data, end=' ')
#     if node.left_node != None:
#         pre_order(tree[node.left_node])
#     if node.right_node != None:
#         pre_order(tree[node.right_node])

# # 중위 순회(Inorder Traversal)
# def in_order(node):
#     if node.left_node != None:
#         in_order(tree[node.left_node])
#     print(node.data, end=' ')
#     if node.right_node != None:
#         in_order(tree[node.right_node])

# # 후위 순회(Postorder Traversal)
# def post_order(node):
#     if node.left_node != None:
#         post_order(tree[node.left_node])
#     if node.right_node != None:
#         post_order(tree[node.right_node])
#     print(node.data, end=' ')

# n = int(input())
# tree = {}

# for i in range(n):
#     data, left_node, right_node = input().split()
#     if left_node == "None":
#         left_node = None
#     if right_node == "None":
#         right_node = None
#     tree[data] = Node(data, left_node, right_node)

# pre_order(tree['A'])
# print()
# in_order(tree['A'])
# print()
# post_order(tree['A'])

      
# 벨만 포드
# 음수 간선 포함되어 있을 때
# import sys
# input = sys.stdin.readline
# INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# # 노드의 개수, 간선의 개수를 입력받기
# n, m = map(int, input().split())
# # 모든 간선에 대한 정보를 담는 리스트 만들기
# edges = []
# # 최단 거리 테이블을 모두 무한으로 초기화
# distance = [INF] * (n + 1)

# # 모든 간선 정보를 입력받기
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
#     edges.append((a, b, c))

# def bf(start):
#     # 시작 노드에 대해서 초기화
#     distance[start] = 0
#     # 전체 n - 1번의 라운드(round)를 반복
#     for i in range(n):
#         # 매 반복마다 "모든 간선"을 확인하며
#         for j in range(m):
#             cur_node = edges[j][0]
#             next_node = edges[j][1]
#             edge_cost = edges[j][2]
#             # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
#                 distance[next_node] = distance[cur_node] + edge_cost
#                 # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
#                 if i == n - 1:
#                     return True
#     return False

# negative_cycle = bf(1) # 1번 노드가 시작 노드

# if negative_cycle:
#     print("-1")
# else:
#     # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리를 출력
#     for i in range(2, n + 1):
#         # 도달할 수 없는 경우, -1을 출력
#         if distance[i] == INF:
#             print("-1")
#         # 도달할 수 있는 경우 거리를 출력
#         else:
#             print(distance[i])


# 바이너리 인덱스 트리
# import sys
# input = sys.stdin.readline

# # 데이터의 개수(n), 변경 횟수(m), 구간 합 계산 횟수(k)
# n, m, k = map(int, input().split())

# # 전체 데이터의 개수는 최대 1,000,000개
# arr = [0] * (n + 1)
# tree = [0] * (n + 1)

# # i번째 수까지의 누적 합을 계산하는 함수
# def prefix_sum(i):
#     result = 0
#     while i > 0:
#         result += tree[i]
#         # 0이 아닌 마지막 비트만큼 빼가면서 이동
#         i -= (i & -i)
#     return result

# # i번째 수를 dif만큼 더하는 함수
# def update(i, dif):
#     while i <= n:
#         tree[i] += dif
#         i += (i & -i)

# # start부터 end까지의 구간 합을 계산하는 함수
# def interval_sum(start, end):
#     return prefix_sum(end) - prefix_sum(start - 1)

# for i in range(1, n + 1):
#     x = int(input())
#     arr[i] = x
#     update(i, x)

# for i in range(m + k):
#     a, b, c = map(int, input().split())
#     # 업데이트(update) 연산인 경우
#     if a == 1:
#         update(b, c - arr[b]) # 바뀐 크기(dif)만큼 적용
#         arr[b] = c
#     # 구간 합(interval sum) 연산인 경우
#     else:
#         print(interval_sum(b, c))


# 최소 공통 조상
import sys
sys.setrecursionlimit(int(1e5)) # 런타임 오류를 피하기 위한 재귀 깊이 제한 설정

n = int(input())

parent = [0] * (n + 1) # 부모 노드 정보
d = [0] * (n + 1) # 각 노드까지의 깊이
c = [0] * (n + 1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)] # 그래프(graph) 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[y] = x
        dfs(y, depth + 1)

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # 먼저 깊이(depth)가 동일하도록
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0) # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))