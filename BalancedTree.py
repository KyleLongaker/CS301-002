## Group Members: Katelyn Juhl & Kyle Longaker

class Node:
    """A Node in a AVL Tree."""
  def __init__(self, key, payload=None):
        self.key = key
        self.payload = payload
        self.left = None
        self.right = None
    
class AVLTree(object):
  def __init__(self):
        self.root = None
  
    # Function to insert a node
  def insert_node(self, root, key):
        # Find the correct location and insert the node
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
 """
 Average case: O(log n), where n is the number of nodes in the tree.
 Worst case: O(n), this occurs when the tree becomes a linked list (degenerate tree).
 """

    # Function to delete a node
  def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root
          
        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        balanceFactor = self.getBalance(root)
        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
  """"
  Average case: O(log n), where n is the number of nodes in the tree.
  Worst case: O(n), occurs when the tree is a degenerate tree (like a linked list).
  """

  def search(self, key):
        return self._search_rec(self.root, key)
  """"
  Average case: O(log n), where n is the number of nodes in the tree.
  Worst case: O(n), occurs when the tree is a degenerate tree (like a linked list).
  """
  
  def _search_rec(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_rec(node.left, key)
        else:
            return self._search_rec(node.right, key)

  def sortedlist(self):
        result = []
        self._inorder_traversal(self.root, result)
        return [item[0] for item in result]
  """
  Runs in O(n) time for all cases as it must visit every node.
  """
  
  def reverseSortedList(self):
        result = []
        self._inorder_traversal(self.root, result)
        return [item[0] for item in reversed(result)]
 """
 Runs in O(n) time for all cases as it must visit every node.
 """

        
myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = myTree.insert_node(root, num)
myTree.printHelper(root, "", True)
key = 13
root = myTree.delete_node(root, key)
print("After Deletion: ")
myTree.printHelper(root, "", True) 


###################################################################################################

import heapq

class PriorityQueue:
    def __init__(self):
        # Initializes an empty heap.
        # The heap invariant is always satisfied.
        self.heap = []
        heapq.heapify(self.heap)  # Ensures the heap property; O(n) time, but for an empty heap, it's O(1).

    def insert(self, item, key):
        """
        Inserts an item with its associated key into the priority queue.
        After insertion, ensures that the internal binary heap satisfies the heap order property.
        Average Case: O(log n), Worst Case: O(log n) -- where n is the number of items in the priority queue.
        """
        heapq.heappush(self.heap, (-key, item))  # Negate the key for max heap behavior.

    def pop(self):
        """
        Returns a tuple (key, item) that is the item associated with the largest key in the queue.
        After popping, the priority queue ensures that the internal binary heap maintains the heap order property.
        If the queue is empty, returns None.
        Average Case: O(log n), Worst Case: O(log n) -- where n is the number of items in the priority queue.
        """
        if not self.heap:
            return None  # Handle empty heap case.
        key, item = heapq.heappop(self.heap)
        return (-key, item)  # Return the original key value.

    def returnQueue(self):
        """
        Returns a list representation of the priority queue that is ordered by how the contents of the queue will be
        returned by successive pop() operations.
        This method does not affect the original queue.
        Note: This operation involves creating a sorted copy of the heap, so it is more costly.
        Average Case: O(n log n), Worst Case: O(n log n) -- where n is the number of items in the priority queue.
        """
        # Returns a sorted list of tuples with negated keys to reflect the true priority order.
        return sorted(self.heap, key=lambda x: x[0], reverse=True)

# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert("Task 1", 3)
    pq.insert("Task 2", 2)
    pq.insert("Task 3", 1)
    print("Queue after inserts:", pq.returnQueue())
    print("Popping highest priority item:", pq.pop())
    print("Queue after popping one item:", pq.returnQueue())



########################################
"""Combined together"""

class Node:
    """A Node in an AVL Tree."""
    def __init__(self, key, payload=None):
        self.key = key
        self.payload = payload
        self.left = None
        self.right = None
        self.height = 1  # Height of the node for balancing.

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key, payload=None):
        # O(log n) - Height-balanced tree ensures logarithmic depth
        self.root = self._insert_node(self.root, key, payload)

    def _insert_node(self, root, key, payload=None):
        # O(log n) - Each insertion requires traversing the height of the tree
        if not root:
            return Node(key, payload)
        elif key < root.key:
            root.left = self._insert_node(root.left, key, payload)
        else:
            root.right = self._insert_node(root.right, key, payload)

        # Balancing the tree
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance_factor = self._get_balance(root)

        # Four cases to keep tree balanced
        if balance_factor > 1:
            if key < root.left.key:
                return self._right_rotate(root)
            else:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root)
        if balance_factor < -1:
            if key > root.right.key:
                return self._left_rotate(root)
            else:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root)
        return root

    def delete(self, key):
        # O(log n) - Height-balanced tree ensures logarithmic depth
        self.root, deleted = self._delete_node(self.root, key)
        return deleted

    def _delete_node(self, root, key):
        # O(log n) - Deletion requires traversing the height of the tree
        if not root:
            return root, False
        if key < root.key:
            root.left, deleted = self._delete_node(root.left, key)
        elif key > root.key:
            root.right, deleted = self._delete_node(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None or root.right is None:
                temp = root.left if root.left else root.right
                root = None if temp is None else temp
                deleted = True
            else:
                # Node with two children: Get the inorder successor
                temp = self._get_min_value_node(root.right)
                root.key, root.payload = temp.key, temp.payload
                root.right, _ = self._delete_node(root.right, temp.key)
                deleted = True

        if root is None:
            return root, deleted

        # Balancing the tree
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance_factor = self._get_balance(root)

        # Four cases to keep tree balanced
        if balance_factor > 1:
            if self._get_balance(root.left) >= 0:
                return self._right_rotate(root), deleted
            else:
                root.left = self._left_rotate(root.left)
                return self._right_rotate(root), deleted
        if balance_factor < -1:
            if self._get_balance(root.right) <= 0:
                return self._left_rotate(root), deleted
            else:
                root.right = self._right_rotate(root.right)
                return self._left_rotate(root), deleted

        return root, deleted

    def search(self, key):
        # O(log n) in average case, O(n) in worst case (degenerate tree)
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        # O(log n) in average case, O(n) in worst case (degenerate tree)
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_rec(node.left, key)
        else:
            return self._search_rec(node.right, key)

    def sorted_list(self):
        # O(n) - In-order traversal visits every node once
        result = []
        self._inorder_traversal(self.root, result)
        return [item.key for item in result]

    def reverse_sorted_list(self):
        # O(n) - Same as sorted_list, but reverses the result
        result = []
        self._inorder_traversal(self.root, result)
        return [item.key for item in reversed(result)]

    # Utility methods below are all O(1) or O(log n) due to the height-balanced nature of AVL trees.

    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node)
            self._inorder_traversal(node.right, result)

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def _right_rotate(self, y):
        # O(1) - Rotation operations are constant time
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x

    def _left_rotate(self, x):
        # O(1) - Rotation operations are constant time
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_min_value_node(self, root):
        # O(log n) - Requires traversing to the leftmost node
        current = root
        while current.left is not None:
            current = current.left
        return current



