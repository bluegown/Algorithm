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



location = input()
row = ord(location[0]) - ord('a')
col = int(location[1]) - 1

dx = [-1,1,1,-1,-2,-2,2,2]
dy = [2,2,-2,-2,1,-1,1,-1]
count = 0
for i in range(8):
        nx = row + dx[i]
        ny = col + dy[i]
        if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
            continue
        count +=1
print(count)