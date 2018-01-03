class hashingtable():
    def __init__(self,length=100):
        self.data = [[None,None] for i in range (length)]
    def insert(self,x,currentIndex=None):
        if currentIndex == None:
            currentIndex = self.hashString(x[0])
        if self.data[currentIndex][0]==None:
            self.data[currentIndex]=x
        else:
            self.insert(x,currentIndex+1)
    def find(self,x,currentIndex=None):
        if currentIndex == None:
            currentIndex = self.hashString(x)
        if self.data[currentIndex][0]==x:
            return self.data[currentIndex][1]
        elif self.data[currentIndex][0]==None:
            return -1
        else:
            return self.find(x,currentIndex+1)
    def hashString(self,x):
        acc = 0
        for i in x:
            acc = acc +ord(i)
        return acc%10
    def printArray(self):
        for i in self.data:
            print (i)

a=hashingtable()
a.insert(['Apple', 'Apply Company'])
a.insert(['Google','Google Scholar'])
a.insert(['Sony','Sony Playstation'])
print(a.find('Sony'))
print(a.find('Apple'))

