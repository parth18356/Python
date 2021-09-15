#ParthSingh
import array

arr = list(map(int, input().split()))
n=len(arr)

arr.sort()

mf=arr[1]-arr[0]

for i in range(1,n):
    mf = min(mf, arr[i]-arr[i-1])
print(mf)
