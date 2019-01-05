import sample_tree

# Similarly for in/post order
def preorder(root, visited):
    if not root:
        return

    visited.append(root.data)
    preorder(root.left, visited)
    preorder(root.right, visited)


visited = []
preorder(sample_tree.node1, visited)
print visited

# Preorder  [1, 2, 4, 5, 3, 6, 7]
# Inorder   [4, 2, 5, 1, 6, 3, 7]
# Postorder [4, 5, 2, 6, 7, 3, 1]


def preorder_nonrecursive(root, visited):
    stack = [root]
    while stack:
        element = stack.pop()
        visited.append(element.data)

        if element.right: stack.append(element.right)
        if element.left :stack.append(element.left)

visited = []
preorder_nonrecursive(sample_tree.node1, visited)
print "Preorder : ", visited
#
# def preorder_nonrecursive_2(root):
#     if not root:
#         return
#     result = []
#     stack = []
#     node = root
#     while stack or node:
#         if node:
#             stack.append(node)
#             node = node.left
#         else:
#             node = stack.pop()
#             if node.right and not node.right.data in result:
#                 stack.append(node)
#                 node = node.right
#             else:
#                 result.append(node.data)
#                 node = None
#     return result


def inorder_nonrecursive(root, visited):
    stack = [root]
    while stack:
        element = stack.pop()
        if element.left:
            if element.right:
                stack.append(element.left)
            else:
                visited(element.right)
            visited.append(element.data)
            stack.append(element.left)
        # if element.left: stack.append(element.left)

visited = []
inorder_nonrecursive(sample_tree.node1, visited)
print "Inorder : ", visited


