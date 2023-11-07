# Replace ___ with your code

class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self):
            return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return str(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.parent(index) >= 0

    def has_left_child(self, index):
        return self.left_child(index) < len(self.heap)

    def has_right_child(self, index):
        return self.right_child(index) < len(self.heap)
       
    def heapify(self, array):
        self.heap = array
        for i in range(len(self.heap) - 1, -1, -1):
            if  self.has_left_child(i):
                self.heapify_down(i)
        
    def heapify_down(self, index):
        if not self.has_left_child(index):
            return
        smaller_child_index = self.left_child(index)
        if self.has_right_child(index): 
            if self.heap[self.right_child(index)] < self.heap[smaller_child_index]:
                smaller_child_index = self.right_child(index)
        if self.heap[index] > self.heap[smaller_child_index]:
            self.swap(index, smaller_child_index)
        if self.has_left_child(smaller_child_index):
            self.heapify_down(smaller_child_index)
    
    def heapify_up(self, index):
        if self.has_parent(index): 
            parent_index = self.parent(index)
            # compare the value to its parent and swap if necessary
            if self.heap[index] < self.heap[self.parent(index)]:
                parent_index = self.parent(index)
                self.swap(index, parent_index)
                # run the code for parent                 
                if self.has_parent(parent_index):
                    self.heapify_up(parent_index)

    def insert(self, value):
        self.heap.append(value)
        index=self.size()-1

        self.heapify_up(index)
        return self.heap

    def extract_min(self):
        min=self.heap[0]
        if self.size()<2:
            self.heap=[]
            return min

        self.heap[0]=self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return min
    
    def peek(self):
        return self.heap[0]

def heap_sort(lst):
    sortedd=[]

    heap =MinHeap()
    for val in lst:
        heap.insert(val)
    for val in range(heap.size()):
        sortedd.append(heap.extract_min())

    return sortedd

lst = list(map(int, input().split()))
print(heap_sort(lst))