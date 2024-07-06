
import sys

N = int(input())
li = list(map(int,sys.stdin.readline().split()))


x = [0] * (N)

for i in range(N):
    count = 0
    for j in range(N):
        if count == li[i]:
             index = j
             break
        if x[j] == 0:
            count +=1
    if x[index] == 0:
     x[index] = i+1
    else:
     for a in range(index+1,N):
        if x[a] == 0:
           x[a] = i+1
           break
        
for i in x:
   print(i,end=" ")
    
