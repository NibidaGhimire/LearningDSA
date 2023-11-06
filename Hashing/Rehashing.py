class ModulusHashing:
    
    def __init__(self):
        self.table = [None] * 10
 
    def find_load_factor(self):
        occupied_slots = sum(1 for slot in self.table if slot is not None)
        return occupied_slots / len(self.table)
 
    def H(self, key):
        return key % 10
 
    def insert(self, data):
        hash_value = self.H(data)
        self.table[hash_value] = data
        if self.find_load_factor() > 0.5:
            self.rehash()
    
    def rehash(self):
        new_size = 2 * len(self.table)
        new_table = [None] * new_size
 
        for data in self.table:
            if(data is not None):
                hash_value = data % new_size
                new_table[hash_value] = data
 
        self.table = new_table
 
    def retrieve(self, key):
        hash_value = self.H(key)
        if hash_value < len(self.table):
            return self.table[hash_value]
        else:
            return None
 
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f'{hash_value}:{key}')
            
elements = [1, 3, 5, 4, 7, 2, 9, 20]
hash_table = ModulusHashing()
for element in elements:
    hash_table.insert(element)
 
hash_table.display()