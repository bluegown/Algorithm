import sys
import queue
N,K = map(int,sys.stdin.readline().split())

count = 0
d = [0] * 20
queue = deque()
d[N] = 0


   
print(d[K])