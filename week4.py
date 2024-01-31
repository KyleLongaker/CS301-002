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
import time 

class Queue:
    def __init__(self, item ):
        self.items = item

    def enqueue(self, item):
        start_time = time.time()
        self.items.append(item)
        end_time = time.time()
        total_time = end_time - start_time
        print("******* Total Time Taken by -- ", item," --" , total_time,"s")

    def dequeue(self):
        start_time = time.time()
        if self.isEmpty():
         return None
        end_time = time.time()
        total_time = end_time - start_time
        print("******* Total time taken by dequeue -----> " , total_time,"s",)
        return self.items.pop(0)
        

    def isEmpty(self):
      start_time = time.time()
      if (len(self.items) == 0):
       end_time = time.time()
       total_time = end_time - start_time
       print("******** Total time taken by isEmpty -----> ", total_time,"s")
       return True
      else:
        end_time = time.time()
        total_time = end_time - start_time
        print("******* Total time taken by isEmpty -----> ", total_time, "s")
        return False

    def size(self):
       
       return len(self.items)


# testing the code 
number = ["Green"]
testing  = Queue(number)
print("Checkig queue is empty or  not?", testing.isEmpty())
testing.enqueue("Aman")
testing.enqueue("Beer")
testing.enqueue("C")
print("Queue size:", testing.size())
print("Dequeue:", testing.dequeue()) 
print("Queue size after dequeue:", testing.size())
print("Is the queue empty?", testing.isEmpty()) 


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
