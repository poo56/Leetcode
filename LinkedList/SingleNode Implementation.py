class Node:

    #constructor
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
#creating a single node
first_data = Node(5)
print(first_data.data)