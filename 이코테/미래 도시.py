import sys

def dijkstra(start):
    distance = [[INF * (N+1)] for _ in range(N+1)]
INF = 1e9
N,M = map(int,sys.stdin.readline().split())
graph = [[INF for i in range(N+1)] for _ in range(N+1)]
distance = [[INF for i in range(N+1)] for _ in range(N+1)]


        


for _ in range(M):
    x,y = map(int,sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1 # 거리 설정


for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

x, k = map(int,sys.stdin.readline().split())
dist = graph[1][k] + graph[k][x]
print(graph)
print(dist)


