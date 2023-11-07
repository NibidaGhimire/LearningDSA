
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

def heapify_up(self, index):
    if self.has_parent(index): 
        parent_index = self.parent(index)
        if self.heap[index] < self.heap[self.parent(index)]:
            self.swap(index, parent_index)
            self.heapify_up(parent_index)

def insert(self, value):
    self.heap.append(value)
    # replace with heapify_up() logic
    self.heapify_up(self.size() - 1)
 
def extract_min(self):
    min = self.heap[0]
    if self.size() == 1:    
        self.heap = []
        return min
    self.heap[0] = self.heap[-1] 
    self.heap.pop()  
    self.heapify_down(0)
    return min
