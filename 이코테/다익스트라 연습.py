import sys
import heapq
INF = 1e9


def dijkstra(start):
    distance[start] = 0
    q =[]
    heapq.heappush(q,(0,start))
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
                
N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
distance =  [INF] * (N+1)
