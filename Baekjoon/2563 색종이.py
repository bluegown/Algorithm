import sys

N = int(input())
arr = []

for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    arr.append((x,y))

d = [[0 for _ in range(101)] for _ in range(101)]

for i in range(N):
    for x in range(10):
        for y in range(10):
          d[arr[i][0] +x][arr[i][1]+y] = 1

count = 0
for i in range(101):
    for j in range(101):
        if d[i][j] == 1:
            count += 1

print(count)


