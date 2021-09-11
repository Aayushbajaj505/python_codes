# thisd queue avoids wastage of space
class MYCircularQUeue():
    def __init__(self, k):
        self.k = k
        self.queue = [None]*k
        self.head = self.tail = -1
    # insert an elemet

    def Enqueue(self, data):
        if(slef.tail+1) % self.k == self.head:
            print("The circular QUeue is full")
        elif(self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data
