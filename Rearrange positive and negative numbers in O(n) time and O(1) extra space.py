#ParthSingh
import array
from collections import deque
arr = list(map(int, input().split()))
n=len(arr)

def rearrange(arr, n):
    i = -1
    for j in range(n):
        if (arr[j] < 0):
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    count=0
    positive=i+1
    negative=0
    while (positive < n and negative < positive and arr[negative] < 0):
        arr[negative], arr[positive] = arr[positive], arr[negative]
        positive = positive+ 1
        negative = negative+  2

rearrange(arr, n)
print(arr)
