#Katelyn  
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
        
    def contains(self,item):
        if item == key:
             return True 
             return (old_hash + 1) % size
        else:
             return False
            
    def items(self,key):
        return self.get(key)
        
      
#Katelyn 
In order to convert our hashlist into a dictionary we can create two lists, one for keys and one for values.
We can then zip those lists together in order to get key value pairs and then convert those lists into a dictionary. 
































