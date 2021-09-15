#ParthSingh
import array
from collections import deque
arr = list(map(int, input().split()))
n=len(arr)
new_arr= []
pos_arr=[]
for i in range(0,n):
    if (arr[i]<=0):
        p=arr[i]
        new_arr.append(p)
    else:
        m=arr[i]
        pos_arr.append(m)
#print(new_arr)
#print(pos_arr)
final_arr= new_arr+pos_arr
print(final_arr)
