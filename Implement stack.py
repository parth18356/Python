class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self , item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]
    def printt(self):
        a=[]
        for i in range(len(self.items)):
            p=self.items.pop()
            a.append(p)
        return a
            
        

s=Stack()
s.push(2)
s.push(22)
size=s.size()
print(s.printt())
