class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left_child(self, node):
        self.left = node

    def add_right_child(self, node):
        self.right = node

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def print_all_paths(self):
        self.print_paths(self.root, [])

    def print_paths(self, node, path):
        if node is None:
            return

        path.append(node.data)

        if node.left is None and node.right is None:
            print(path)
            
        else:
            
            self.print_paths(node.left,path.copy())
            self.print_paths(node.right,path.copy())

# take user input
input_str = input()
inputs = input_str.split()

root, node1, node2, node3, node4, node5, node6 = [BinaryTreeNode(val.strip()) for val in inputs]

root.add_left_child(node1)
root.add_right_child(node2)
node1.add_left_child(node3)
node1.add_right_child(node4)
node2.add_left_child(node5)
node2.add_right_child(node6)

# call the function
tree = BinaryTree(root)
tree.print_all_paths()