class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value, current_node=None):
        if self.root is None:
            self.root = BinarySearchTreeNode(value)
            return
    
        if current_node is None:
            current_node = self.root

        if value < current_node.data:
            if current_node.left is None:
                current_node.left = BinarySearchTreeNode(value)
            else:
                self.insert(value, current_node.left)
        elif value > current_node.data:
            if current_node.right is None:
                current_node.right = BinarySearchTreeNode(value)
            else:
                self.insert(value, current_node.right)


    def inorder_traversal(self, node, visited_nodes=None):
        if visited_nodes is None:
            visited_nodes = []

        if node:
            self.inorder_traversal(node.left, visited_nodes)
            visited_nodes.append(node.data)
            self.inorder_traversal(node.right, visited_nodes)

        return visited_nodes

bst = BinarySearchTree()

values_to_insert = [1,2,3,4,5]

for value in values_to_insert:
    bst.insert(value)

print(f'Inorder Traversal after Insertion {bst.inorder_traversal(bst.root)}')