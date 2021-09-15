#ParthSingh
import array
from collections import deque
arr = list(map(int, input().split()))
n= int(input())
c=len(arr)-n
if n>len(arr):
    print("The integer entered is bigger than the list")
else:
    arr = arr[c:]+arr[:c]
    print(arr)

