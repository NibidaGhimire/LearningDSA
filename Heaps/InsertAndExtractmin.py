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

    def insert(self, value):
        self.heap.append(value)
        index=len(self.heap)-1

        while self.has_parent(index) and self.heap[self.parent(index)]>self.heap[index]:
            self.swap(index,self.parent(index))
            index=self.parent(index)

        return self.heap
    
    # Time Complexity : O(logn)


    def extract_min(self):
        min=self.heap[0]

        if self.size()<2:
            self.heap=[]
            return min
        
        self.heap=[self.heap[-1]]+self.heap[1:-1]

        index=0
        while True:
            if not self.has_left_child(index):
                return min

            sIndex= self.left_child(index)
            if self.has_right_child:
                if  self.heap[self.right_child(index)] < self.heap[sIndex]:
                    sIndex=self.right_child(index)

            if self.heap[index]>self.heap[sIndex]:
                self.swap(index,sIndex)

            else:
                break

            index=sIndex
        return min
    
    # Time Complexity : O(logn)

    def peek(self):
        return self.heap[0]
    # Time Complexity : O(1)
      
heap = MinHeap()
array = [1, 2, 5, 3, 4, 6, 7]
for i in array:
    heap.insert(i)
print(f'Root: {heap.peek()}')
print(heap)
print(f'Root: {heap.extract_min()}')
print(f'Root: {heap.peek()}')
print(heap)