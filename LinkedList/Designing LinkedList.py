class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class MyLinkedList():
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self,index:int):
        cur = self.left.next
        while cur and index >0:
            cur = cur.next
            index -=1

        if cur and cur!=self.right and index ==0:
            return cur.val

        return - 1


    def AddAthead(self,val:int):
        node = Node(val)
        next = self.left.next
        prev = self.left
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def AddAtTail(self,val:int):
        node = Node(val)
        next = self.right
        prev = self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev= prev

       def AddAtIndex(self,index:int):
        cur = self.left.next
        while cur and index >0:
            cur = cur.next
            index -=1
            
        if cur and index ==0:
            node = Node(val)
            next = cur
            prev = cur.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev
            
    def deleteAtIndex(self,index:int):
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -=1
            
        if cur and cur!= self.right and index==0:
            next = cur.next
            prev = cur.prev
            next.prev = prev
            prev.next = next



