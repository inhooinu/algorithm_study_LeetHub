class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v = []
        c = []
        result = ''

        for alphabet in s:
            if alphabet in vowels:
                v.append(alphabet)
                c.append('')
            else:
                c.append(alphabet)

        for i in c:
            if i == '':
                result += v.pop()
            else:
                result += i
        
        return result