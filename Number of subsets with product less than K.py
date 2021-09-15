#ParthSingh
import array
import math

arr = list(map(int, input().split()))
k=int(input())
n=len(arr)

def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x
    return (result)


subsets=[]
for i in range(0,n+1):
    for j in range(0,i):
        subsets.append(arr[j: i])
final=[]

print(subsets)
count=0
for i in range(0,len(subsets)):
    if (len(subsets[i])) <=1:
        print(subsets[i])
        for j in subsets[i]:
            if j <k:
                count=count+1
                final.append(subsets[i])
    else:
        for d in range(0,len(arr)):
            p=arr[d]
            print(p)
            print(multiplyList(p))
print(final)

            
            


