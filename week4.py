class Stack():
    def __init__(self):
        self.__index = [ ]
    def push(self, item):
        self.item = item
        self.__index.append(self.item)
    def pop(self):
        try:
            self.__index.pop()
        except:
            return None

class Deque():
    def__init__(self):
        self.__index = []
    def addFront(item):
        self.item = curNode
    ##def addRear(item):
    ##def removeFront():
    ##def removeRear():
    ##def isEmpty():
        ##if()
          ##  return True
        ##else 
            ##return False 
