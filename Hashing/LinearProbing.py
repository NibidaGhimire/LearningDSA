class LinearProbingHashTable:
 
    def __init__(self, size=12):
        self.size = size
        self.table = [None] * self.size
 
    def H(self, value, i):
        return (value + i) % self.size
 
    def insert(self, value):
        i = 0
        key = self.H(value, i)
        while self.table[key] is not None:
            i += 1
            key = self.H(value, i)
        self.table[key] = value
 
    def retrieve(self, value):
        i = 0
        key = self.H(value, i)
        while self.table[key] is not None:
            if self.table[key] == value:
                return value
            i += 1
            key = self.H(value, i)
        return None
    #Time Complexity : O(1) to O(n)

    def display(self):
        for key, value in enumerate(self.table):
            print(f'Index {key}: {value}')
 
elements = [12, 14, 2, 6, 9, 35]
hash_table = LinearProbingHashTable()
for element in elements:
    hash_table.insert(element)
hash_table.display()
print(f'Retrieved Value: {hash_table.retrieve(2)}')
