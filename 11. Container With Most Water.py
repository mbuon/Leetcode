# Could not understand the logic very intuitively, was hovering around a similar thought of sarting pointers from left and right before looking at the
# solution at https://leetcode.com/problems/container-with-most-water/solution/

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
       
        left = 0
        right = len(height) - 1
        
        jar = min(height[left], height[right]) * (right - left)
        
        while(left < right):
            
            if (right - left == 0):
                return jar
            else:
            
                if (height[left] < height[right]):
                    left += 1

                else:
                    right -= 1

                area = min(height[left], height[right]) * (right - left)
                
                if (area) > jar:
                    jar = area
                
        return jar