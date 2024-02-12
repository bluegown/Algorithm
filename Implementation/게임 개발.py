import sys
# sys.stdin.readline()
import heapq
import copy
import itertools
from itertools import combinations
from itertools import permutations
from collections import deque
sys.setrecursionlimit(100000000)
INF = 1e9
       
def turn():
    global direction
    direction -=1
    if direction == -1:
        direction = 3

N,M = map(int,sys.stdin.readline().split())
graph = []
row,col,direction = map(int,sys.stdin.readline().split())
for _ in range(M):
    graph.append(list(map(int,sys.stdin.readline().split())))
graph[row][col] = -1
count = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while True:
    countsea = 0
    for _ in range(4):
        turn()
        nx = row + dx[direction]
        ny = col + dy[direction]
        if nx < 0 or ny < 0 or nx >=N or ny >=M:
            continue
        if graph[nx][ny] == 0:
            row = nx
            col = ny # 현재 위치 최신화 하고
            count +=1
            graph[nx][ny] = -1 # 방문은 -1로 변경
            break # 보이는대로 하고 for문을 빠져나올 수 있다.
        else:
            countsea +=1
    if countsea == 4:
        turn()
        turn()
        if graph[row + dx[direction]][col + dy[direction]] == 1:
            break
print(count)

    


    
    
    

        

        



    


    
    


