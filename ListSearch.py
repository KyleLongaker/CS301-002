import time

# Group members: Katelyn Juhl, Kyle Longaker

# Kyle
def search_sorted_list(sorted_list, item, start=0, end=None):
    start_time = time.time()  # Start timing
    # Initialize `end` during the first call
    if end is None:
        end = len(sorted_list) - 1

    # Base case
    if start > end:
        end_time = time.time()  # End timing
        print(f"search_sorted_list execution time: {end_time - start_time} seconds")
        return False

    # Find the middle index
    mid = (start + end) // 2

    # If the item is at the mid, return True
    if sorted_list[mid] == item:
        end_time = time.time()  # End timing
        print(f"search_sorted_list execution time: {end_time - start_time} seconds")
        return True
    # If the item is smaller than mid, recursively search the left half
    elif sorted_list[mid] > item:
        return search_sorted_list(sorted_list, item, start, mid - 1)
    # If the item is larger than mid, recursively search the right half
    else:
        return search_sorted_list(sorted_list, item, mid + 1, end)
    # Big O runtime: O(log n) due to the binary search algorithm's halving approach.

# Katelyn & Kyle
class HashTable:
    def __init__(self, size=1000):
        self.size = size
        self.slots = [None] * self.size  # This will store the keys
        self.data = [None] * self.size  # This will store the values
        # Big O runtime for init: O(n) where n is the size, due to initializing the hash table.

    def put(self, key, data):
        start_time = time.time()  # Start timing
        hash_value = self.hash_function(key)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            # If the slot is already taken by the same key, update the data
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
                end_time = time.time()  # End timing
                print(f"HashTable put execution time: {end_time - start_time} seconds")
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
        end_time = time.time()  # End timing
        print(f"HashTable put execution time: {end_time - start_time} seconds")
        # Big O runtime: Average case O(1), worst case O(n) due to linear probing in case of collisions.

    def hash_function(self, key):
        return key % self.size
        # Big O runtime: O(1) for calculating hash value.

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size
        # Big O runtime: O(1) for calculating new hash value.

    def contains(self, key):
        start_time = time.time()  # Start timing
        start_slot = self.hash_function(key)
        position = start_slot
        while self.slots[position] is not None:
            if self.slots[position] == key:
                end_time = time.time()  # End timing
                print(f"HashTable contains execution time: {end_time - start_time} seconds")
                return True
            position = self.rehash(position)
            if position == start_slot:
                end_time = time.time()  # End timing
                print(f"HashTable contains execution time: {end_time - start_time} seconds")
                return False  # The table has been fully traversed
        end_time = time.time()  # End timing
        print(f"HashTable contains execution time: {end_time - start_time} seconds")
        return False
        # Big O runtime: Average case O(1), worst case O(n) due to linear probing and needing to traverse the table.

    def get(self, key):
        # This method remains unchanged
        pass

    def items(self):
        # This method remains unchanged
        pass

# Example usage
if __name__ == "__main__":
    # Example for search_sorted_list
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    search_sorted_list(sorted_list, 5)
    
    # Example for HashTable
    ht = HashTable()
    ht.put(1, "value1")
    ht.contains(1)


# Katelyn
# In order to convert our hashlist into a dictionary we can create two lists, one for keys and one for values.
# We can then zip those lists together in order to get key value pairs and then convert those lists into a dictionary.
