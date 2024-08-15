import sys
from collections import deque
def bfs(graph,x,y):
    queue = deque(virus)
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    count = 0
    while queue:
        if count == s:
            break
        for i in range(len(queue)):
            index, row, col = queue.popleft()
            for i in range(4):
             nx = row + dx[i]
             ny = col + dy[i]
             if nx < 0 or ny < 0 or nx >=N or ny>=N:
                continue
             if graph[nx][ny] == 0:
                graph[nx][ny] = graph[row][col] 
                queue.append((graph[nx][ny],nx,ny))
        count +=1
    return graph[x-1][y-1]



N,K = map(int,sys.stdin.readline().split())
graph = []
virus = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
    for j in range(N):
        if graph[i][j]!=0:
            virus.append(((graph[i][j],i,j)))

s,x,y = map(int,sys.stdin.readline().split())
virus.sort()
# x,y는 좌표 / s는 경과한 초
print(bfs(graph,x,y))

