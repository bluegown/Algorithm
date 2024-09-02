import sys
import heapq
INF = 1e9

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    




N,M,C = map(int,sys.stdin.readline().split())
distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y,z = map(int,sys.stdin.readline().split())
    graph[x].append((y,z))# i[0] node i[1] cost
    
dijkstra(C)
count = 0
maxValue = 0
for i in distance:
    if i!=INF:
        count += 1
        maxValue = max(i,maxValue)
print(count-1,maxValue)
