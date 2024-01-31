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
    #running time - takes O(1) because it just uses a length function
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    #running time - takes O(1) because it just uses a length function
    def size(self):
        return len(self.stack)

#A queue is similar to a stack, but it enforces FIFO (First In, First Out) access. 

class Queue:
  #running time - takes O(1) because it is essentially an index assignment
    def __init__(self):
        self.items = []
 #running time - takes O(2) because it requires an index assignment and an append items to the list 
    def enqueue(self, item):
        self.item = item 
        self.items.append(item)
 #running time - takes O(1) because it is only a pop or returns None
    def dequeue(self):
        
        if self.isEmpty():
         return None
        
        return self.items.pop(0)
 #running time - takes O(1) because it just uses a length function
    def isEmpty(self):
      if (len(self.items) == 0):
       return True
      else:
        return False

 #running time - takes O(1) because it just uses a length function
    def size(self):
       return len(self.items)


# Testing the code 
testing = Queue()
print("Checkig queue is empty or  not?", testing.isEmpty())
testing.enqueue("Aman")
testing.enqueue("Beer")
testing.enqueue("C")
print("Queue size:", testing.size())
print("Dequeue:", testing.dequeue()) 
print("Queue size after dequeue:",testing.size())
print("Is the queue empty?", testing.isEmpty()) 



class Deque():
    def __init__(self):
        self.index = []
    def addFront(self.item):
        self.item = FirstNode
        self.index(0, FirstNode)
    def addRear(self.item):
        self.item = LastNode
        LastNode = len(self.index)
    def removeFront():
        self.index.remove(index[0])
    def removeRear():
        self.index = LastNode
        LastNode = len(self.index)
        self.index.remove(index[LastNode])
    def isEmpty():
        if(self.index == "")
            print("Your list is empty")
            return False
        else
            print("Your list is not empty")
            return True
