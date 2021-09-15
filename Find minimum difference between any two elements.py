#ParthSingh
import array
from collections import Counter

arr = list(map(int, input().split()))
n=len(arr)
diff_list=[]

arr.sort()

for i in range(n-1):
    d= arr[i+1]-arr[i]
    diff_list.append(d)

print(min(diff_list))
