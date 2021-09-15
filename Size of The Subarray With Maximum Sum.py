#ParthSingh
import array
import statistics 

arr = list(map(int, input().split()))
n=len(arr)
maxi = 0
end=0
for i in range(n):
    end = end + i
    end = max(end, 0)
    maxi = max(maxi, end)
print(maxi)
