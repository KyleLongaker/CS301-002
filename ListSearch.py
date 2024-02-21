class HashTable():
    def __init__(self):
      self.stack = []
      self.size = 1000
      self.slots = [None] * self.size
      self.data = [None] * self.size
        
    def hash_function(self, key):
      return key%self.size
        
    def put(self, key):
        insert_pos = self.hash_function(key)
    if self.slots[insert_pos] == None:
        self.slots[insert_pos] = key
    else:
        insert_pos = self.rehash(insert_pos)
        while self.slots[insert_pos] != None and self.slots[insert_pos] != key:
            insert_pos = self.rehash(insert_pos)
        if self.slots[insert_pos] == None:
            self.slots[insert_pos] = key
            
    def contains(self,item):

    def items():
      

































