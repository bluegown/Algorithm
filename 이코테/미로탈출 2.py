import sys
from collections import deque
def bfs(graph):
    queue = deque()
    queue.append((0,0))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = int(x) + dx[i]
            ny = int(y) + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
             graph[nx][ny] = int(graph[x][y]) + 1
             queue.append((nx,ny))
    return graph[N-1][M-1]
N,M = map(int,sys.stdin.readline().split())
graph = []
for _ in range(N):
    x = list(map(int,input()))
    graph.append(x)

print(bfs(graph))