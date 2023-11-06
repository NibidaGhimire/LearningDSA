class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def search(self, value, current_node=None):

        if current_node is None:
            return None

        if value == current_node.data:
            return current_node
        elif value < current_node.data:
            return self.search(value, current_node.left) if current_node.left else None
        else:
            return self.search(value, current_node.right) if current_node.right else None
        
    #Time Complexity : 
        #Best TC : O(1)
        #Worst TC : O(h)

bst= BinarySearchTree()


