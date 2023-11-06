class TreeNode:
    def __init__(self, data, size=0):
        self.data=data
        self.size=size
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, root=None):
        self.root = root

    def calculate_disk_space(self, node):
        if node is None:
            return
        size=node.size
        for child in node.children:
            size+=self.calculate_disk_space(child)
        
        return size



mydoc=TreeNode("MyDocuments")
mus=TreeNode("Music")
pic=TreeNode("Pictures")
work = TreeNode("Work", 10)  
m1 = TreeNode("M1", 20)  
m2 = TreeNode("M2", 10)  
p1 = TreeNode("P1", 30)  
p2 = TreeNode("P2", 20)  

mydoc.add_child(mus)
mydoc.add_child(pic)
mydoc.add_child(work)
mus.add_child(m1)
mus.add_child(m2)
pic.add_child(p1)
pic.add_child(p2)

tree=Tree(mydoc)

print(tree.calculate_disk_space(tree.root))