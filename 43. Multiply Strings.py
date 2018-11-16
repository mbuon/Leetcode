# The following executions of the exact same file result into different results (Python3 vs Python2)

# python3 43.\ Multiply\ Strings.py 
# python 43.\ Multiply\ Strings.py 
import Datetime


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        result = 0
        place = 1

        for j in reversed(num2):
        	carry = 0
        	local_place = 1 * place
        	for i in reversed(num1):

        		prod = int(i) * int(j) + carry
        		ones = prod % 10
        		result += ones * local_place
        		carry = (prod - ones) / 10
        		local_place *= 10

        	result += local_place * carry
        	place *= 10

        return str(int(result))

num2 = "123456789"
num1 = "987654321"

# print ("Expected: " + str(int(num1) * int(num2)))
# print("Output:   " + str(Solution().multiply(num1, num2)))