class ChainingHashTable:
 
    def __init__(self, size=12):
        self.size = size
        self.table = [None] * self.size
 
    def H(self, key):
        return key % self.size
 
    def insert(self, value):
        key = self.H(value)
        if self.table[key] is None:
            self.table[key] = [value]
        else:
            self.table[key].append(value)
            self.table[key] = sorted(self.table[key])
 
    def display(self):
        for key, value_list in enumerate(self.table):
            print(f'Index {key}: {value_list}')
 
    def retrieve(self, value):
        key = self.H(value)
        value_list = self.table[key]
        if value_list is not None:
            for val in value_list:
                if val == value:
                    return val
        return None
    #Time Complexity : O(LF)   
    #Successful retrieval time = 1+LF/2
    #Falied retrieval time = 1+LF

    

elements = [12, 14, 2, 6, 9, 35]
hash_table = ChainingHashTable()
for element in elements:
    hash_table.insert(element)
 
hash_table.display()
print(f'\nRetrieved Value: {hash_table.retrieve(14)}')
