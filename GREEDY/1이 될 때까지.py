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

N,K = map(int,sys.stdin.readline().split())
count = 0
while True:
    if N == 1:
        break
    if N % K == 0:
        N /= K
    else:
        N -=1
    count +=1
print(count)

