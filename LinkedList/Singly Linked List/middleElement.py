#Replace ___ with your code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # method to append nodes
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next
        current.next = new_node

    # method to return the middle element 
    def find_middle_element(self):
        slow=self.head
        fast=self.head

        while fast.next:
            slow=slow.next
            fast=fast.next
            if fast.next:
                fast=fast.next
        
        return slow.data


linked_list = LinkedList()


data_list = list(map(int, input().split()))

for node in data_list:
    linked_list.append(node)

middle = linked_list.find_middle_element()
print(middle)