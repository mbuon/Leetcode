class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people = sorted(people)
        
        small = 0
        big = len(people) - 1
        
        boats = 0
        
        while (small <= big):
            if people[small] + people[big] > limit:
                big -= 1
            else:
                big -= 1
                small += 1
            boats += 1
        
        return boats