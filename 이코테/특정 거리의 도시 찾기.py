import sys
from collections import deque
def bfs(graph,distance,start):
    distance[start] = 0
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]: # v에서 갈 수 있는 노드들에 대해서 
            if distance[i] == INF: # 만약 방문하지 않은 노드라면,
                distance[i] = distance[v] + 1 # 1만큼 더해주고
                queue.append(i)

INF = 1e9
N,M,K,X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
# 왜 graph = [] * (N+1)은 안되지
for i in range(M):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y) # x->y로 연결시켜준다

distance =  [INF] * (N+1)
bfs(graph,distance,X)
disarr = []
for i in range(len(distance)):
    if distance[i] == K:
        disarr.append(i)
if len(disarr) == 0:
    print(-1)
else:
    disarr.sort()
    for i in disarr:
        print(i)
