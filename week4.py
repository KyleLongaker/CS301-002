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
    

        
