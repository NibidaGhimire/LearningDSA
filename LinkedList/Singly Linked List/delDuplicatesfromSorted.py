# delete duplicate nodes from sorted list
def remove_duplicates(self):
    if not self.head:
        return
    current = self.head 

    while current.next:
       
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next 