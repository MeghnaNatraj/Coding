__author__ = 'Meghna'

class BTN:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def pre_order(root):
    if not root:
        return
    result = []
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right.data in result:
                stack.append(node)
                node = node.right
            else:
                result.append(node.data)
                node = None
    return result


root = BTN(1)
n2 = BTN(2)
n3 = BTN(3)
n4 = BTN(4)
n5 = BTN(5)
n6 = BTN(6)
n7 = BTN(7)
print("Here")

root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

print(pre_order(root))

