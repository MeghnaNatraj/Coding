class Node:

	def __init__(self,data = None,next = None):
		self.data = data
		self.next = next

class Linked_List:

	def __init__(self,head = None):
		if head:
			self.head = Node(head)
		else:
			self.head = None

	def insert_end(self,data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node		
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_node

	def print_list(self):
		if not self.head :
			print("The list is empty")
			return
		else:
			print("Head")
			current = self.head
			while current :
				print(current.data)
				current = current.next

	def even_odd(self):
		if not self.head:
			return
		else:
			odd_list = Linked_List()
			previous = None
			current = self.head
			while current:
				if current.data % 2 != 0:
					odd_list.insert_end(current.data)
					if current == self.head :
						self.head = self.head.next
						previous = current
					else:
						previous.next = current.next

				else:
					previous = current
				current = previous.next
			previous.next = odd_list.head
		
list = Linked_List()
for item in []:
	list.insert_end(item)
# list.print_list()
list.even_odd()
list.print_list()
print("End")




