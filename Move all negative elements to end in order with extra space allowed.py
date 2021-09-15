#ParthSingh
import array
from itertools import permutations
arr = list(map(int, input().split()))
n=len(arr)
neg_list=[]
pos_list=[]

for i in range(n):
    if (arr[i]>=0):
        pos_list.append(arr[i])
for i in range(n):
    if (arr[i]<=0):
        neg_list.append(arr[i])
print(pos_list+neg_list)
        
