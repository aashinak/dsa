# Hash Table Implementation
# A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values.
# A hash table uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
# The worst-case time complexity for search, insert, and delete operations is O(n), but the average time complexity is O(1).
# Hash tables are used to implement associative arrays, database indexing, caches, and sets.
# Hash tables are a very efficient way to store and retrieve data. They are used in many applications, including databases, caches, and sets.

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]): # enumerate gives index and value
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if len(element) == 2 and element[0] == key:
                return element[1]
        return "Not found"
        
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                return
    
ht = HashTable()

ht["abc"] = 130
ht["cab"] = 20
# # del ht["cab"]
print(ht["abc"])
del ht["abc"]
print(ht["abc"])





