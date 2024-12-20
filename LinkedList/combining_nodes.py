class Node:

    #constructor
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

# a linked list with a single head node
class LinkedList:
    def _init__(self):
        self.head=None
LL = LinkedList()
LL.head = Node(5)
print(LL.head.data)
