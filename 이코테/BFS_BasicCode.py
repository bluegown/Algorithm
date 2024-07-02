from collections import deque # 외워두기 !!!! 중요함 
def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v,end=" ")
        for i in graph[v]: # 인접한 노드들에 대한 조사
            if not visited[i]: # 인접한 노드가 방문되지 않았다면
                queue.append(i) # 큐에 추가 
                visited[i] = True # 그리고 방문 처리

graph = [[], [2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False] * 9

bfs(graph,1,visited)