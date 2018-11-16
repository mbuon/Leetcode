class Solution:
    def findLongestChain(self, pairs_unsorted):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        
        if len(pairs_unsorted) <= 1:
            return len(pairs_unsorted)
        
        counter = 1       
        pairs = sorted(pairs_unsorted, key=lambda x:x[1])
        current = pairs[0]
        
        for i in range(1, len(pairs)):
            if current[1] < pairs[i][0]:
                counter += 1
                current = pairs[i]
                
        return counter
        

'''

Intuition

Imagine the pairs to be ladders which take you from bottom to up. So ladder [3,5] takes you from level 3 to 5.
You want to stay as close to the ground as possible. So, if you have an option of [3,4] and [3,5], you wanna grap [3,4]
This keeps the opportunity open to grab the next ladder closest to the ground, thus maxizing the number of ladders you can take before reaching the top.

Algorithm

Arrange the ladders left to right, with the increasing level they take you to. Keep climbing up and up and counting the ladders on yuor way up.


						-
						-
					-	-
			-	-	-	
	-	-	-	-	-	
-	-	-	-			
-	-	-	-
-	-	-
	-

'''