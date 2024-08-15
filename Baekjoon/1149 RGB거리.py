import sys

N,M = map(int,sys.stdin.readline().split())

lis = set()
wat = set()

for i in range(N):
    name = input()
    lis.add(name)
ans = []

for i in range(N):
    name = input()
    wat.add(name)

for i in lis:
    if i in wat: # O(1)으로 해서 괜찮음
        ans.append(i)

print(len(ans))
ans.sort()
for i in ans:
    print(i)
            








