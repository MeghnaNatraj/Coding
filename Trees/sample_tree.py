class BT_Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

node1 = BT_Node(1)
node2 = BT_Node(2)
node3 = BT_Node(3)
node4 = BT_Node(4)
node5 = BT_Node(5)
node6 = BT_Node(6)
node7 = BT_Node(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7