import sys
def binary_search(arr):
    start = 1
    end = arr[-1] # 가장 큰 elem으로 나눈다
    value = 0 
    while start <= end:
        sum = 0 # 총 길이
        mid = (start + end) // 2

        for i in arr:
             sum += ( i // mid)
            
        if sum < N: # 만약 잘랐는데 선의 개수가 들나왔으면 ? 더 많이 잘라야지 -> 길이 줄여!
            end = mid - 1
        elif sum >= N : # 잘랐는데 선의 개수가 N보다 큰것도 경우에 포함이므로 , 일단 value는 기록
            value = mid
            start = mid + 1 
    return value
K,N = map(int,sys.stdin.readline().split())
arr = []
for i in range(K):
    elem = int(input())
    arr.append(elem)
arr.sort()
print(binary_search(arr))

