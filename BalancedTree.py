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






