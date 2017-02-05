__author__ = 'Meghna'

from collections import deque
q = deque()

class BTN:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def breadth_first_search(root):
    if not root:
        return
    result = []
    q.append(root)
    while q:
        front = q.popleft()
        result.append(front.data)
        if front.left:
            q.append(front.left)
        if front.right:
            q.append(front.right)
    return result

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

print(breadth_first_search(root))
print("Done")