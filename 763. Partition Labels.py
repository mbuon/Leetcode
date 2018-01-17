# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

# https://leetcode.com/problems/partition-labels/description/

S = "qiejxqfnqceocmy"

def minimizer(S):
   
    node = []
    
    for index, value in enumerate(S):
        if (value == S[0]):
        	node.append(index)

    min_length = max(node) + 1
    
    i = 0

    while (i < min_length):
    
    	current = S[i]
        node = []

        for index, value in enumerate(S):
            if (value == current):
                node.append(index)

        if (max(node) >= min_length):
        	min_length = max(node) + 1

        i += 1
        
    return min_length

node = []

while (len(S) != 0):
	length = minimizer(S)
	node.append(length)
	S = S[length:]

print node