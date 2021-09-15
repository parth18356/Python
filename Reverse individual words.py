string=str(input())
words=string.split(' ')
print(words)
arr=[]
for i in words:
    p=i[::-1]
    arr.append(p)
print(*arr)


