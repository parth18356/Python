arr = list(map(int, input().split()))
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

def my_list(stack,arr):
    a=[]
    for i in range(len(stack)-1, -1, -1):
        a.append(stack[i])
    arr.sort()
    if a == arr:
        print("True")
    else:
        print("False")     
        
# stack 1
s=Stack()

for i in arr:
    push(s,i)

my_list(s,arr)

prints(s)



