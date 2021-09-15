#ParthSingh
import array
from collections import deque
arr = list(map(int, input().split()))
n=len(arr)
for i in range(n):
    for j in range(n):
        if (arr[j]==i):
            arr[j], arr[i] = arr[i], arr[j]
for i in range(n):
    if (arr[i] != i):
        arr[i] = -1
for i in range(n):
        print(arr[i], end = " ")
