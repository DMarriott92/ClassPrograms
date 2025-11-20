### Constructing a queue
class CircularQueue:
    def __init__(self,maxItems):
        self.items = [None]*maxItems
        self.front = 0
        self.rear = -1
        self.size = 0
        self.maxSize = maxItems
    
    def show(self):
        print("lists and pointers", self.iitems, self.front, self.rear, "size =",self.size)

    def size(self):
        return self.size

q = CircularQueue(5)
