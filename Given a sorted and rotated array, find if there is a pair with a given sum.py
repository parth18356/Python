#ParthSingh
import array
from collections import deque
arr = list(map(int, input().split()))
sum= int(input())
n=len(arr)
for i in range(0, n):
    for j in range(i + 1, n ):
        if (arr[i] + arr[j] == sum):
            print("(", arr[i],", ", arr[j],")", sep = "")
