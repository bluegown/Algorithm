# 5:33 #

import sys

X = int(input())
count = 0
while True:
 print(X)
 if X == 1:
   break
 if X%3 == 0:
    count +=1
    X = X // 3
 elif X%2 == 0:
    count +=1
    X = X // 2
 else:
   count +=1
   X = X - 1
 
print(count)