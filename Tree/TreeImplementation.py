# a class to create and add nodes
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        print(f'Node {self.data} was created')
 
    def add_child(self, child):
        self.children.append(child)
        print(f'Node {child.data} was added as child to Node {self.data}')
 
# a class to create tree and perform tree operations
class Tree:
    def __init__(self, root=None):
        self.root = root
        print("A tree was created")
 
root = TreeNode("Book")
 
child1 = TreeNode(1)
child2 = TreeNode(2)
child3 = TreeNode(3)
 
child1_1 = TreeNode(1.1)
child1_2 = TreeNode(1.2)
child1_3 = TreeNode(1.3)
child1_4 = TreeNode(1.4)
child2_1 = TreeNode(2.1)
child3_1 = TreeNode(3.1)
child3_2 = TreeNode(3.2)
child3_3 = TreeNode(3.3)
 

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
 
child1.add_child(child1_1)
child1.add_child(child1_2)
child1.add_child(child1_3)
child1.add_child(child1_4)
 
child2.add_child(child2_1)
 
child3.add_child(child3_1)
child3.add_child(child3_2)
child3.add_child(child3_3)
 
general_tree = Tree(root)