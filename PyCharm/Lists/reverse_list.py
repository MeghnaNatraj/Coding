class Node:
    def __init__(self,data):
        self.data = data
        self.nxt = None
class LL:
    def __init__(self,head):
        self.head = head
    
    def print_LL(self):
        current = self.head
        if current:
            print "Head"
        while current:
            print current.data
            current = current.nxt
    
    def reverse_LL(self):
        previous = None
        current = self.head
        while current:
            nxt = current.nxt
            current.nxt = previous
            previous = current
            current = nxt
        self.head = previous

a = Node(1)
a.nxt = Node(2)
a.nxt.nxt = Node(3)
l = LL(a)


l.print_LL()
l.reverse_LL()
l.print_LL()       