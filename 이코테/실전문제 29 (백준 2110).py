import sys
def binary_search(arr):
    start = 1
    res = 0
    end = arr[-1] - arr[0]
    while start <= end:
        mid = (start + end) // 2
        value = arr[0]
    
        count = 1 
        for i in range(1,N):
            if arr[i] - value >= mid: # 둘 사이의 거리가 mid보다 크다면? 설치 가능
                value = arr[i] # 실시간으로 value를 바꿔준다
                count +=1 # 설치
        if count >= C:# 만약 c보다 더 설치할 수 있거나 같은 경우라면 , start를 증가시켜서 mid를 더 증가시킨다
            start = mid + 1 
            res = mid # 바운드리에 들어올 때 res를 기록한다.
        else: # 아니라면 mid를 감소시켜야 함
            end = mid - 1
    return res
    

N,C = map(int,sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort() 
print(binary_search(arr))