
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class LinkedList:
    def __init__(self):
        self.head=None

    
    def create_linked_list(self):

        # take input for node data
        data1 = int(input())
        data2 = int(input())
        data3 = int(input())
        data4 = int(input())

    
        node1=Node(data1)
        node2=Node(data2)
        node3=Node(data3)
        node4=Node(data4)
        self.head=node1

    
        node1.next=node2
        node2.next=node3
        node3.next=node4
        node4.next=self.head

    def is_empty(self):
        return  self.head is None
    
    
    def traverse_linked_list(self):

        if self.is_empty():
            print('Empty Linked List')
            return
        current=self.head
        while current.next is not self.head:
            print(current.data,end=" -> ")
            current=current.next
        print(f'{current.data} -> {self.head.data}')

linked_list = LinkedList()


linked_list.create_linked_list()

linked_list.traverse_linked_list()


#Time Complexity = O(n)