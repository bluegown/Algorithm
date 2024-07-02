import sys
from collections import deque
def bfs(graph):
    queue = deque()
    queue.append((0,0))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue:
        x,y = queue.popleft()
        if x == N-1 and y == M-1:
            return graph[x][y] # 만약 최초로 발견되면 바로 Return해주는 방식으로 처리한다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx>=N or ny>=M:
                continue
            if graph[nx][ny] == 1:
             graph[nx][ny] = graph[x][y] + 1
             queue.append((nx,ny))

N,M = map(int,sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

print(bfs(graph))
