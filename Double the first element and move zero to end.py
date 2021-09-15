#ParthSingh
import array
from collections import deque
arr = list(map(int, input().split()))
n=len(arr)
count=0
new_arr=[]
c= arr.count(0)

for i in range(0,n-1):
    if ((arr[i] != 0) and (arr[i] == arr[i+1])):
        arr[i] = 2 * arr[i]
        arr[i+1] = 0
        count=count+1
        i=i+1

for i in range(len(arr)):
    if arr[i]>0:
        p=arr[i]
        new_arr.append(p)
        
final_count=c+count

for i in range(final_count):
    new_arr.append(0)
print(new_arr)


