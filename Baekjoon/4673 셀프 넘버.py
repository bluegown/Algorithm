import sys
# sys.stdin.readline()
import heapq
import copy
import itertools
from itertools import combinations
from itertools import permutations
from collections import deque
import math
sys.setrecursionlimit(100000000)
INF = 1e9
    
N,M = map(int,sys.stdin.readline().split())
arr = dict()
for _ in range(N):
    a = sys.stdin.readline().rstrip()
    if len(a) >= M:
     if a in arr:
        arr[a] +=1
     else:
        arr[a] = 1 # 없다면 만들어준다

arr = sorted(arr.items(),key = lambda x:(-x[1],-len(x[0]),x[0]))


for i in arr:
    print(i[0])













    



