import sys

def num1(arr):
   value = round(((sum / len(arr))))
   print(value)

def num2(arr):
   print(arr[len(arr) // 2])

def num3(dic):
   x = []
   mx = max(dic.values()) # dic의 values의 max값을 추출
   for i in dic: # 이렇게 쓰면 딕셔너리의 각 키를 순회한다
    if mx==dic[i]: # 여기서 dic[i]는 i라는 키에 대응하는 value값
        x.append(i) # 순서가 key,value이므로 ,, dic[key] = value!! 

   if len(x) > 1:
      print(x[1])
   else:
      print(x[0])
   
def num4(arr):
   value = max(arr) - min(arr)
   print(value)



N = int(input())
arr = []
sum = 0
for i in range(N):
   arr.append(int(sys.stdin.readline()))
arr.sort()
dic = dict()
for elem in arr:
    if elem in dic:
     dic[elem] +=1
    else:
       dic[elem] = 1
    sum += elem


num1(arr)
num2(arr)
num3(dic)
num4(arr)