import sys
import copy
from collections import deque
def findMax(graph2):
    global answer
    graph = copy.deepcopy(graph2)

    queue = deque()
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                queue.append((i,j))
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=N or ny>=M:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx,ny))
    for i in range(N):
        count += graph[i].count(0)
    answer = max(count,answer)





def bfs():
    if len(s) == 3:
        findMax(graph)
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                s.append((i,j))
                bfs()
                s.pop()
                graph[i][j] = 0



N,M = map(int,sys.stdin.readline().split())
graph = []
for _ in range(N):
    x = list(map(int,sys.stdin.readline().split()))
    graph.append(x)

s = []
answer = 0
bfs()

print(answer)