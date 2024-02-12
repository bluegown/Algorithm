import sys
from itertools import combinations

N,M = map(int,sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))

chicken = []
home = []
count = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken.append((i,j))
            count +=1
        elif graph[i][j] == 1:
            home.append((i,j))

# 각 치킨집에 대하여 모든 집에 대한 거리를 구하고
# 그 뒤에 정렬해서 구하면 될것 같다

chickenCombination = list(combinations(chicken,M))
sumarr = []
for i in chickenCombination:
    sum = 0
    for j in home:
        minValue = 1e9
        for k in range(M):
             minValue = min(minValue,abs(j[0] - i[k][0]) + abs(j[1] - i[k][1]))
        sum += minValue
    sumarr.append(sum)
print(min(sumarr))




