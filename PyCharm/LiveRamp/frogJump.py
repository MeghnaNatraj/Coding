# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, X, D):
    # write your code in Python 2.7
    pass
    if D>=X or not A:
        return 0
    elif A[0] <= D and A[0]+D >= X:
            return 0
    else:
        max_to_go =  X-D
        positions = [False]*X
        current = 0
        for idx,leaf_drop in enumerate(A):
            positions[leaf_drop] = True
            if leaf_drop - current <= D and leaf_drop - current > 0:
                current = leaf_drop
                counter = 1
                while counter!=D and current+counter < X :
                    if positions[current+counter] == False:
                        counter+=1
                    else:
                        current += counter
                        counter = 1
                if current >= max_to_go:
                    return idx
        return -1