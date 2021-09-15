#ParthSingh
import array

arr = list(map(int, input().split()))
n=len(arr)
a1=int(input())
a2=int(input())

p=arr.index(a1)
w=arr.index(a2)

print(w-p)
