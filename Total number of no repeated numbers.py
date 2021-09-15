#ParthSingh
import array
from collections import Counter

arr = list(map(int, input().split()))
n=len(arr)
l=[]
repeated_l=[]

for i in range(0,n):
    b=arr[i]
    a=len(str(arr[i]))
    if a<=1:
        l.append(arr[i])
    else:
        c = Counter(str(b))
        if any(value > 1 for value in c.values()):
            repeated_l.append(arr[i])
        else:
            l.append(arr[i])

print(*l)
