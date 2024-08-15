import sys

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))

d = [0] * (N)

d[0] = arr[0]
d[1] = arr[1]
for i in range(2,N):
    d[i] = max(arr[i-1],d[i-2] + arr[i])

print(d)
