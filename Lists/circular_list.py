class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
class CL:
    def __init__(self,data = None):
        if data == None:
            self.head = None
        else:
            self.head = Node(data)
            self.head.next = self.head

    def printCL(self):
        if self.head == None:
            print("No elements to print")
        else:
            current = self.head
            print("Head")
            print(current.data)
            while current.next!=self.head:
                current = current.next
                print(current.data)


    def insert_front(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next!=self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node


    def insert_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next!=self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete_front(self):
        if self.head == None:
            print("No elements to delete")
            return None
        elif self.head == self.head.next:
            value = self.head.data
            self.head = None
            return value
        else:
            value = self.head.data
            current = self.head
            while current.next!= self.head:
                current = current.next
            current.next = self.head.next
            self.head = current.next
            return value

    def delete_end(self):
        if self.head == None:
            print("No elements to delete")
            return None
        elif self.head == self.head.next:
            value = self.head.data
            self.head = None
            return value
        else:
            current = self.head
            while current.next.next!= self.head:
                current = current.next
            value = current.next.data
            current.next = self.head
            return value

circular_list = CL()
circular_list.insert_front(5)
circular_list.insert_front(6)
circular_list.insert_front(7)
circular_list.printCL()
circular_list.insert_end(4)
circular_list.insert_end(3)
circular_list.insert_end(2)
circular_list.printCL()
print("Deleting front")
print(circular_list.delete_front())
print(circular_list.delete_front())
print(circular_list.delete_front())
circular_list.printCL()
print("Deleting end")
print(circular_list.delete_end())
print(circular_list.delete_end())
print(circular_list.delete_end())
circular_list.printCL()












