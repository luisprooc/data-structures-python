class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        current_node = self.root
        preorder_checkpoint = None

        if current_node:
            while current_node:

                if current_node.right:
                    preorder_checkpoint = current_node

                if find_val == current_node.value:
                    return True

                elif not current_node.left:
                    print(current_node.value,preorder_checkpoint.value)
                
                current_node = current_node.left
                

        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        nodes = ""
        current_node = self.root
        preorder_checkpoint = None

        if current_node:
            while current_node:

                nodes += str(current_node.value) + "-"
                
                if current_node.right:
                    preorder_checkpoint = current_node

                current_node = current_node.left


        return nodes

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)


# Test search
# Should be True
# Should be False
print(tree.search(6))
#print (tree.search(6))
print (tree.print_tree())

"""
# Test print_tree
# Should be 1-2-4-5-3
print (tree.print_tree())
"""