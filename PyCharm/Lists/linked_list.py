__author__ = 'Meghna'

class Node:
    def __init__(self,data = None , next = None):
        self.data = data
        self.next = next
    def getData(self):
        return  self.data
    def setData(self,data):
          self.data = data


class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert_end(self,node):
        if self.head == None :
            self.head = node
        elif self.head.next == None :
            self.head.next = node
        else:
            traverse = self.head
            while(traverse.next != None):
                traverse = traverse.next
            traverse.next = node

    def insert_start(self,node):
        node.next = self.head
        self.head = node

    def length(self):
        current = self.head
        length = 0
        while (current != None):
            length = length + 1
            current = current.next
        return length

    def print_list(self):
        current = self.head
        if current!= None:
            print("Head")
        else  :
            print("Array has no elements")
        while (current != None):
            print(current.data)
            current = current.next

    def insert_middle(self,node,position):
        length = self.length()
        if position < 1 or position > length + 1 :
            print("This is an invalid position")
        elif position == 1  :
            self.insert_start(node)
        elif position == length + 1 :
            self.insert_end(node)
        else:
            current_position = 1
            current = self.head
            while current_position != position - 1:
                current = current.next
                current_position = current_position  + 1
            node.next = current.next
            current.next = node


    def delete_node(self,node):
        if self.head == None :
            print("No elements to delete")
        else :
            if node == self.head :
                self.head = self.head.next
            else:
                current = self.head.next
                previous = self.head
                while current != None :
                    if current == node:
                        previous.next = current.next
                        print("Node "+str(node.data)+" has been successfully deleted")
                        return
                    previous = current
                    current = current.next
                print("The node was not found")



        # length = self.length()
        # if position < 1 or position > length:
        #     print("This is an invalid position")
        # elif length == 0:
        #     print("No elements to delete")
        # elif position == 1:
        #     self.head = self.head.next
        # else:
        #     while




n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

l = LinkedList()
# l.insert_end(n2)
# print(l.length())
# l.print_list()
# l.insert_end(n3)
# l.print_list()



l.insert_middle(n4,1)
l.print_list()

l.insert_middle(n5,1)
l.print_list()

l.insert_middle(n6,1)
l.print_list()

l.delete_node(n1)
l.print_list()



