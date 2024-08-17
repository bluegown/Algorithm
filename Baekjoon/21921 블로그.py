import sys

N,X = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

result = 0
count = 0
sumValue = sum(arr[0:X]) # 초기에는 이렇게 해주고
for i in range(1,N-X+1): 
     if sumValue > result: 
        result = sumValue 
     sumValue = sumValue + arr[i+X-1] - arr[i-1]
     
sumValue = max(sumValue, sum(arr[N-X:N]))


    


sumValue = sum(arr[0:X])
for i in range(1,N-X+1):
    if sumValue == result: 
        count += 1
    sumValue = sumValue + arr[i+X-1] - arr[i-1]

if result == sum(arr[N-X:N]):
   count += 1

if max(arr)!= 0: 
 print(result)
 print(count)
else:
   print("SAD")