def Stack():
    stack = []
    return stack

def isEmpty( stack ):
    return len(stack) == 0

def push( stack, item ):
    stack.append( item )

def pop(stack ):

    if(isEmpty( stack )):
        print("Stack Underflow ")
        exit(1)
    return stack.pop()

def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end = ' ')
    print()
            
        
# stack 1
s=Stack()
arr = list(map(int, input().split()))
n=len(arr)
if (n%2)!=0:
    p=arr[n//2]
    arr.remove(p)
#print(arr)
    
for i in arr:
    push(s,i)
print("Below is the stack after deleting middle element")
prints(s)





