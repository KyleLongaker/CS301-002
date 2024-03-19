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










