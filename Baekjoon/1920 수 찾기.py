import sys

N = int(input())
arr = set(map(int,sys.stdin.readline().split()))

M = int(input())
lis = list(map(int,sys.stdin.readline().split()))

for i in lis:
    if i in arr:
        print(1)
    else:
        print(0)