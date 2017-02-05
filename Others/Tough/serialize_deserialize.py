__author__ = 'Meghna'
# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        a_list = deque()
        final_list = []
        if not root:
            return final_list
        a_list.append(root)
        while len(a_list) != 0 :
            node = a_list.popleft()
            if node != None:
                a_list.append(node.left)
                a_list.append(node.right)
                final_list.append(node.val)
            else:
                final_list.append(None)
        return final_list


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        length_data = len(data)
        if length_data == 0:
            return
        for i in range(length_data):
            if data[i]:
                data[i] = TreeNode(data[i])

        visited = [False]*length_data
        for i in range(length_data):
            if visited[i] == False or data[i] != None:
                if 2*i+1 < length_data:
                    data[i].left = data[2*i+1]
                    visited[2*i+1] = True
                if 2*i+2 < length_data:
                    data[i].right = data[2*i+2]
                    visited[2*i+2] = True
            visited[i] = True
        return data[0]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
root = TreeNode(1)
tree_node_2 = TreeNode(2)
tree_node_3 = TreeNode(3)
tree_node_4 = TreeNode(4)
tree_node_5 = TreeNode(5)

root.left = tree_node_2
root.right = tree_node_3
tree_node_3.left = tree_node_4
tree_node_3.right = tree_node_5

codec = Codec()
print codec.serialize(codec.deserialize(codec.serialize(root_temp)))