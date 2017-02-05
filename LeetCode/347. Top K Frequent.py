class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Create a dictionary of frequency counts
        d = {}
        for item in nums:
            if item in d:
                d[item]+=1
            else:
                d[item]=0
        size_d = len(d)

        # Step 2: Add elements to a Max heap
        h = []
        for key,value in d.iteritems():
            heapq.heappush(h,(value,key))

        # Step 3: Pop out size_d - k elements
        for i in range(size_d - k):
            heapq.heappop(h)

        # Step 4: Pop the top K frequent elements
        topK = []
        for i in range(k):
            topK.append(heapq.heappop(h)[1])

        return topK[::-1]








