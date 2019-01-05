__author__ = 'Meghna'

# BUBBLE SORT
# Runtime :
#       Average : O(n^2)
#       Worst   : O(n^2)
# Memory : O(1)
# push the largest to the last
def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j+1] < A[j]:
                A[j] , A[j+1] = A[j+1] , A[j]

# SELECTION SORT
# Runtime and Memory : Same as above
# find the min idx and put in the beginning
def selection_sort(A):
    for i in range(0,len(A)):
        min = i
        for j in range(i+1,len(A)):
            if A[j] < A[min] :
                min = j
        A[i] , A[min] = A[min] , A[i]

# INSERTION SORT
# Runtime and Memory : Same as above
# start from  1, 2, 3..travel back to 0, keep exchanging if it's min. This puts the min to 0, 1 2,..n-1..... 
def insertion_sort(A):
    for i in range(1,len(A)):
        j=i
        while j>0 and A[j] < A[j-1]:
            A[j] , A[j-1] = A[j-1] , A[j]
            j -= 1

# MERGE SORT
# Runtime : O(nlogn) ; Memory : Depends
def merge_sort(A):
    if len(A)>1:
        mid = int(len(A)/2)
        left = A[0:mid]
        right = A[mid:]
        merge_sort(left)
        merge_sort(right)
        l , r = 0 , 0
        for pos in range(len(A)):
            lvalue = left[l] if l<len(left) else None
            rvalue = right[r] if r<len(right) else None
            if (lvalue and rvalue and lvalue < rvalue) or rvalue is None :
                A[pos] = lvalue
                l +=1
            elif (lvalue and rvalue and rvalue <= lvalue) or lvalue is None :
                A[pos] = rvalue
                r +=1
            else:
                raise Exception("Could not merge subarray sizes do not match main array")

# QUICK SORT
# Runtime :
#       Average : O(nlogn)
#       Worst   : O(n^2)
# Memory : O(logn)

# Simple
def quick_sort_simple(A):
    if len(A) <= 1:
        return A
    else:
        return quick_sort_simple([x for x in A[1:] if x < A[0]]) + [A[0]] + quick_sort_simple([x for x in A[1:] if x >= A[0]])

# Normal
def partition(A, begin, end):
    pointer = begin + 1
    for i in range(begin + 1, end + 1):
        if A[i] < A[begin]:
            A[pointer] , A[i] = A[i] , A[pointer]
            pointer += 1
    pointer -= 1
    A[pointer] , A[begin] =  A[begin] , A[pointer]
    return pointer

def quick_sort(A,begin,end):
    if begin >= end:
        return
    pivot = partition(A,begin,end)
    quick_sort(A,begin,pivot-1)
    quick_sort(A,pivot+1,end)


#HEAP SORT
import heapq
def heap_sort(A):
    heapq.heapify(A)
    A[:] = [heapq.heappop(A) for i in range(len(A))]


A = [1,5,9,3,7,0,34,78,65,21,34,26,43]
heap_sort(A)
print(A)


#Binary Search
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1

    while first<=last:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            return True
        else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
    return False

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
    #
	# def binarySearch(alist, item):
	#     if len(alist) == 0:
	#         return False
	#     else:
	#         midpoint = len(alist)//2
	#         if alist[midpoint]==item:
	#           return True
	#         else:
	#           if item<alist[midpoint]:
	#             return binarySearch(alist[:midpoint],item)
	#           else:
	#             return binarySearch(alist[midpoint+1:],item)





