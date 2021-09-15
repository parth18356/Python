#ParthSingh
import array
from collections import Counter
from itertools import combinations_with_replacement

arr = list(map(int, input().split()))
n=len(arr)
r=1

for i in range (0, n):
        if arr[i] <= r:
            r = r + arr[i]
        else:
            break
print(r)
