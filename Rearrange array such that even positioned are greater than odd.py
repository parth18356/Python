#ParthSingh
import array
from collections import deque
arr = list(map(int, input().split()))
n=len(arr)
for i in range(1,n):
    if (i % 2 == 0):
        if (arr[i]>arr[i-1]):
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
    else:
        if (arr[i]<arr[i-1]):
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
print(arr)
        
