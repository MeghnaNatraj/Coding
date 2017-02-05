class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            else:
                d[s[i]] = t[i]

        d = {}
        for i in range(len(s)):
            if t[i] in d:
                if d[t[i]] != s[i]:
                    return False
            else:
                d[t[i]] = s[i]

        return True

        