import sys
def dfs(graph,v,visited):
    visited[v] = True 
    print(v,end=" ")

    for i in graph[v]: # 자신의 노드와 연결된 노드를 탐색하며
        if not visited[i]: # 그 노드들이 방문되지 않았다면(순차적으로 정렬되어있다는 전제)
            dfs(graph,i,visited)

graph = [[], [2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False] * 9

dfs(graph,1,visited)