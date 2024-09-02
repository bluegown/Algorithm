import sys
def convert(x):
    if x == 'A':
        x = 1
    if x == 'B':
        x = 2
    if x == 'C':
        x = 3
    if x == 'D':
        x = 4
    if x == 'E':
        x = 5
    if x == 'F':
        x = 6
    if x == 'G':
        x = 7
    if x == 'H':
        x = 8

    return x

def reconvert(x):
    if x == 1:
        return 'A'
    if x == 2:
        return 'B'
    if x == 3:
        return 'C'
    if x == 4:
        return 'D'
    if x == 5:
        return 'E'
    if x == 6:
        return 'F'
    if x == 7:
        return 'G'
    if x == 8:
        return 'H'




location = list(sys.stdin.readline().split())

king = location[0]
rock = location[1]
N = int(location[2])
v = convert(king[0])
nx = int(v)
ny = int(king[1])
v = convert(rock[0])
rockx = int(v)
rocky = int(rock[1])
for _ in range(N):
    move = input()
    if move == 'R':
        if nx == 8:
            continue
        nx = nx + 1
        ny = ny
        if nx == rockx and ny == rocky:
            if rockx == 8:
                nx = nx - 1 # 원래 위치로 돌려주고
                continue
            rockx = rockx + 1
    if move == 'L':
        if nx == 1:
            continue
        nx = nx - 1
        ny = ny
        if nx == rockx and ny == rocky:
            if rockx == 1:
                nx = nx + 1 # 원래 위치로 돌려주고
                continue
            rockx = rockx - 1
    if move == 'B':
        if ny == 1:
            continue
        nx = nx
        ny = ny - 1# 한칸 아래
        if nx == rockx and ny == rocky:
            if rocky == 1:
                ny = ny + 1 # 원래 위치로 돌려주고 멈춘다
                continue
            rocky = rocky - 1
    if move == 'T':
        if ny == 8:
            continue
        ny = ny + 1
        if nx == rockx and ny == rocky:
            if rocky == 8:
                ny = ny - 1 # 원래 위치로 돌려준다
                continue
            rocky = rocky +1
    if move == 'RT':
        if nx == 8 or ny == 8:
            continue
        nx = nx + 1
        ny = ny + 1
        if nx == rockx and ny == rocky:
            if rockx == 8 or rocky == 8:
                nx -=1
                ny -=1
                continue
            rockx +=1
            rocky +=1
    if move == 'LT':
        if nx == 1 or ny == 8:
            continue
        nx -=1
        ny +=1
        if nx == rockx and ny == rocky:
            if rockx == 1 or rocky == 8:
                nx +=1
                ny -=1
                continue
            rockx -=1
            rocky +=1
    if move == 'RB':
        if nx == 8 or ny == 1:
            continue
        nx +=1
        ny -=1
        if nx == rockx and ny == rocky:
            if rockx == 8 or rocky == 1:
                nx -=1
                ny +=1
                continue
            rockx +=1
            rocky -=1
    if move == 'LB':
        if nx == 1 or ny == 1:
            continue
        nx -=1
        ny -=1
        if nx == rockx and ny == rocky:
            if rockx == 1 or rocky == 1:
                nx +=1
                ny +=1
                continue
            rockx -=1
            rocky -=1


nx = reconvert(nx)
rockx = reconvert(rockx)

str1= nx + str(ny)
str2 = rockx + str(rocky)
print(''.join(str1))
print(''.join(str2))

