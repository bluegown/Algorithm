import sys
from collections import deque
import heapq
INF = 1e9

def djikstra(graph,start):
    distance[start] = 0
    q = []
    heapq.heappush(q,(0,start)) # 0은 비용 start== node number
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist: # 이미 처리된적 있는 노드
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


V,E = map(int,sys.stdin.readline().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))
distance = [INF] * (V+1)

djikstra(graph,K)
for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
