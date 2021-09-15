#ParthSingh
import array
from collections import deque
arr = list(map(int, input().split()))
n= int(input())
if n>len(arr):
    print("The integer entered is bigger than the list")
else:
    arr = arr[n:]+arr[:n]
    print(arr)

