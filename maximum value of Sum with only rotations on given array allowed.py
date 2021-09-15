#ParthSingh
import array
arr = list(map(int, input().split()))
n=len(arr)
arr.sort()
sum=0
for i in range(0, n):
    p=i*(arr[i])
    print(p)
    sum=sum+p
print(sum)
