import sys
def first(arr,x,start,end): # 처음 등장한 위치를 찾기 위한 함수
   if start > end:
      return None
   mid = (start + end ) // 2
   if ((mid == 0 or arr[mid-1] < x) and arr[mid] == x): # mid가 0이면 start,end가 모두 0
      # arr[mid-1]은 x보다 작고 , arr[mid]가 x와 일치하다면 ? -> 그게 처음으로 등장한 인덱스가 될 것
      return mid
   elif arr[mid] >= x:
      return first(arr,x,start,mid-1)
   else:
      return first(arr,x,mid+1,end)
#mid로 0을 반환한다면 존재하지 않는다는 의미이고, 0이 아니라면 첫 인덱스를 반환해줄 것

def last(arr,x,start,end):
   if start > end:
      return None
   mid = (start + end) // 2
   if ((mid == N-1 or arr[mid+1] > x) and arr[mid] == x): # mid가 0이면 start,end가 모두 0
      # arr[mid-1]은 x보다 작고 , arr[mid]가 x와 일치하다면 ? -> 그게 처음으로 등장한 인덱스가 될 것
      return mid
   elif arr[mid] > x:
      return last(arr,x,start,mid-1)
   else:
      return last(arr,x,mid+1,end)
      
       
   
   

    



N,x = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
count = 0
a = first(arr,x,0,N-1)
b = last(arr,x,0,N-1) # 인덱스라서 N-1로 해줘야함

if a == None or b == None:
   print(-1)
else:
   print(b-a+1)
