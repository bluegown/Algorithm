import sys

def dfs(graph,visited,start):
    global count
    for i in graph[start]:
            if i in bear:
                 count += 1 # 만약 곰을 만났다면 +1만큼 진행
            if len(graph[start]) == 0: # 더이상 진행할 수 없는 경우에 점검
                 if count == 0: # 만약 곰을 만나지 않았다면?
                      return True #"yes"
                 count = 0
            dfs(graph,visited,i)
    return False # "Yes"

N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)  #단방향이므로 하나만 
count = 0

print(graph)
s = int(input())
bear = list(map(int,sys.stdin.readline().split()))
visited = [False] * (N+1)



print(dfs(graph,visited,1))
