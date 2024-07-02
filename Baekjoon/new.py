import sys
N,K = map(int,sys.stdin.readline().split())
arr = []
string = ''
for i in range(N):
    value = input()
    arr.append(value)
print(arr)
for i in range(N):
    string = string+ str(arr[i])
number = K % len(string)

print(arr[number-1])