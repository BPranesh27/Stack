class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, n):
        self.size = n
        self.peek = None
        self.current_size = 0

    def push(self, value):
        if self.current_size == self.size:
            print("Overflow")
        else:
            new_node = Node(value)
            new_node.next = self.peek
            self.peek = new_node
            self.current_size += 1

    def Pop(self):
        if self.peek is None:
            print("Stack is empty")
        else:
            popped_value = self.peek.value
            self.peek = self.peek.next
            self.current_size -= 1
            return popped_value

    def peek_value(self):
        if self.peek is None:
            print("Stack is Empty")
        else:
            return self.peek.value

    def display(self):
        if self.peek is None:
            print("Stack is empty")
        else:
            temp = self.peek
            elements = []
            while temp:
                elements.append(temp.value)
                temp = temp.next
            print(elements)

# Usage
obj = Stack(int(input("Enter size: ")))
while True:
    operation = int(input("Operation: \n1: Push\n2: Pop\n3: Peek\n4: Exit\n"))
    
    match operation:
        case 1:
            obj.push(int(input("Enter value to Push: ")))
            obj.display()
        
        case 2:
            obj.Pop()
            obj.display()

        case 3:
            print(obj.peek_value())  
        
        case 4:
            break

        case _:
            print("Invalid operation. Please try again.")
