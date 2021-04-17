from binary_tree import Node


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current = self.root

        while current:

            if new_val >= current.value:
                if not current.right:
                    current.right = Node(new_val)
                    return
               
                current = current.right

            else:
                if not current.left:
                    current.left = Node(new_val)
                    return 

                current = current.left


    def search(self, find_val):

        # If current node is equal to 
        # find_value, return True 
        if self.root.value == find_val:
            return True

        else:

            # If the find_value is bigger to current node and the current
            #  node not is a leaf, scroll right
            if find_val >= self.root.value and self.root.right:
                self.root = self.root.right
                return self.search(find_val)

            else:
                # If current node not is a leaf, scroll left
                if self.root.left:
                    self.root = self.root.right
                    return self.search(find_val)

                # This means that you reached a leaf and not 
                # find the expected value
                return False


    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)


# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))