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

N,M = map(int,sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
maxi = -1
for i in range(N):
    maxValue = min(graph[i])
    if maxValue > maxi:
        minValue = maxi
print(maxValue)