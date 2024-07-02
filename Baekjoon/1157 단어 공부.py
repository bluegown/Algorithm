import sys
N,K = map(int,sys.stdin.readline().split())
a = list((map(int,sys.stdin.readline().split()))) # 길이가 N인 배열
a.sort()
arr = []
b = set(a)
for i in b:
    if a.count(i) >= K+1:
        arr.append(i)



count = 0
for i in arr:
    count += a.count(i) - 2
print(count)