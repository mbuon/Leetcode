class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        root = x
        last = x
        
        while not (((root * root) <= x) and (((root + 1) * (root + 1)) > x)):
                        
            if ((root * root) > x):
                last = root
                root = int(root / 2)
            else:
                root = int((root + last) / 2)
            
        return root