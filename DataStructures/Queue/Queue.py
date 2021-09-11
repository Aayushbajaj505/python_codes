# FIFO principle
# Basic operations of Queue
# Enqueue, Dequeue, IsEmpty, IsFull, Peek

class Queue:
    def __init__(self):
        self.queue = []

    def Enqueue(self, item):
        self.Enqueue.append(item)

    def Dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
# Applications of queue
# CPU scheduling, disk scheduling

# There are 4 diff types of queue
# simple, circular, priority, double ended
