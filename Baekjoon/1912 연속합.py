import sys

N = int(input())

arr = list(map(int,sys.stdin.readline().split()))

d = [-1001] * (N+1)

sum = 0 
d[0] = arr[0]
sum = d[0]
for i in range(1,len(arr)):
  d[i] = arr[i]
  d[i] = max(d[i],d[i-1]+ arr[i])
  sum += d[i]


print(max(d))