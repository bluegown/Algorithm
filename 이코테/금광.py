import sys

# 11:17 풀이 시작

T = int(input())
graph = []
for _ in range(T):
    N,M = map(int,sys.stdin.readline().split())
    arr = list(map(int,sys.stdin.readline().split()))
    i = 0
    d = [[0 for _ in range(M)] for _ in range(N)]

    while True:
        graph.append(arr[i:i+M])
        i = i + M
        if i >= N *M:
            break # 여기가 그래프 divide 하는 부분

    index = 0
    for i in range(N):
        value = graph[i][0] # 시작점 각각 다르게 해서 시작
        d[i][0] = value # 초기값 세팅해주고 시작
        for j in range(1,M):
         if i == 0: # 
            d[i][j] = max(d[i][j-1],d[i+1][j-1]) + graph[i][j]
         elif i == N-1: # 위,오른쪽밖에 못 가는 상황
            d[i][j] = max(d[i-1][j-1],d[i][j-1]) + graph[i][j]
         else: # 위 , 옆, 아래 모두 갈 수 있는 상황
            d[i][j] = max(d[i][j-1],d[i+1][j-1],d[i-1][j-1]) + graph[i][j]
    print(d)
    print(max(d[N-1]))

            

                
           

        




        

    


    
