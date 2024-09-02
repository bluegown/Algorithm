import sys

T = int(input())



for _ in range(T):
    arr = list(sys.stdin.readline().rstrip())
    number = len(arr)
    index = -1
    count = 0
    for i in range(number):
        if arr[i] == '(':
            count += 1
        if arr[i] == ')':
            count -=1
        if count < 0:
            break

    if count == 0:
        print("YES")
    else:
        print("NO")

            
                
               
    