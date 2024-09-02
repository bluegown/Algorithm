import sys
from collections import deque
INF = 1e9

def bfs(graph,X):
    distance[X] = 0 # 시작점은 거리 0
    queue = deque([X])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i]!=INF:
                continue
            else:
                distance[i] = distance[v] + 1
                queue.append(i)
    return distance

N,M,K,X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
bfs(graph,X)
if distance.count(K) == 0:
    print(-1)
else:
 for i in range(len(distance)):
    if distance[i] == K:
        print(i)