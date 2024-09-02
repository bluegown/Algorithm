import sys
from collections import deque
import heapq

def djikstra(graph,start):
    q = []
    heapq.heappush(q,(0,start)) # i[0]는 거리 , i[1]은 노드
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                cost = distance[i[0]]
                heapq.heappush(q,(cost,i[0]))
            


INF = 1e9
n,m = map(int,sys.stdin.readline().split()) # 노드와 간선
start = int(input())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

distance = [INF] * (n+1)