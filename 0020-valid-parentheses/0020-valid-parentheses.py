class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        for bracket in s:
            if bracket == '(':
                stack.append(bracket)
                print(stack)
            elif bracket == '{':
                stack.append(bracket)
            elif bracket == '[':
                stack.append(bracket)
            elif bracket == ')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            elif bracket == '}':
                if stack and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            elif bracket == ']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            
        if stack:
            return False
        else:
            return True