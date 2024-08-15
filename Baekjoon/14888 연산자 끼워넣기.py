import sys

def dfs(i,Value):
    global maxValue,minValue,cal
    if i == N: # i가 N이 될 떄 까지 재귀 조진다
        maxValue = max(maxValue,Value)
        minValue = min(minValue,Value)
    else:
     if cal[0] > 0: # add가 존재하는 경우
        cal[0] -=1 # 한개 감소시키고 
        dfs(i+1,Value + num[i]) # 그 다음 굴리고
        cal[0] +=1 # 만약 돌아온다면 조건
     if cal[1] > 0: # add가 존재하는 경우
        cal[1] -=1 # 한개 감소시키고 
        dfs(i+1,Value - num[i]) # 그 다음 굴리고
        cal[1] +=1 # 만약 돌아온다면 조건
     if cal[2] > 0: # add가 존재하는 경우
        cal[2] -=1 # 한개 감소시키고 
        dfs(i+1,Value * num[i]) # 그 다음 굴리고
        cal[2] +=1 # 만약 돌아온다면 조건
     if cal[3] > 0: # add가 존재하는 경우
        cal[3] -=1 # 한개 감소시키고 
        dfs(i+1,int(Value / num[i])) # 그 다음 굴리고
        cal[3] +=1 # 만약 돌아온다면 조건
N = int(input())
num = list(map(int,sys.stdin.readline().split()))
cal = list(map(int,sys.stdin.readline().split()))
maxValue = int(-1e9)
minValue = int(1e9)

dfs(1,num[0])

print(maxValue)
print(minValue)