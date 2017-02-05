class Solution(object):
    def reverseWords(self, s):

        if not s: return s

        s = list(' '.join(s.split()))

        start, end = 0, 0
        while start<len(s) and end<len(s) :
            if s[end]!= ' ':
                end +=1
                continue
            self.reverse(s, start, end-1)
            start, end = end+1, end+1

        if start < end: self.reverse(s, start, len(s)-1)

        self.reverse(s, 0, len(s)-1)
        s = ''.join(s)
        return s

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start +=1
            end -=1