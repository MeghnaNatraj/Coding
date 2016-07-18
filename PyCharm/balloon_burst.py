__author__ = 'Meghna'

class Solution(object):
    def maxCoins(self, nums):
        if not nums:
            return 0
        total_max, max, index = 0, 0, 0
        for t in range(len(nums)):
            for i in range(len(nums) - 3):
                prod = nums[i]*nums[i+1]*nums[i+2]
                if prod > max:
                    max = prod
                    index = i+1
            if index!= 0:
                del nums[index]
            total_max += max
            max, index = 0, 0
        if len(nums) == 3 :
            total_max += nums[0]*nums[1]*nums[2]
            del nums[1]
        if len(nums) == 2 :
            total_max += nums[0]*nums[1]
            if nums[0]>nums[1]:
                val = nums[1]

            else:
                val = nums[0]
            del nums[nums.index(val)]
        if len(nums) == 1:
            total_max += nums[0]
        return total_max

sol = Solution()
print sol.maxCoins([3,1,5,8])
