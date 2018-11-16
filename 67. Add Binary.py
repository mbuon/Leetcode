class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        answer = []
        
        while (i >= 0) and (j >= 0):
            if (int(a[i]) + int(b[j]) + carry == 3):
                carry = 1
                answer.append(1)
            
            elif (int(a[i]) + int(b[j]) + carry == 2):
                carry = 1
                answer.append(0)
            
            else:
                answer.append(int(a[i]) + int(b[j]) + carry)
                carry = 0
                
            i -= 1
            j -= 1
            
        while (i >= 0):
            if (int(a[i]) + carry == 2):
                answer.append(0)
                carry = 1
                    
            else:
                answer.append(int(a[i]) + carry)
                carry = 0
            
            i -= 1
                
        while (j >= 0):
            if (int(b[j]) + carry == 2):
                answer.append(0)
                carry = 1
            
            else:
                answer.append(int(b[j]) + carry)
                carry = 0
                
            j -= 1
                
        if (carry == 1):
            answer.append(carry)
                           
        return "".join([str(i) for i in reversed(answer)])
                
                