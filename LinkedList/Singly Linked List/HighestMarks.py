# method to return the largest number 
def find_largest(self):
 
    if not self.head:
        return None
    current = self.head
  
    largest = current.data

    while current:

        if current.data > largest:
            largest = current.data
        current = current.next
    return largest