class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits) - 1
        carry = 1
        
        while (n >= 0):
            added = digits[n] + carry
            digits[n] = added % 10
            carry = int((added - digits[n])/10)
            
            if (carry == 0):
                break
            
            n -= 1
            print(digits, carry)
            
        if (carry > 0):
            answer = [1]
            answer.extend(digits)
            return answer
        else:
            return digits
            