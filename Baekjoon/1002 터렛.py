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
def distance(x1,y1,x2,y2):
    
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

T = int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())
    if distance(x1,y1,x2,y2) == 0: # 중심이 같은 경우
       if r1 == r2: # 반지름까지 같으면 원이 완전히 일치
          print(-1)
       else: # 반지름이 다르다면 원이 만날수 없다
          print(0)

    
    else: 
     if distance(x1,y1,x2,y2) == r1 + r2 or abs(r2-r1) == distance(x1,y1,x2,y2):
        print(1) # 내접하는 순간
     elif distance(x1,y1,x2,y2) < r1 + r2 and abs(r2-r1) < distance(x1,y1,x2,y2):
        print(2) # 
     else:
        print(0)
    
      
     
