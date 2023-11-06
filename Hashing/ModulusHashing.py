class ModulusHashing:
    # creation
    def __init__(self):
        self.table = [None] * 10
 
    def H(self, key):
        return key % 10
 
    # insert
    def insert(self, data):
        hash_value = self.H(data)
        self.table[hash_value] = data
 
    # retrieve
    def retrieve(self, key):
        hash_value = self.H(key)
        if hash_value < len(self.table):
            return self.table[hash_value]
        else:
            return None
    #Time Complexiry : O(n)


    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f'{hash_value}:{key}')
            
elements = [1, 3, 5, 4, 7, 2, 9, 20]
hash_table = ModulusHashing()
for element in elements:
    hash_table.insert(element)
 
hash_table.display()