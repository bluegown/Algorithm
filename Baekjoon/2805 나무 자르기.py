import sys
def binary_search(arr):
    start = 0
    end = arr[-1]
    value = 0
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for i in arr:
            if i >= mid and mid!=0: # 
             sum += (i - mid) # 나누고 이후의 나머지만 가져간다
        if sum < M : # 목표치보다 들 잘려있으면, 나무를 더 잘라야지 -> 
           end = mid - 1
        elif sum >= M:
           value = mid
           start = mid + 1
    return value
           



N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort() # 이분탐색에서의 디폴트 조건이므로 무조건 할것 ! O(logN)으로 실행됨

print(binary_search(arr))