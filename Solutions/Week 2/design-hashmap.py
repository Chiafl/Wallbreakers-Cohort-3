# Using list
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = [-1 for x in range(1000000)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hash[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.hash[key]==-1:
            return -1
        return self.hash[key]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if self.hash[key] != -1:
            self.hash[key] = -1
        
# Using dictionary (trivial)
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hash[key] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key not in self.hash.keys():
            return -1
        return self.hash[key]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hash:
            del self.hash[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)