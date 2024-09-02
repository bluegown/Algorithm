import sys

def binary_search(arr):
    start = min(arr)
    end = sum(arr)

    mid = (start+end) // 2
    while start <= end:
        mid = (start + end) // 2
        count = 0
        sumValue = 0
        for i in arr:
            if sumValue < i: # 만약 기준 원소보다 크면 count 해주고 
                sumValue = mid # mid만큼 일단 충전시켜주고, 
                count +=1 
            sumValue -= i # i만큼 사용하므로 
        if count > M or mid < max(arr): # 이렇게하면 불필요하게 M번 이상 충전하므로 
            start = mid +1 
        else:
            end = mid - 1
            answer = mid
        

    return answer



N,M = map(int,sys.stdin.readline().split())
arr = []
for _ in range(N):
    x = int(input())
    arr.append(x)



print(binary_search(arr))

    

    
