
import sys
from collections import deque
import heapq
def bfs(arr,x,y,value):
    count = 0
    queue = deque()
    queue.append((x,y))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited = [[False for _ in range(N+1)] for _ in range(N+1)]
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if x < 0 or y < 0 or x >= N or y >=N:
               continue
            if arr[x][y] == value and visited[x][y] == False:
                visited[x][y] = True
                count +=1
                queue.append((x,y))
    return count
    


    
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))


printarr = []
for k in range(1,11):
    flag = 0
    maxValue = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == k:
                x,y = i,j # 이거로 일단 임의의 점을 잡아주고
                flag = 1
                maxValue = max(maxValue,bfs(arr,x,y,k))
    if flag == 1:
     printarr.append(maxValue)
    else:
     printarr.append(0)

string = ""
for i in printarr:
   string += str(i)
   string += " "
print(string)






    