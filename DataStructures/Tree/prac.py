class binartree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def addchild(self, data):
        # check to see if data already exsists then dont add
        if data == self.data:
            return
        # check if data is smaller or larger than the current code
        if data < self.data:
            if self.left:
                # if some other data also exists in the left subtree then keep on going untill the last
                self.left.addchild(data)
            else:
                self.left = binartree(data)
        else:
            if self.right:
                self.right.addchild(data)
            else:
                self.right = binartree(data)

    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder()
        return elements


def buildtree(elements):
    root = binartree(elements[0])

    for i in range(1, len(elements)):
        root.addchild(elements[i])
    return root


if __name__ == "__main__":
    numbers = [17, 1, 8, 20, 9, 23, 18, 34, 18, 4]
    numbertree = buildtree(numbers)
    print(numbertree.inorder())
