import sys
N = int(input())
arr = []
for i in range(N):
    x = list(map(int,sys.stdin.readline().split()))
    arr.append(x)

d = [[0 for _ in range(N+1)] for _ in range(N+1)]

d[0][0] = arr[0][0]
for i in range(N):
    for j in range(i+1):
        if j == 0:
            d[i][0] = d[i-1][0] + arr[i][0]
        elif j == i:
            d[i][j] = d[i-1][j-1] + arr[i][j]
        else: # min값으로 대결
            d[i][j] = max(d[i-1][j-1],d[i-1][j]) + arr[i][j]

print(max(d[N-1]))

# 7-> [0][0]
# 3 8 -> [1][0] [1][1]
# 8 1 0 -> [2][0] [2][1] [2][2]
# 2 7 4 4 -> [3][0] [3][1] [3][2] [3][3]
# 4 5 2 6 5 -> [4][0] [4][1] [4][2] [4][3] [4][4]