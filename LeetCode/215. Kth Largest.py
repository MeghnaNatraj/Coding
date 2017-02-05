class Solution(object):

    def findKthLargest(self, nums, k):

       pivot = self.findPivot(nums)
       if k == pivot+1 :
           return nums[pivot]
       elif k > pivot+1:
           return self.findKthLargest(nums[pivot+1:], k-(pivot+1))
       else:
           return self.findKthLargest(nums[:pivot], k)

    def findPivot(self,nums):
        pivot = 0
        pivotValue = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > pivotValue:
                pivot +=1
                nums[i], nums[pivot] = nums[pivot], nums[i]
        nums[0], nums[pivot] = nums[pivot], nums[0]
        return pivot