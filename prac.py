def Node(self,data,next):
    self.data = data
    self.next = next
class LL:
    def __init__(self):
        self.head= None
    def insert(self,data):
        
        if(self.head == None):
            self.head=Node(data,None)
        
            