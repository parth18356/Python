#ParthSingh
import array

arr = list(map(int, input().split()))
k=int(input())
n=len(arr)
index=0
total=0

if (n < k):
    print("0")

for i in range(k):
        total=total+arr[i]
t=total

for i in range(k, n):
    total=total+ (arr[i] - arr[i-k])

    if (total < t):
         
            t = total
            index = (i - k + 1)
print("Subarray index =", index, " to ", (index + k - 1), "contains min avg")
