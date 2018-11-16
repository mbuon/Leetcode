class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = [-1] * 1000000

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.storage[key] = 1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.storage[key] = -1

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if self.storage[key] == -1:
            return False
        else:
            return True
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)