class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_bit = 0
        t_bit = 0

        a = ord('a')

        for c in s:
            position = ord(c) - a
            s_bit ^= 1 << position

        for c in t:

            position = ord(c) - a
            t_bit ^= 1 << position

        missing_bit = s_bit ^ t_bit

        count = -1
        while missing_bit:
              missing_bit =  missing_bit >> 1
              count +=1

        return chr(ord('a')+count)








