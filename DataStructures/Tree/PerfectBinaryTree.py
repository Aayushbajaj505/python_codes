# every internal node has exactly two child nodes
# and all the leaf nodes are at the same level
# All the internal nodes have a degree of 2.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# calcualte depth


def calculatedepth(node):
    d = 0
    while node is not None:
        d = d+1
        node = node.left
    return d


def isperfect(root, d, level=0):
    # empty tree check
    if root is None:
        return True
    # only root element check
    if root.left is None and root.right is None:
        return (d == level+1)
    if root.left is None or root.right is None:
        return False
    return (isperfect(root.left, d, level+1)) and isperfect(root.left, d, level+1)
