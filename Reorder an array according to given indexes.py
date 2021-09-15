#ParthSingh
import array
from collections import deque
arr = list(map(int, input().split()))
index = list(map(int, input().split()))
n=len(arr)

for i in range(n):
	x,y=arr[i],index[i]
	arr[i]=arr[index[i]]
	arr[index[i]]=x
	index[i]=index[y]
	index[y]=y
print(arr)

