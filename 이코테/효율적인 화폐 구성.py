import sys
N,M = map(int,sys.stdin.readline().split())

d = [10001] * (10001)

arr = []
for i in range(N):
    elem = int(input())
    arr.append(elem)
    d[elem] = 1


arr.sort()
for i in range(N):
    for j in range(arr[i],M+1):
        if d[j-i]!=10001:
            d[i] = min(d[i],d[i-j]+1)

if d[M]!= 10001:
 print(d[M])
else:
   print(-1)

