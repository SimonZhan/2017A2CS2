
nullPtr = -1
##node initialisation
class listNode:
    def __init__(self):
        self.value = ""
        self.nextPtr = nullPtr
##list functions
class List(object):
##list initialisation
    def __init__(self):
        self.freePtr = 0
        self.startPtr = nullPtr
        self.records = []
        newNode = None
        for i in range (0,10):
            newNode = listNode()
            newNode.nextPtr = i - 1
            self.records.append(newNode)
        newNode.nextPtr = nullPtr
    def insertNode(self, newItem):
        if self.freePtr != nullPtr:
            self.newPtr = self.freePtr
            self.records[self.freePtr].value = newItem
            self.freePtr = self.records[self.freePtr].nextPtr
            thisnodePtr = self.startPtr
            prevnodePtr = nullPtr
            while thisnodePtr != nullPtr:
                prevnodePtr = thisnodePtr
                thisnodePtr = self.records[thisnodePtr].nextPtr
            if prevnodePtr == nullPtr:
                self.records[self.newPtr].nextPtr = self.startPtr
                self.startPtr = self.newPtr
            else:
                self.records[self.newPtr].nextPtr = self.records[prevnodePtr].nextPtr
                self.records[prevnodePtr].nextPtr = self.newPtr
##pop()
    def pop(self):
        self.startPtr = self.records[self.startPtr].nextPtr
        del self.records[self.startPtr]
        
#print list
    def printList(self):
        currentPtr = self.startPtr
        while currentPtr != nullPtr:
            print(self.records[currentPtr].value, end=" ")
            currentPtr = self.records[currentPtr].nextPtr
        


##create a list
l = List()
l.insertNode(1)
l.insertNode(7)
l.insertNode(3)
l.insertNode(8)
l.insertNode(5)
l.insertNode(6)
l.printList()
