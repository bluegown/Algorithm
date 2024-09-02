import sys

N = int(input())

arr = []

for i in range(N):
    x = list(map(int,sys.stdin.readline().split()))
    arr.append(x)

d = [[(1000*1000)+ 1 for _ in range(3)] for _ in range(N)]

# 원래 그래프는 arr !! 
row = [0,1,2]
for k in range(3):
  start = arr[0][k] # 시작점 다르게 시작하고
  d[0][k] = start 
  for i in range(1,N): # i가 행이 될것.
    for j in range(3):
        if j == 0:# 포함되지 않는다면 
         d[i][0] = min(d[i][0],d[i-1][1] + arr[i][0],d[i-1][2] + arr[i][0])
        if j == 1:# 포함되지 않는다면 
         d[i][1] = min(d[i][1],d[i-1][0] + arr[i][1],d[i-1][2] + arr[i][1])
        if j == 2:# 포함되지 않는다면 
         d[i][2] = min(d[i][2],d[i-1][0] + arr[i][2],d[i-1][1] + arr[i][2])


print(d)









