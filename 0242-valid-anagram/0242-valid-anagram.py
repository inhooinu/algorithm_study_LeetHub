class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        t = list(t)
        for letter in s:
            if letter in t:
                t.pop(t.index(letter))
            else:
                return False
        
        if len(t) == 0:
            return True
        else:
            return False