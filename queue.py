### Constructing a queue
class CircularQueue:
    def __init__(self,maxItems):
        self.items = [None]*maxItems
        self.front = 0
        self.rear = -1
        self.size = 0
        self.maxSize = maxItems
    
    def enQueue(self, item):
        if self.size == self.maxSize:
            print("Queue is full, size =", self.size)
        else:
            self.rear = (self.rear + 1)%(self.maxSize)
            self.size += 1
            self.items[self.rear] = item


    def deQueue(self):
        if (self.size == 0):
            return "Queue Empty"
        else:
            first = self.items[self.front]
            self.size -= 1
            self.front = (self.front + 1)%(self.maxSize)
            return first

    def isFull(self):
        print("self.size, self.maxSize", self.size, self.maxSize)
        return self.size == self.maxSize

    def isempty(self):
        print("self.size, self.maxSize", self.size, self.maxSize)
        return self.size == 0

    def show(self):
        print("lists and pointers", self.iitems, self.front, self.rear, "size =",self.size)

    def size(self):
        return self.size
    
    def showFront(self):
        print(self.items[self.front])

q = CircularQueue(10)
q.enQueue("320")