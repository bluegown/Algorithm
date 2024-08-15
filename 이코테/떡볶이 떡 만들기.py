import sys

def binary_search(arr,M):
    start = 0
    end = max(arr)

    value = 0
    while start <= end:
        mid = (start + end) // 2 # 떡 길이 탐색 
        sum = 0
        for i in arr:
         if i > mid: # 원소가 더 큰경우만 떡을 잘라야지,,,,
          sum += (i - mid)
        print(sum)
        if sum > M:
           start = mid + 1 # 떡 더자르자!
           value = mid
        elif sum < M:
           end = mid - 1 # 떡을 들 잘라야할듯?
        else:
           value = mid # sum == M인 베스트 경우.
           return value
           
    return value
    
N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

print(binary_search(arr,M))
