import sys
import itertools
from collections import deque
import copy
def bfs(graph,comb,virusindex):
    queue = deque()
    for i in virusindex:
        queue.append((i[0],i[1]))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue:
        x,y = queue.popleft() # 일단 바이러스 인덱스부터 빼고
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx>=N or ny>=M:
                continue # 성립 x
            if graph[nx][ny] == 1:
                continue # 벽이므로 지나가야함
            if graph[nx][ny] == 0: # 만약 비어있다면?
                graph[nx][ny] = 2
                queue.append((nx,ny))
    count = 0
    for i in graph:
        for j in i:
            if j == 0:
                count +=1
    return count


        



N,M = map(int,sys.stdin.readline().split())

graph = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))


zeroindex = []
virusindex = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            zeroindex.append((i,j))
        elif graph[i][j] == 2:
            virusindex.append((i,j))
# zeroindex 배열 안에 인덱스가 0인 것들을 집합
maxValue = 0
comb = list(itertools.combinations(zeroindex,3)) # 이렇게하면 comb 내에 모든 0개중에서 3개를 선택한 경우의수가 들어있다
for i in comb:
    graph2 = copy.deepcopy(graph)
    graph2[i[0][0]][i[0][1]] = 1
    graph2[i[1][0]][i[1][1]] = 1
    graph2[i[2][0]][i[2][1]] = 1
    maxValue = max(maxValue,bfs(graph2,comb,virusindex))

print(maxValue)
