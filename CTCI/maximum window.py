__author__ = 'Meghna'


# IMPLEMENTATION 1 - Brute Force
# returns the maximum difference between 2 elements a-b such that b lies before a
# def maximum_window(alist):
#     max = 0
#     for i in range(0,len(alist)):
#         for j in range(i+1,len(alist)):
#             difference = alist[j] - alist[i]
#             if  difference > max:
#                 max = difference
#     return max


# alist = [10,3,7,2,4,5,8,20,1]
# print(maximum_window(alist))

# Space - O(1)
# Time - O(n^2)

# # IMPLEMENTATION 2
# def maximum_window(alist):
#     len_alist = len(alist)
#     if len(alist) == 0 :
#         return None
#     min_element = alist[0]
#     difference = 0

#     for i in range(1,len_alist):
#         if alist[i] < min_element:
#             min_element = alist[i]
#         if alist[i] - min_element > difference:
#             difference = alist[i] - min_element
#     return difference

# alist = [1,10,7,2,0,5,8,20,1]
# print(maximum_window(alist))

# # Space - O(1)
# # Time - O(n)


