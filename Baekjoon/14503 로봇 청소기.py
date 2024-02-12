import sys
def turn_left():
    global direction
    direction -=1
    if direction == -1:
        direction = 3

N,M = map(int,sys.stdin.readline().split())
x,y,direction = map(int,sys.stdin.readline().split())
graph = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 0,1,2,3 -> 북,동,남,서
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
count = 0

breaknumber = 0
while breaknumber == 0:
    flag = 0
    if graph[x][y] == 0:
        count +=1
        graph[x][y] = 2 # 1번 조건 . 현재 칸 청소
    for i in range(4): # 이제 2,3번 조건 turn around
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx < 0 or ny < 0 or nx >= N or ny >=M:
            continue
        if graph[nx][ny] == 0:
            count +=1
            flag = 1 # 3번 조건
            graph[nx][ny] = 2 # 청소 완
            x,y = nx,ny
            break # for // break
       
    if flag == 0: # 만약 청소되지 않은 빈칸이 없다?
        direction2 = direction
        nx = x + dx[(direction2 + 2) % 4]
        ny = y + dy[(direction2 + 2) % 4] # 후진으로 이동
        if nx < 0 or ny < 0 or nx >=N or ny >=M or graph[nx][ny] == 1:
            breaknumber = 1 # 여기서 작동 중단
        x,y = nx,ny
print(count)

        




        





        




