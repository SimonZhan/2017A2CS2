#Simon Zhan
null = -1
class queue():
    def __init__(self,x,y):
        self.value = x
        self.next = y

class Queue():
    def __init__(self):

        self.free = null
        self.start = null
        self.prev = null
        self.end = null
        self.data = [queue(None,i) for i in range(1,10)]
        self.data.append(queue(None,-1))

    def enqueue(self,x):
        if self.free != null:
            if self.start == null:
                self.start = self.free
            temp = self.data[self.free].next
            self.data[self.free]=queue(x,-1)
            if self.prev != null:
                self.data[self.prev].next = self.free
            self.prev = self.free
            self.free = temp


    def dequeue(self):
        if self.start != null:
            tempPointer = self.free
            self.free = self.start
            self.start = self.data[self.free].next
            self.data[self.free].next = tempPointer
            return self.data[self.free].value





