# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        end = None
        head = None

        for idx, list in enumerate(lists):
            if list:
                heapq.heappush(h,(list.val,idx))
        while h:
            min_value, list_number = heapq.heappop(h)

            if not head:
                head = end = lists[list_number]
            else:
                end.next = lists[list_number]
                end = end.next

            lists[list_number] = lists[list_number].next
            end.next = None

            if lists[list_number]:
                heapq.heappush(h,(lists[list_number].val,list_number))

        return head


