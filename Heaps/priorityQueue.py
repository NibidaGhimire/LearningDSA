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
    
    def peek(self):
        return self.heap[0]

class PriorityQueue(MinHeap):
    # use methods from MinHeap Class
    def __init__(self):
        super().__init__()
        
    def insert(self, value, priority):
        super().insert((priority,value))

    def extract_min(self):
        return super().extract_min()

    def peek(self):
        return super().peek()

    def change_key(self, value, new_priority):
        for i in range(self.size()):
            if self.heap[i][1]==value:
                old_priority=self.heap[i][0]
                self.heap[i]=(new_priority,value)

                if new_priority<old_priority:
                    self.heapify_up(i)
                else:
                    self.heapify_down(i)
        return self.heap
priority_queue = PriorityQueue()

tasks = [(12, 'Task1'), (15, 'Task2'), (25, 'Task3'), (16, 'Task4'), (5, 'Task5')]
print('Insert tasks into priority queue')
for priority, task in tasks:
    priority_queue.insert(task, priority)
print(priority_queue)
print('--------------')


print('Change priority of task1 to 20')
priority_queue.change_key('Task1', 20)
print(priority_queue)
print('--------------')

print('Change priority of task1 to 2')
priority_queue.change_key('Task1', 2)
print(priority_queue)
print('--------------')

print('Top priority task')
print(priority_queue.peek()) 
print('-----------')

priority_queue.extract_min()
print('After removing top priority task')
print(priority_queue)