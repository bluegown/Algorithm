import sys

X = int(input())

d = [0] * (30001)


for i in range(2,X+1):
    d[i] = d[i-1] + 1 # 1을 뺀 경우
    if i % 2 == 0:
        d[i] = min(d[i//2] + 1 , d[i])
    if i % 3 == 0:
        d[i] = min(d[i//3] + 1,d[i])


print(d[X])