__author__ = 'Meghna'

def find_element(A,n):
    r , c = len(A) , len(A[0])
    found = False
    current_r , current_c = 0, c-1
    while current_r != r-1 or current_c !=0:
        if A[current_r][current_c] == n:
            return True
        elif A[current_r][current_c] > n:
            current_c -=1
        else:
            current_r +=1
    if A[current_r][current_c] == n:
            return True
    return found

A = [[1,3,5],[2,4,10],[6,9,15],[7,11,16]]
print(find_element(A,9))