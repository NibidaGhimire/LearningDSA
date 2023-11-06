# Replace ___ with your code

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
       
        
    def preorder_traversal(self, node, traversal=[]):
        if node is None:
            return traversal
        traversal.append(node.data)
        
        self.preorder_traversal(node.left,traversal)
        self.preorder_traversal(node.right,traversal)

        return traversal
        
    def postorder_traversal(self, node, traversal=[]):
        
        if node is None:
            return traversal
        self.postorder_traversal(node.left,traversal)
        self.postorder_traversal(node.right,traversal)
        traversal.append(node.data)
        return traversal
    
    def inorder_traversal(self, node, visited_nodes=[]):
        if node is not None:
            self.inorder_traversal(node.left, visited_nodes)
            visited_nodes.append(node.data)
            self.inorder_traversal(node.right, visited_nodes)
        return visited_nodes

A=BinaryTreeNode("A")
B=BinaryTreeNode("B")
C=BinaryTreeNode("C")
D=BinaryTreeNode("D")
E=BinaryTreeNode("E")
F=BinaryTreeNode("F")

A.add_left_child(B)
A.add_right_child(C)
B.add_left_child(D)
B.add_right_child(E)
C.add_left_child(F)

tree=BinaryTree(A)

print(f'Preorder Traversal: {tree.preorder_traversal(tree.root)}')
print(f'Postorder Traversal: {tree.postorder_traversal(tree.root)}')
print(f'Inorder Traversal: {tree.inorder_traversal(tree.root)}')