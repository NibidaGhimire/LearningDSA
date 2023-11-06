# method to check if a linked list is sorted 
def is_sorted(self):

    if not self.head:
        return True
    current = self.head
        
    while current.next:
        if current.data > current.next.data:
            return False
        current = current.next
    return True