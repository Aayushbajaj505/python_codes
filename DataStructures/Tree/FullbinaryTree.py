# also known as proper binary tree
# every parent node/internal node has either two or no children
# can lean left or right does not mattera

# Terms:
# i = the number of internal nodes
# n = be the total number of nodes
# l = number of leaves
# λ = number of levels

# <-- Theorems of Full Binary Tree-->

# The number of leaves            =  i + 1.
# The total number of nodes       =  2i + 1.
# The number of internal nodes    =  (n – 1) / 2.
# The number of leaves            =  (n + 1) / 2.
# The total number of nodes       =  2l – 1.
# The number of internal nodes    =  l – 1.
# The number of leaves is at most =  2λ - 1.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isFullTree(root):
    # check if empty
    if root is None:
        return True
    # check onl;y if root node is present and no leaves
    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return (isFullTree(root.left)) and isFullTree(root.right)
    return False


root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)

if isFullTree(root):
    print(True)
else:
    print(False)
