#HEAPIFY_DOWN
def heapify(self, array):
    self.heap = array
    for i in range(len(self.heap) - 1, -1, -1):
        self.heapify_down(i)
 
def heapify_down(self, index):
    if not self.has_left_child(index):
        return
    smaller_child_index = self.left_child(index)
    if self.has_right_child(index) and self.heap[self.right_child(index)] < self.heap[smaller_child_index]:
        smaller_child_index = self.right_child(index)
    if self.heap[index] <= self.heap[smaller_child_index]:
        return
    self.swap(index, smaller_child_index)
    self.heapify_down(smaller_child_index)


    # Time Complexity : O(logn)


#HEAPIFY_UP

def heapify(self, array):
    self.heap = array
    for i in range(len(self.heap) - 1, -1, -1):
        self.heapify_up(i)
 
def heapify_up(self, index):
    if self.has_parent(index): 
        parent_index = self.parent(index)
        if self.heap[index] < self.heap[self.parent(index)]:
            self.swap(index, parent_index)
            self.heapify_up(parent_index)
