class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        # Method 1 : New Array Copy : Time and Space O(n)
        # nums[:] = nums[-k:]+nums[:-k]

        # Method 2 : Like Bubble Sort : Time O(n*k) , Space O(1)
        # for i in range(k):
        #     for j in range(len(nums)-1, 0, -1):
        #         nums[j-1], nums[j] = nums[j], nums[j-1]

        # Method 3 : Like Reverse a sentence
        n = len(nums)
        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-1)

    def reverse(self, nums, start, end):
        for i in range((end-start)/2+1):
            nums[start+i], nums[end-i] = nums[end-i], nums[start+i]



        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
