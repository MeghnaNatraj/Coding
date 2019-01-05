__author__ = 'Meghna'

class Node:
    def __init__(self,data = None, previous = None,  next = None):
        self.data = data
        self.previous = previous
        self.next = next


class DoubleLinkedList:
    def __init__(self,head=None):
        self.head = head

    def length(self):
        l = 0
        current = self.head
        while current != None:
            l += 1
            current = current.next
        return l


    def insert_node(self,data,position = 1):
        if position < 1 or  position > self.length()+1:
            print("This is an invalid position")
        else:
            new_node = Node(data)
            if position == 1:
                if self.head == None:
                    self.head = new_node
                else:
                    new_node.next = self.head
                    self.head.previous = new_node
                    self.head = new_node
            else :
                current_position = 1
                current = self.head
                while current_position != position-1 :
                    current_position = current_position+1
                    current = current.next

                new_node.next = current.next
                new_node.previous = current
                current.next = new_node
                if(new_node.next != None): new_node.next.previous = new_node


    def print_list(self):
        current = self.head
        if current == None:
            print("List has no elements")
        else  :
            print("Head")
            while (current != None):
                print(current.data)
                current = current.next

d = DoubleLinkedList()
d.insert_node(1)
d.insert_node(2)
d.insert_node(3)
d.insert_node(4)
d.insert_node(5)

d.insert_node(6,-5)
d.insert_node(7,0)
d.insert_node(8,10)
# d.print_list()
d.insert_node(9,1)
# d.print_list()
d.insert_node(10,4)
# d.print_list()
d.insert_node(11,8)
d.print_list()
print("Done")