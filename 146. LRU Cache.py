class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.index = {}
        self.cold = ListNode(None, None)
        self.hot = ListNode(None, None)
        self.cold.next = self.hot
        self.hot.prev = self.cold

    def remove(self, key):
        node = self.index[key]
        _prev = node.prev
        _next = node.next
        _prev.next = _next
        _next.prev = _prev
        del node
        self.index.pop(key, None)
        
    def insert(self, key, value):
        node = ListNode(key, value)
        _prev = self.hot.prev
        _prev.next = node
        node.next = self.hot
        self.hot.prev = node
        node.prev = _prev
        self.index[key] = node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.index:
            return -1
        else:
            value = self.index[key].val
            self.remove(key)
            self.insert(key, value)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.index:
            self.remove(key)
        elif len(self.index) == self.capacity:
            self.remove(self.cold.next.key)
        self.insert(key, value)