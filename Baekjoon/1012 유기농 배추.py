import sys
from collections import deque

def bfs(x,y):
     visited[x][y] = True
     queue = deque()
     queue.append((x,y))
     dx = [-1,0,1,0]
     dy = [0,1,0,-1]
     while queue:
      a,b = queue.popleft()
      for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if nx < 0 or ny < 0 or nx>=M or ny>=N:
            continue
        if graph[nx][ny] == 1 and visited[nx][ny] == False:
         visited[nx][ny] = True
         queue.append((nx,ny))
    
               

    

T = int(input())
for _ in range(T):
    M,N,K = map(int,sys.stdin.readline().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]
    visited = [[False for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        x,y = map(int,sys.stdin.readline().split())
        graph[x][y] = 1
    count = 0

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1 and visited[i][j] == False:
                 bfs(i,j)
                 count +=1
    print(count)



