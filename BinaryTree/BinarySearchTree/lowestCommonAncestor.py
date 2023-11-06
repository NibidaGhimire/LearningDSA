
# Replace ___ with your code

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value, current_node=None):
        if current_node is None:
            if self.root is None:
                self.root = BinarySearchTreeNode(value)
                return
            else:
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
    
    def search(self, value, current_node=None):
        if current_node is None:
            current_node = self.root

        if current_node is None:
            return None

        if value == current_node.data:
            return current_node
        elif value < current_node.data:
            return self.search(value, current_node.left) if current_node.left else None
        else:
            return self.search(value, current_node.right) if current_node.right else None
            
    def find_LCA(self, current_node, p, q):
        if not current_node:
            return None

        if p.data < current_node.data and q.data < current_node.data:
            return self.find_LCA(current_node.left,p,q)

        elif p.data > current_node.data and q.data > current_node.data:
            return self.find_LCA(current_node.right,p,q)

        else:
            return current_node
        
bst = BinarySearchTree()

values_input = input()
values_to_insert = list(map(int, values_input.split()))

for value in values_to_insert:
    bst.insert(value)

value1 = int(input())
value2 = int(input())
node1 = bst.search(value1)
node2 = bst.search(value2)

if node1 and node2: 
    lca = bst.find_LCA(bst.root,node1, node2)
    print(lca.data)