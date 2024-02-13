import sys
def convert(x):
    if x == 1:
        x = 0
    else:
        x = 1
    return x
N = int(input())
switch = list(map(int,sys.stdin.readline().split()))

student = int(input())
info = [] 
for _ in range(student):
    gender,num = map(int,sys.stdin.readline().split())
    info.append((gender,num))


for i in range(len(info)):
    index = 1
    if info[i][0] == 1: # 남자인 경우
        for j in range(len(switch)):
            if (j+1) % info[i][1] == 0:
                switch[j] = convert(switch[j]) # 문제없음
    else:
        center = info[i][1] - 1
        count = 0
        switch[center] = convert(switch[center]) # 3번 카드 바꿔
        for k in range(1,len(switch)):
              leftindex = center - k
              rightindex = center + k
              if leftindex >= 0 and rightindex < len(switch):
               if switch[leftindex] == switch[rightindex]:
                  switch[leftindex] = convert(switch[leftindex]) 
                  switch[rightindex] = convert(switch[rightindex]) 
               else:
                  break  
              
        
index = 0
for i in switch:
    print(i,end = ' ')
    index +=1
    if index >= 20:
        index = 0
        print()



        
        


