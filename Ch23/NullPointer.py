NullPointer = -1
class ListNode():
    def __init__(self,x,y):
        self.Value = x
        self.Next = y

class InitialiseList():
    def __init__(self):
        self.StartPointer = NullPointer
        self.FreeListPtr = 0
        for i in range(10):


