import sys
# sys.stdin.readline()
import heapq
import copy
import itertools
from itertools import combinations
from itertools import permutations
from collections import deque
sys.setrecursionlimit(100000000)
INF = 1e9

def secondsolution():
   count = int(M/(K+1)) * K
   count += (M%(K+1))

   result = 0
   result += arr[0] *(count)
   result += arr[1] * (M-count)
   
N,M,K = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort(reverse = True)
index = 0
sum = 0
for _ in range(M):  
    index +=1 
    if index < K:
     sum += arr[0]
    else:
       index = 0
       sum +=arr[1]
print(sum)