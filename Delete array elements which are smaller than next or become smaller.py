a=int(input())
arr = list(map(int, input().split()))
n=len(arr)

for i in range(0,n-2):
    count=0
    if count == a:
        break
    else:
        if arr[i]<arr[i+1]:
            p=arr[i]
            arr.remove(p)
            print(arr)
            count=count+1
print(arr)







