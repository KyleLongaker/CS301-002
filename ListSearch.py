# Group members: Katelyn Juhl, Kyle Longaker

# Kyle         
def search_sorted_list(sorted_list, item, start=0, end=None):
    # Initialize `end` during the first call
    if end is None:
        end = len(sorted_list) - 1

    # Base case
    if start > end:
        return False

    # Find the middle index
    mid = (start + end) // 2

    # If the item is at the mid, return True
    if sorted_list[mid] == item:
        return True
    # If the item is smaller than mid, recursively search the left half
    elif sorted_list[mid] > item:
        return search_sorted_list(sorted_list, item, start, mid - 1)
    # If the item is larger than mid, recursively search the right half
    else:
        return search_sorted_list(sorted_list, item, mid + 1, end)

# Katelyn  
class HashTable():
    def __init__(self):
          self.stack = []
          self.size = 1000
          self.slots = [None] * self.size
          self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
           return None

    def hash_function(self, key):
        return key%self.size
        
    def contains(self,item,key):
        if item == key:
             return True 
        else:
             return False
            
    def items(self,key):
        return self.get(key)
    
# Katelyn 
# In order to convert our hashlist into a dictionary we can create two lists, one for keys and one for values.
# We can then zip those lists together in order to get key value pairs and then convert those lists into a dictionary. 
