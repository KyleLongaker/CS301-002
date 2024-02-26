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
class HashTable:
    def __init__(self, size=1000):
        self.size = size
        self.slots = [None] * self.size  # This will store the keys
        self.data = [None] * self.size  # This will store the values

    def put(self, key, data):
        hash_value = self.hash_function(key)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            # If the slot is already taken by the same key, update the data
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
                return
            # Linear probing in case of collision
            next_slot = self.rehash(hash_value)
            while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                next_slot = self.rehash(next_slot)
            if self.slots[next_slot] is None:
                self.slots[next_slot] = key
                self.data[next_slot] = data
            else:
                # Update data if the key already exists
                self.data[next_slot] = data

    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def contains(self, key):
        start_slot = self.hash_function(key)
        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                return True
            position = self.rehash(position)
            if position == start_slot:
                return False  # The table has been fully traversed
        return False

    def get(self, key):
        start_slot = self.hash_function(key)
        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            position = self.rehash(position)
            if position == start_slot:
                break  # The table has been fully traversed
        return None

    def items(self):
        return [(self.slots[i], self.data[i]) for i in range(self.size) if self.slots[i] is not None]

# Katelyn
# In order to convert our hashlist into a dictionary we can create two lists, one for keys and one for values.
# We can then zip those lists together in order to get key value pairs and then convert those lists into a dictionary.
