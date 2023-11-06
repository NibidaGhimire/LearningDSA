def concatenate(self, list2):
 
    if not self.head:
        self.head = list2.head
        return
        
    current = self.head 
 
    while True:

        if current.next is None:
            break
 
        current = current.next
        
    current.next = list2.head