class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """


        if not nums:
            return []

        window = []
        result=[]

        for i in range(len(nums)):

            if window and window[0] <= i - k:
                window.pop(0)

            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.append(i)

            if window and window[-1] >= k-1:
                result.append(nums[window[0]])

        return result
