import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return n
        low = 1
        high = n
        while low < high:

            mid = (low+high+1)/2
            if mid*(mid+1)/2.0 <= n: low = mid
            else: high = mid-1
        return low