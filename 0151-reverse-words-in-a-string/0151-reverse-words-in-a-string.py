class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        word_list = s.split()
        word_list.reverse()

        result = ''
        for word in word_list:
            result += word
            result += ' '

        result = result.rstrip()
        return result