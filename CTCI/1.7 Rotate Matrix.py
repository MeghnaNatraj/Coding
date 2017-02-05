# [ first,f     ->      f,last ]
#
#
# [ l,first     <-    last,l ]
#
# Fixed - first or last
# Changing - f or l

def rotate(A):
    length = len(A)
    for first in range(length/2):
        last = length-1-first
        for f in range(first,last):
            l = length-1-f

            temp = A[first][f]
            A[first][f] = A[l][first]
            A[l][first] = A[last][l]
            A[last][l] = A[f][last]
            A[f][last] = temp

    return A

if __name__ == "__main__":
    A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    for i in A:
        print i
    print
    for i in rotate(A):
        print i
