import sys
from collections import deque
def bfs(graph,visited):
    visited[1] = True
    queue = deque()
    queue.append(1)
    count = 0


    while queue:
        pop = queue.popleft() # 큐에서 빼낸 원소
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = True

    return count

N = int(input())
i = int(input())

graph = [[] for _ in range(N+1)]


visited = [False] * (N+1)
for _ in range(i):
    x,y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(graph,visited))
