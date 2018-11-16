class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split("/")
        stack = []
        
        for item in path:
            if item == "":
                pass
            elif item == ".":
                pass
            elif item == "..":
                if stack:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(item)
        return "/" + "/".join(stack)