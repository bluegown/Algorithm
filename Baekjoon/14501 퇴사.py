import sys

N = int(input())
time = []
d= [0] * (N+1)
cost = []

for _ in range(N):
    t , c  = map(int,sys.stdin.readline().split())
    time.append(t)
    cost.append(c)




maxValue = 0
for i in range(N-1,-1,-1):
    times = time[i] + i
    if times <= N:
        d[i] = max(d[times] + cost[i],maxValue)
        maxValue = d[i]
    else:
        d[i] = maxValue


print(max(d))
    
    

