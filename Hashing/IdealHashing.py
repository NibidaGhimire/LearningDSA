class IdealHashing:
    # creation
    def __init__(self):
        self.table = [None] * 10
 
    def H(self, key):
        return key
 
    def insert(self, data):
        # hash value
        hash_value = self.H(data)
        # insert to table
        self.table[hash_value] = data
 
    def retrieve(self, key):
        hash_value = self.H(key)
        # return value if in table
        if hash_value < len(self.table):
            return self.table[hash_value]
        # else return None
        else:
            return None
    #Time Complexity : O(n)

    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f'{hash_value}:{key}')
            
elements = [1, 3, 5, 4, 7, 2, 9]
hash_table = IdealHashing()
for element in elements:
    hash_table.insert(element)
 
hash_table.display()
 
keys_to_retrieve = [2, 6, 9]
for key in keys_to_retrieve:
    print(f"Retrieved value for key {key}: {hash_table.retrieve(key)}")
