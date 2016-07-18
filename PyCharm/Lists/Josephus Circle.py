__author__ = 'Meghna'

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

    def delete_node(self,position):
        if self.head == self.head.next:
            return None
        else:
            count = 0
            current = self.head
            while count < position - 2 :
                current = current.next
                count  += 1
            value = current.next.data
            current.next = current.next.next
            self.head = current.next
            return value

def josephus_circle(n,m):
    death_order = []
    circular_list = CL()
    for item in range(n):
        circular_list.insert_end(item)
    deleted_value = circular_list.delete_node(m)
    while deleted_value!=None:
        death_order.append(deleted_value)
        deleted_value = circular_list.delete_node(m)
    circular_list.printCL()
    print(death_order)


josephus_circle(2,3)





#
# def josephus_circle(n,m):
#     die_order = []
#     start = -1
#     while start < n:
#         start = start + 3
#         if start >= n :
#             start = start - n
#         die_order.append(start)
#         if start == n-1:
#             break
#     return die_order






