class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        """Initializing the head"""
        self.top = None

    def is_empty(self):
        return self.top is None

    def peek(self):
        """ Fetching the data on top of the node without removing it"""
        if self.is_empty():
            return "Stack is empty"
        return self.top.data #Return the data on the top of the stack

    def push(self,data):

        """Push the data onto the stack """
        new_node = Node(data) #create a new node with the given data
        new_node.next = self.top #Link the new node with the current top
        self.top = new_node #Update the top with the new node

    def pop(self):
        if self.is_empty():
            return "Stack is empty"

        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None #This is used to remove the unwanted reference to the popped element
        return popped_node.data

    def display(self):

        if self.is_empty():
            return "stack is empty"

        current = self.top
        element = []
        while current:
            element.append(current.data)
            current = current.next
        return element

stack = Stack()
stack.push(5)
stack.push(6)
print(stack.pop())
stack.push(7)
print(stack.peek())
print(stack.display())

