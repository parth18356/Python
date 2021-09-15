#ParthSingh
import array

n=int(input())
new=[]
matrix = [list(map(int,input().split())) for i in range(n)]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        new.append(matrix[j])
print(min(min(new)))

