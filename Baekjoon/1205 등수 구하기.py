import sys
def nisbigthanone():
    ranklist = []
    rank.sort()
    for i in range(len(rank)):
     index = 1
     for j in range(i+1,len(rank)):
        if rank[i] < rank[j]:
            index +=1
     ranklist.append((rank[i],index))


    index = 1
    samecount = 0
    for i in ranklist:
     if i[0] > score:
        index +=1
     if i[0] == score:
        samecount +=1 
    
    if index + samecount <= P:
     ranklist.insert(N-1-index,(score,index))
     ranklist.sort()
    
    for i in range(len(ranklist)-1,0,-1):
       if ranklist[i][0] == score:
        index = ranklist[i][1]
    if index + samecount > P:
        print(-1)
    else:
        print(index)



N, score, P = map(int,sys.stdin.readline().split())
if N>=1:   
 rank = list(map(int,sys.stdin.readline().split()))
else:
   print(1)

if N >=1:
   nisbigthanone()






    

    
