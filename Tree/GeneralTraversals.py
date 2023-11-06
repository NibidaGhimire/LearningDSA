from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root=None):
        self.root = root
 
    def preorder_traversal(self, node, traversal=[]):
        if node is None:
            return traversal
        
        traversal.append(node.data)
        for child in node.children:
            self.preorder_traversal(child, traversal)
        
        return traversal
        
    def postorder_traversal(self, node, traversal=[]):
        if node is None:
            return traversal
        for child in node.children:  
            self.postorder_traversal(child, traversal)
        traversal.append(node.data)
        return traversal
        
    def breadth_first_traversal(self):
        if not self.root:
            return []

        queue = deque()
        queue.append(self.root)
        
        traversal = [] 

        while queue:
            current_node = queue.popleft()
            traversal.append(current_node.data)  
    
            for child in current_node.children:
                queue.append(child)
    
        return traversal  

A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')
G = TreeNode('G')

A.add_child(B)
A.add_child(C)
A.add_child(D)
B.add_child(E)
B.add_child(F)
E.add_child(G)

general_tree = Tree(A)

print(f'Preorder Traversal: {general_tree.preorder_traversal(general_tree.root)}')
print(f'Postorder Traversal: {general_tree.postorder_traversal(general_tree.root)}')
print(f'Breadth First Traversal: {general_tree.breadth_first_traversal()}')