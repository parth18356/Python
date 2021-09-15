#ParthSingh
import array
import statistics 

arr = list(map(int, input().split()))
n=len(arr)
for i in range(0,n-1):
    p=(arr[i]+arr[i+1])/2
    arr[i+1]=p
print(arr)
    
