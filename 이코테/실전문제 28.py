import sys

def binary_search(arr):
    start = 0
    end = len(arr)-1 # 인덱스로 할 거니까?
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
print(binary_search(arr))
