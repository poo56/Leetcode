class Node:
    def __init__(self, data=None, next=None):
        self.data= data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        newNode = Node(data) #create a new node with the given data

        #If the list is empty, make the new node the head

        if not self.head:
            self.head = newNode

        else:
            # tranverse to the end of the list
            current =  self.head
            while(current.next):
                current = current.next

            current.next = newNode


    def print(self):
        current =self.head
        while(current):
            print(current.data)
            current = current.next


ll = LinkedList()
ll.insert(5)
ll.insert(6)
ll.print()