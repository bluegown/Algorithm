import sys

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
M = int(input())
arr.sort()
sum2 = 0
for i in arr:
    sum2 += i

if sum2 < M:
    print(max(arr))
else:
 Value = N
 arr2 = []
 while True:
    sum = 0
    for i in arr:
        if i <= Value:
            sum += i # 범위 이내인 경우는 그 값을 더해준다
        else:
            sum += Value # 초과인 경우는 상한액을 더해주고 
    if sum > M:
        break
    arr2.append((sum,Value))
    Value += 1
 print(arr2[-1][1])



