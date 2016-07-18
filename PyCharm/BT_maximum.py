__author__ = 'Meghna'


class BTN:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

max_value = float("-infinity")
def max(root):
    global max_value
    if not root:
        return
    elif root.data>max_value:
        max_value = root.data
    max(root.left)
    max(root.right)

root = BTN(1)
n2 = BTN(2)
n3 = BTN(3)
n4 = BTN(4)
n5 = BTN(5)
n6 = BTN(6)
n7 = BTN(7)

root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

max(root)
print(max_value)
