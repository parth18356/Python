#ParthSingh
import array
from collections import deque
arr = list(map(int, input().split()))
n=len(arr)
new_arr=[]
new_n=n//2
final=arr[new_n]

if n%2==0:
    for i in range(0,new_n):    
        p=arr[i]
        new_arr.append(p)
        p1=n-1-i
        d=arr[p1]
        new_arr.append(d)
else:
    for i in range(0,new_n):    
        p=arr[i]
        new_arr.append(p)
        p1=n-1-i
        d=arr[p1]
        new_arr.append(d)
    new_arr.append(final)
print(new_arr)
