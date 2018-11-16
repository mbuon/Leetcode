class Solution:

	def combine(self, piece, digits):

		letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

		result = []

		if (len(digits) == 0):
			return []

		elif (len(digits) == 1):
			for letter in letters[digits]:
				result.append(piece + letter)
		else:
			for letter in letters[digits[0]]:
				result.extend(self.combine(piece + letter, digits[1:]))

		return result

	def letterCombinations(self, digits):
		output = self.combine("", digits)
		return output

print(Solution().letterCombinations("2354"))