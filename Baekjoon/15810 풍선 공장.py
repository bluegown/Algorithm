import sys
INF = 1000000 * 1000000
N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

start = 1
end = INF

res = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in range(len(arr)):
        count = count + (mid // arr[i])
    if count >= M: # 더 세어졌닫는 소리라서 mid가 감소해야함
        end = mid - 1
        res = mid
    else:
        start = mid + 1
    


    
print(res)

    
