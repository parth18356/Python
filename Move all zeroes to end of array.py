#ParthSingh
import array
from collections import deque
arr = list(map(int, input().split()))
n=len(arr)
new_arr= []
for i in range(0,n):
    if (arr[i]!=0):
        p=arr[i]
        new_arr.append(p)
m=len(new_arr)
final_length= n-m
for i in range(final_length):
    new_arr.append(0)
print(new_arr)
        
