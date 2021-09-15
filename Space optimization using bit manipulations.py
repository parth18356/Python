#ParthSingh
import array

#arr = list(map(int, input().split()))
k=int(input())
n=int(input())
a=[]
b=[]

for i in range(k,n+1):
    a.append(i)
for j in range(0,len(a)):
    if ((a[j]%2==0) or (a[j]%5==0)):
        new=a[j]
        b.append(new)
print(*b)
