class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        input_string = s.lower()
        forward_string = ''

        for i in input_string:
            if i.isalnum():
                forward_string += i

        backward_string = forward_string[::-1]

        if forward_string == backward_string:
            return True
        else:
            return False