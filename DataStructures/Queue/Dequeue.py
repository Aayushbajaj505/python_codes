class Dequeue():
    def __init__(self):
        self.items = []

    def IsEmpty(self):
        return self.item == []

    def addRear(self, item):
        self.items.append(item)

    def addfront(self, item):
        self.items.insert(0, item)

    def removefront(self):
        return self.items.pop(0)

    def removerear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
