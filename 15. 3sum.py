# Based on the beautiful solution at https://leetcode.com/problems/3sum/discuss/7402/Share-my-AC-C++-solution-around-50ms-O(N*N)-with-explanation-and-comments
# TODO:
# 	1) Do Two Sum with the same approach
# Done - Worse performance because we need indices, not values

# Concept:
# -6,-5,-4,-1,2,3,5,7,8,11

# -5, 11
# THe key is that pairs are inside the left and right


from datetime import datetime
startTime = datetime.now()

class Solution:      
    def threeSum(self, S):
        S = sorted(S)
        output = set()
        location = {}
        for i in range(0, len(S)):
        	for j in range(0, len(S)):
        		if i > j:
	        		if - S[i] - S[j] in location:
	        			k = location[- S[i] - S[j]]
	        			if (k != i) and (k != j):
        					output.add(tuple(sorted([S[i], S[j], S[k]])))
	        		else:
	        			location[S[j]] = j
	        			
        return [list(triple) for triple in output]

	def threeSumEfficient(self, S):
			"""
			:type nums: List[int]
			:rtype: List[List[int]]
			"""

			S = sorted(S)
			output = []

			for i in range (0, len(S)):

				if ((i > 0) and (S[i] == S[i-1])):
					continue

				if (S[i] > 0):
					break

				target = -S[i]
				left = i + 1
				right = len(S) - 1

				while (left < right):
					total = S[left] + S[right]

					if (total < target):
						left += 1

					elif (total > target):
						right -= 1

					else:
						triplet = [S[i], S[left], S[right]]
						output.append(triplet)
						
						while((S[left] == triplet[1]) and (left < right)):
							left += 1
						while((S[right] == triplet[2]) and (left < right)):
							right -= 1

			return output

print(Solution().threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
print(datetime.now() - startTime)