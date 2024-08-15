import sys
def dfs():
    
    
    if len(s) == M: # 만약 요구하는 길이가 다 된다면 
        print(' '.join(map(str,s)))
        return 
    for i in num:
        if len(s)!=0:
            if s[-1] > i:
                continue
        s.append(i) # 스택에 쌓아주고
        dfs()
        s.pop() #만약 끝나고 돌아왔다면, 이제 더이상 가지치기를 할 필요가 없으므로 pop

N,M = map(int,sys.stdin.readline().split())


s = []
num = list(map(int,sys.stdin.readline().split()))
num.sort()

dfs()


