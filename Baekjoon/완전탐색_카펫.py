def solution(brown, yellow):
    answer = []
    
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            x,y = yellow // i, i
            if (x+2) * (y+2) == (brown + yellow):
                return [x+2,y+2]
            
    return answer