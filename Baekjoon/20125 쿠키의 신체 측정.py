import sys

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))
# 결과값에 다 1씩 더해주면 된다
graphindex = []

for i in range(len(graph)):
    count = 0
    for j in range(len(graph[i])):
        if graph[i][j] == '*':
            graphindex.append((i,j))
            if (1<=i<=N-2 and 1<=j<=N-2) and graph[i+1][j] == graph[i][j+1] == graph[i-1][j] == graph[i][j-1] == '*':
              heartx,hearty = i,j
heartx2,hearty2 = heartx,hearty
print(heartx+1,hearty+1)

leftarm = 0 
rightarm = 0
leftleg = 0
rightleg = 0
mid = 0
index = hearty - 1
while 0<=index<=N-1 and graph[heartx][index] == '*':
    if graph[heartx][index] == '*':
        leftarm +=1
        index -= 1
index = hearty + 1
while 0<=index<=N-1 and graph[heartx][index] =='*':
    if graph[heartx][index] == '*':
        rightarm +=1
        index +=1
index = heartx + 1
while 0<=index<=N-1 and graph[index][hearty] == '*':
    if graph[index][hearty] == '*':
        midx, midy = index,hearty
        mid +=1
        index +=1
        
leftx, lefty = midx + 1, midy - 1
rightx, righty = midx + 1, midy + 1

index = leftx
while 0<=index<=N-1 and graph[index][lefty] == '*':
    if graph[index][lefty] == '*':
        leftleg +=1
        index +=1

index = rightx
while 0<=index<=N-1 and graph[index][righty] == '*':
    if graph[index][righty] == '*':
        rightleg +=1
        index +=1
print(leftarm,rightarm,mid,leftleg,rightleg,end=' ')
        










    


            


