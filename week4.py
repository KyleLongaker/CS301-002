class Stack():
    #running time - takes O(1) because it is essentially an index assignment
    def __init__(self):
        self.stack = [ ]
    #running time - takes O(2) because it requires an index assignment and an append
    def push(self, item):
        self.item = item
        self.stack.append(self.item)
    #running time - takes O(1) because it is only a pop or returns None
    def pop(self):
        try:
            return self.stack.pop()
        except:
            return None
    #running time - takes O(1) because it just returns a value from a given index
    def peek(self):
        return self.stack[len(self.stack) - 1]
    #??????????????????
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    #??????????????????
    def size(self):
        return len(self.stack)

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
