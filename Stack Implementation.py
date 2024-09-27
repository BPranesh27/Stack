class Stack:
    def __init__(self,n):
        self.size=n
        self.li=[]
    def push(self,value):
        if len(self.li)==self.size:
            print("OverFlow")
        else:
            return self.li.append(value)
    def Pop(self):
        if self.li==[]:
            print("Stack is empty")
        else:
            return self.li.pop()
    def peek(self):
        if(self.li==[]):
            print("Stack is Empty")
        else:
            return self.li[-1]
    
obj=Stack(int(input("Enter size : ")))
while True:
    operation=int(input("Operation : \n1 : Push\n2 : Pop\n3 : Peek\n"))
    match operation:
        case 1:
            obj.push(int(input("Enter value to Push : ")))
            print(obj.li)
        case 2:
            obj.Pop()
            print(obj.li)
        case 3:
            print(obj.peek())
        case 4:
            break