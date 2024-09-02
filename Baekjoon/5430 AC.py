import sys
from collections import deque
def AC(queue,func):
    global count
    count = 0
    for i in func:
        if i == 'R':
         count += 1
        elif i == 'D':
            if len(queue) == 0:
                return False
            else:
                if count % 2 == 0:
                 queue.popleft() # popleft면 왼쪽 원소 제거
                else:
                 queue.pop()
    return queue
T = int(input())

count = 0
for _ in range(T):
    func = list(input())
    N = int(input()) # 배열 길이 리스트
   

    queue = deque(input()[1:-1].split(','))

    if N == 0:
       queue = []




    arr = AC(queue,func)
    if arr == False:
        print('error')
    else:
     if count % 2 == 0:
      print("["+",".join(arr)+"]")
     else:
        arr.reverse()
        print("["+",".join(arr)+"]")
       
