import sys
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] *(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0 # 갈일 없는 경유지 ㅠㅠ

for _ in range(m):
    a,b,cost = map(int,sys.stdin.readline().split())
    graph[a][b] = cost # 각각의 노드들에 대해 설정

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)