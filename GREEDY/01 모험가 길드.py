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
N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
index = 0
sum = 0
minValue = arr[0]
team = 0
count = 0
index2 = 0
while True:
    if index >=len(arr) or index2 == len(arr):
        break
    if arr[index] == 1:
        index +=1
        count = 0
        team +=1
    elif count == arr[index]:
        index += count
        count = 0
        team +=1
    elif count < arr[index]:
        count +=1
    index2 +=1
    
print(team)



    
