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

*********************************************************************************************************************
    
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
# Deque or a “double-ended queue” combines the features of the Stack and Queue
###############################################
class Deque():
    def __init__(self):
        self.index = []
 ## The Big O run time for the addFront is O(n) ##
    def addFront(self, item):
        self.index.insert(0, item)
 ## The Big O run time for the addRear is O(n) ##
    def addRear(self, item):
        self.item.append(item)
 ## The Big O run time for the removeFront is O(n)  ##
    def removeFront(self):
        if self.index:
            return self.index.pop(0)
 ## The Big O run time for the removeRear is O(n)  ##
    def removeRear(self):
        if self.index:
            return self.index.pop()
## The Big O run time for the isEmpty is O(n) ##
    def isEmpty(self):
        return len(self.index) == 0
#####################################################
# Linked List Code
class Node():
    def __init__(self, item):
        self.item = item
        self.next = None

class Linked_List():
    def __init__(self):
        self.head = None

    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def remove(self, item):
        current_node = self.head
        prev_node = None

        if current_node is not None and current_node.item == item:
            self.head = current_node.next
            return
        
        while current_node is not None:
            if current_node.item == item:
                break
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            raise KeyError(f"Item {item} not found in the list.")
        
        if prev_node is None:
            self.head = current_node.next
        else:
            prev_node.next = current_node.next

    def search(self, item):
        current_node = self.head
        
        while current_node is not None:
            if current_node.item == item:
                return True
            current_node = current_node.next

        return False
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def size(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count
    
    def append(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def index(self, item):
        current_node = self.head
        position = 0

        while current_node is not None:
            if current_node.item == item:
                return position
            current_node = current_node.next
            position += 1

        if current_node is None:
            raise KeyError(f"Item {item} not found in the list.")
        
    def insert(self, position, item):
        if position < 0:
            raise ValueError("Position needs be a positive number.")
    
        new_node = Node(item)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
    
        current_node = self.head
        current_position = 0

        while current_node is not None and current_position < position - 1:
            current_node = current_node.next
            current_position += 1

        if current_node == None:
            raise ValueError("List is too short for the specified position.")
    
        new_node.next = current_node.next
        current_node.next = new_node

    def pop(self):
        if self.head is None:
            raise ValueError("List is empty. Cannot pop from an empty list.")
    
        if self.head.next is None:
            popped_item = self.head.item
            self.head = None
            return popped_item
    
        current_node = self.head

        while current_node.next.next == None:
            current_node = current_node.next

        popped_item = current_node.next.item
        current_node.next = None
        return popped_item

    def pop(self, pos):
        if self.head is None:
            raise ValueError("List is empty. Cannot pop from an empty list.")

        if pos < 0:
            raise ValueError("Position should be a positive number.")
    
        if pos == 0:
            popped_item = self.head.item
            self.head = self.head.next
            return popped_item
    
        current_node = self.head
        current_position = 0

        while current_node.next is not None and current_position < pos - 1:
            current_node = current_node.next
            current_position += 1

        if current_node.next is None:
            raise ValueError("Position is beyond the end of the list.")

        popped_item = current_node.next.item
        current_node.next = current_node.next.next
        return popped_item

    def display_list(self):
        current_node = self.head
        while current_node:
            print(current_node.item, end=" -> ")
            current_node = current_node.next
        print("None")
        
# Testing every function of the Linked List Class
linked_list = Linked_List() 

linked_list.add(7)
linked_list.add(5)
linked_list.add(9)
linked_list.add(3)
linked_list.add(11)
linked_list.add(1)
linked_list.add(13)
    
linked_list.remove(3)

linked_list.append(27)

linked_list.insert(5, 37)

print("Linked List:")
print(linked_list.display_list())
print(linked_list.search(11))
print(linked_list.isEmpty())
print(linked_list.size())
print(linked_list.index(11))
print(linked_list.pop(1))
print(linked_list.pop(3))

******************************************************************************************************
# Code for the double_linked list 
# I commented out the changes that are different from the linked_list code 

class Node():

    def __init__(self, item):
        self.item = item
        self.prev = None  # It has a pointer to the previous one
        self.next = None

    def __repr__(self):
        return self.data

class DoublyLinked_List():

    def __init__(self):
        self.head = None
        self.tail = None  # Adding the tail here 

    def add(self, item):
        new_node = Node(item)
        if self.head is None:  # To check if the list is empty 
            self.head = new_node # if its empty then set head and tail to newly created node 
            self.tail = new_node
        else:
            new_node.next = self.head # using same logic as in linked list
            self.head.prev = new_node
            self.head = new_node
    def remove(self, item):
     current_node = self.head
     prev_node = None

    def remove(self, item):
        current_node = self.head

        while current_node is not None: # running until the end of the linked list 
            if current_node.item == item:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next: # updating previous refrences 
                    current_node.next.prev = current_node.prev
                else:
                    self.tail = current_node.prev

                return

            current_node = current_node.next

        raise KeyError(f"Item {item} not found in the list.")

# After this every thing is same as in the linked_list code 
    def search(self, item):
        current_node = self.head

        while current_node is not None:
            if current_node.item == item:
                return True
            current_node = current_node.next

        return False

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def size(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def append(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def index(self, item):
        current_node = self.head
        position = 0

        while current_node is not None:
            if current_node.item == item:
                return position
            current_node = current_node.next
            position += 1

        if current_node is None:
            raise KeyError(f"Item {item} not found in the list.")

    def insert(self, position, item):
        if position < 0:
            raise ValueError("Position needs be a positive number.")

        new_node = Node(item)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        current_position = 0

        while current_node is not None and current_position < position - 1:
            current_node = current_node.next
            current_position += 1

        if current_node == None:
            raise ValueError("List is too short for the specified position.")

        new_node.next = current_node.next
        current_node.next = new_node

    def pop(self):
        if self.head is None:
            raise ValueError("List is empty. Cannot pop from an empty list.")

        if self.head.next is None:
            popped_item = self.head.item
            self.head = None
            return popped_item

        current_node = self.head

        while current_node.next.next == None:
            current_node = current_node.next

        popped_item = current_node.next.item
        current_node.next = None
        return popped_item

    def pop(self, pos):
        if self.head is None:
            raise ValueError("List is empty. Cannot pop from an empty list.")

        if pos < 0:
            raise ValueError("Position should be a positive number.")

        if pos == 0:
            popped_item = self.head.item
            self.head = self.head.next
            return popped_item

        current_node = self.head
        current_position = 0

        while current_node.next is not None and current_position < pos - 1:
            current_node = current_node.next
            current_position += 1

        if current_node.next is None:
            raise ValueError("Position is beyond the end of the list.")

        popped_item = current_node.next.item
        current_node.next = current_node.next.next
        return popped_item

    def display_list(self):
        current_node = self.head
        while current_node:
            print(current_node.item, end=" <-> ")
            current_node = current_node.next
        print("None")

# Testing the code for the doubly_linked list 

doubly_linked_list = DoublyLinked_List()
doubly_linked_list.add(7)
doubly_linked_list.add(5)
doubly_linked_list.add(9)
doubly_linked_list.add(3)
doubly_linked_list.add(11)
doubly_linked_list.add(1)
doubly_linked_list.add(13)

doubly_linked_list.remove(3)

doubly_linked_list.append(27)

doubly_linked_list.insert(5, 37)

print("Linked List:")
print(doubly_linked_list.display_list())
print(doubly_linked_list.search(11))
print(doubly_linked_list.isEmpty())
print(doubly_linked_list.size())
print(doubly_linked_list.index(11))
print(doubly_linked_list.pop(1))
print(doubly_linked_list.pop(3))

# It Works :)
