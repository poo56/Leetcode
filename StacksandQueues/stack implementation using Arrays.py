class Stack:

    def __init__(self):
        self.stack = []


    def is_empty(self):
        return len(self.stack) == 0

    def push(self,data):
        self.stack.append(data)
        print("Pushed Item:" + data)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"

        return self.stack.pop()

    def peek(self):
        """Peek at the top item of the stack without removing it"""
        if self.is_empty():
            return " stack is empty"
        return self.stack[-1] #Returns the top of the element without removing it


    def display(self):

        """Display teh elements in the stack"""

        if self.is_empty():
            return "Stack is empty"

        return self.stack

stack = Stack()

stack.push(str(1))
stack.push(str(2))
stack.push(str(3))
stack.push(str(4))
print("popped item: " + stack.pop())
print("stack after popping an element: " , stack.display())
