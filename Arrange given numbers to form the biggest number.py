#ParthSingh
import array
from itertools import permutations
arr = list(map(int, input().split()))
n=len(arr)
res = int(max((''.join(i) for i in permutations(str(i) 
                     for i in arr)), key = int))
print(res)
