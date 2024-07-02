import sys

def dfs(x,y):
    if x < 0 or y < 0 or x>=N or y>=M:
        return False # 조건에 위배되므로 False를 반환해준다.
    if graph[x][y] == 0:
        graph[x][y] = 1 # 1으로 바꿔주고
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False



N,M = map(int,sys.stdin.readline().split())
graph = []

for i in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))
count = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j)== True:
            count +=1




