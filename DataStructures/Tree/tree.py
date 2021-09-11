# A tree is a non linear hierarchical data structure
# that consist of nodes connected by edges

# <-- Terms used -->

# Root         - it is the topmost node if a tree
# HEight(Node) - No of edges from the node to the deepest leaf
# Depth        - No of edges from root to the node
# Heigth(tree) - Height of root node
# Degree(node) - Total No of breaches of that node
# Forest       - Collection of disjoint trees

# <-- Uses of Trees -->

# Binary Search Trees(BSTs) are used to quickly check whether an element is present in a set or not.
# Heap is a kind of tree that is used for heap sort.
# A modified version of a tree called Tries is used in modern routers to store routing information.
# Most popular databases use B-Trees and T-Trees, which are variants of the tree structure we learned above to store their data
# Compilers use a syntax tree to validate the syntax of every program you write.

# <-- tree traversal -->

# Inorder   - left subtree -->       root    --> right subtree
# Preorder  -      root    --> left subtree  --> right subtree
# PostOrder - left subtree --> right subtree -->      root

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def inorder(root):
    if root:
        # Traverse left
        inorder(root.left)
        # traverse root
        print(str(root.data) + "-->", end='')
        # traverse right
        inorder(root.right)


def postorder(root):
    if root:
        # traverse left
        postorder(root.left)
        # traverse right
        postorder(root.right)
        # traverse root
        print(str(root.data) + "-->", end='')


def preorder(root):
    if root:
        # print root
        print(str(root.data) + "-->", end='')
        # traverse left
        preorder(root.left)
        # traverse right
        preorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)


print("Inorder traversal")
inorder(root)

print("\nPreoreder Travcersal")
preorder(root)

print("\nPostorder Traversal")
postorder(root)
