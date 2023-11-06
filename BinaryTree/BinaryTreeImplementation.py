class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        print(f'Node {data} was created')

    def add_left_child(self, node):
        self.left = node
        print(f'Node {node.data} was added as a left child of {self.data}')

    def add_right_child(self, node):
        self.right = node
        print(f'Node {node.data} was added as a right child of {self.data}')
    
class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        print('A tree was created')


root_node = BinaryTreeNode("root")
left_node = BinaryTreeNode("left")
right_node = BinaryTreeNode("right")


root_node.add_left_child(left_node)
root_node.add_right_child(right_node)

tree = BinaryTree(root_node)