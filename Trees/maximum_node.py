import sample_tree

max_value = float("-infinity")
def max(root):
    global max_value
    if not root:
        return
    elif root.data>max_value:
        max_value = root.data
    max(root.left)
    max(root.right)

max(sample_tree.node1)
print(max_value)
