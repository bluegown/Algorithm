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
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx>=N or ny>=M:
                continue
            if graph[nx][ny] == 1:
             graph[nx][ny] = graph[x][y] + 1
             queue.append((nx,ny))
    return graph[N-1][M-1]
N,M = map(int,sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

print(bfs(graph))
