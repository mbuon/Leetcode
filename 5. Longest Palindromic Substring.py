class Solution:

	def extend(self, s, i, j):
		extending = True
		indices = [i, j]

		while (extending):

			if ((indices[0] > 0) and (indices[1] < len(s) - 1)):
				if (s[indices[0] - 1] == s[indices[1] + 1]):
					indices = [indices[0] - 1, indices[1] + 1]
				else:
					extending = False
			else:
				extending = False

		return s[indices[0]:indices[1] + 1]

	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str

		The key is to send each character position and try to expand it in both directions as much as possible.
		Also send two characters at a time if they ate same because palindrome could be odd or even number of characters.

		Based on this: https://leetcode.com/problems/longest-palindromic-substring/discuss/2928/Very-simple-clean-java-solution
		"""

		if (len(s) < 2):
			return s

		palindromes = {}

		for i in range(0, len(s) - 1):

			string_uni = self.extend(s, i, i)
			string_bi = ""

			if (s[i] == s[i+1]):
				string_bi = self.extend(s, i, i + 1)

			palindromes[len(string_uni)] = string_uni
			palindromes[len(string_bi)] = string_bi

		return palindromes[max(palindromes)]

print(Solution().longestPalindrome("gg"))