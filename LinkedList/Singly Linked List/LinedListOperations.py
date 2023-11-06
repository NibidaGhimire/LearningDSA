class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # create the linked list: 90->80->60->50
    def create_linked_list(self):
        node1 = Node(90)
        node2 = Node(80)
        node3 = Node(60)
        node4 = Node(50)

        self.head = node1
        node1.next = node2
        node2.next = node3
        node3.next = node4

    # display linked list in format: A->B->C
    def display(self):
        current = self.head
        while current:
            print(f"{current.data}", end="->")
            current = current.next
        print(None)

    def count_elements(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
#------
    #Append at last
    def append(self, data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return

        current=self.head
        while current.next:
            current=current.next

        current.next=newNode
        return
    #Time complexity : O(1)

#-----
    #Insert at beginning
    def insert_nodeatbeg(self, data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        return
#-----
    # insert node to linked list in given position
    def insert_node(self, data, position):
        if position < 1 or position > self.count_elements():
            print("Position Invalid")
            return
        newNode=Node(data)
        current=self.head

        if position == 1:
            newNode.next = self.head
            self.head = newNode
            return
        
        for i in range(1,position-1):
            current=current.next
        newNode.next=current.next
        current.next=newNode
        return
    #Time Complexity : O(n)
#-----
    # method to delete the first node
    def delete_firnode(self):
        if self.head:
            self.head=self.head.next
            return
    #Time COmplexity : O(n)
#-----

    #Delete node at givenposition
    def delete_node(self, position):
        if position < 1 or position > self.count_elements():
            print("Position Invalid")
            return
        

        if self.head is None:
            return
  
        if position == 1:
            self.head = self.head.next
            return
 
        current = self.head
 
        for i in range(1, position - 1):
 
            current = current.next  

        current.next=current.next.next
        return      
    #Time Complexity : O(n)
#-----


linked_list = LinkedList()
# create the initial linked list
linked_list.create_linked_list()
#-----

# input for data to append
data = int(input())
linked_list.append(data)
#------

linked_list.insert_nodeatbeg(data)
# -----

# position of the new node
position = int(input())
# the data value of the new node
data = int(input())
linked_list.insert_node(data, position)

#-----

linked_list.delete_firnode()
#-----

linked_list.delete_node(position)
#-----
# print the updated linked list
linked_list.display()