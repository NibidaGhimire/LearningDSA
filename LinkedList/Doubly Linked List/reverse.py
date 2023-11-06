def reverse(self):
        if self.node_count()<2:
            return

        current=self.head

        while current:
            current.prev , current.next= current.next, current.prev

            current=current.prev
        self.head,self.tail=self.tail,self.head

        