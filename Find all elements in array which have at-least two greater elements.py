#ParthSingh
import array
import time

start = time.time()


arr = list(map(int, input().split()))
p=max(arr)
index = arr.index(p)
arr.pop(index)
new_p=max(arr)
index2 = arr.index(new_p)
arr.pop(index2)
print(arr)

# time.sleep(1)
end = time.time()
print("Runtime is: " + str(end - start))
