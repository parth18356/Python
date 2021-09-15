#ParthSingh
import array
from collections import deque
arr = list(map(int, input().split()))
index= int(input())
ranges = [ [ 0, 2 ], [ 0, 3 ] ]
rotations = 2
def findElement(arr, ranges, rotations, index) :
     
    for i in range(rotations - 1, -1, -1 ) :
        left = ranges[i][0]
        right = ranges[i][1]
        if (left <= index and right >= index) :
            if (index == left) :
                index = right
            else :
                index = index - 1
    return arr[index]

print(findElement(arr, ranges, rotations, index))


 
