## Group members : Katelyn Juhl & Kyle Longaker
 
class BinaryTree:
   def __init__(self):
        self.root = None
        self.size = 0
     
   def insert(item, tree):
    if (item < tree.entry):
        if (tree.left != None):
            insert(item, tree.left)
        else:
            tree.left = Tree(item)
    else:
        if (tree.right != None):
            insert(item, tree.right)
        else:
            tree.right = Tree(item)
## Best Big O Running time: O(n^2), because we can simplify it into quicker time that we are implementing towards. 
## Worst Big O Running time: O(n^4), because of the if and else statements and how long it takes to implement through each statement.
## Average Big O Running time: O(n^2)

  def search(self, key):
    if self.root:
        result = self._get(key, self.root)
        if result:
            return result.value
    return None
## Best Big O Running time: O(n), beacuse the timing it takes to run can be simpiler.
## Worst Big O Running time: o(n^2), because if you expand the code it can become more clear what is happening but the nested for loops would cause it to take longer to run. 
## Average Big O Running time: O(2n)

class Node:
    def __init__(self, key, payload=None):
        self.key = key
        self.payload = payload
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, payload=None):
        if self.root is None:
            self.root = Node(key, payload)
        else:
            self._insert_rec(self.root, key, payload)
    
    def _insert_rec(self, node, key, payload):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, payload)
            else:
                self._insert_rec(node.left, key, payload)
        else:
            if node.right is None:
                node.right = Node(key, payload)
            else:
                self._insert_rec(node.right, key, payload)
    
    def inorder(self, node):
        if node is None:
            return ""
        lres = self.inorder(node.left)
        rres = self.inorder(node.right)
        return lres + (str(node.key) + " " + (node.payload if node.payload else "") + "\n") + rres

    def flatten(self):
        traversal = []
        self._inorder_traversal(self.root, traversal)
        
        dummy = Node(-1)
        prev = dummy
        for val in traversal:
            prev.right = Node(val[0], val[1])
            prev = prev.right

        return dummy.right

    def _inorder_traversal(self, node, traversal):
        if node is not None:
            self._inorder_traversal(node.left, traversal)
            traversal.append((node.key, node.payload))
            self._inorder_traversal(node.right, traversal)
    
    def print_flattened_tree(self, node):
        curr = node
        while curr is not None:
            print(f"{curr.key} {(curr.payload if curr.payload else '')}", end=" -> " if curr.right else "")
            curr = curr.right
        print()

if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(5, "Root")
    bt.insert(3, "Left")
    bt.insert(7, "Right")
    bt.insert(2, "Left of Left")
    bt.insert(4, "Right of Left")
    bt.insert(6, "Left of Right")
    bt.insert(8, "Right of Right")

    print("In-order Traversal:")
    print(bt.inorder(bt.root))

    print("Flattened Tree:")
    flattened_root = bt.flatten()
    bt.print_flattened_tree(flattened_root)

# Big O Runtime Complexity Explanation

"""
Insert Method:
- Best and average case: O(log n), where n is the number of nodes in the tree. This assumes the tree is reasonably balanced, allowing the insert operation to discard half of the possible locations at each step.
- Worst case: O(n), in a skewed tree where every node has only one child. This degenerates the insert operation into a linear search.

Inorder Traversal (inorder and _inorder_traversal methods):
- O(n) for all cases, as it traverses every node exactly once, where n is the number of nodes in the tree. The complexity is the same regardless of the tree's shape.

Flatten Method:
- O(n), since it involves an in-order traversal of the tree to collect all nodes in a list, followed by iterating over this list to create the "flattened" tree. Each of these steps involves going over each node once, resulting in linear time complexity.

Note: The complexities assume that tree operations like insertions and traversals do not change the overall structure of the tree significantly enough to affect the average height of the tree.
"""

################################################
"""New code to look at"""

## Group members : Katelyn Juhl & Kyle Longaker

class Node:
    """A Node in a Binary Search Tree."""
    def __init__(self, key, payload=None):
        self.key = key
        self.payload = payload
        self.left = None
        self.right = None

class BinaryTree:
    """A Binary Search Tree implementation."""
    def __init__(self):
        self.root = None
    
    def insert(self, key, payload=None):
        """Insert a new element into the BST."""
        if self.root is None:
            self.root = Node(key, payload)
        else:
            self._insert_rec(self.root, key, payload)
    
    def _insert_rec(self, node, key, payload):
        """Recursive helper for the insert method."""
        if key < node.key:
            if node.left is None:
                node.left = Node(key, payload)
            else:
                self._insert_rec(node.left, key, payload)
        else:
            if node.right is None:
                node.right = Node(key, payload)
            else:
                self._insert_rec(node.right, key, payload)
    
    def inorder(self, node):
        """Perform an in-order traversal."""
        if node is None:
            return ""
        lres = self.inorder(node.left)
        rres = self.inorder(node.right)
        return lres + (str(node.key) + " " + (node.payload if node.payload else "") + "\n") + rres

    def flatten(self):
        """Flatten the BST to a linked list in-place."""
        traversal = []
        self._inorder_traversal(self.root, traversal)
        
        dummy = Node(-1)
        prev = dummy
        for val in traversal:
            prev.right = Node(val[0], val[1])
            prev = prev.right

        return dummy.right

    def _inorder_traversal(self, node, traversal):
        """Helper for in-order traversal to support flatten."""
        if node is not None:
            self._inorder_traversal(node.left, traversal)
            traversal.append((node.key, node.payload))
            self._inorder_traversal(node.right, traversal)
    
    def print_flattened_tree(self, node):
        """Print the nodes of a flattened tree."""
        curr = node
        while curr is not None:
            print(f"{curr.key} {(curr.payload if curr.payload else '')}", end=" -> " if curr.right else "")
            curr = curr.right
        print()

# Corrected Big O Runtime Complexity Analysis
"""
Insert Method:
- Best and average case: O(log n) for a balanced tree.
- Worst case: O(n) for a skewed tree (degenerates to a linked list).

Search Method (Not provided but typically):
- Best case: O(1) if the key is at the root.
- Average case: O(log n) for a balanced tree.
- Worst case: O(n) for a skewed tree.

Inorder Traversal and Flatten Method:
- Both operations are O(n), as they visit each node exactly once.
"""

if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(5, "Root")
    bt.insert(3, "Left")
    bt.insert(7, "Right")
    bt.insert(2, "Left of Left")
    bt.insert(4, "Right of Left")
    bt.insert(6, "Left of Right")
    bt.insert(8, "Right of Right")

    print("In-order Traversal:")
    print(bt.inorder(bt.root))

    print("Flattened Tree:")
    flattened_root = bt.flatten()
    bt.print_flattened_tree(flattened_root)








