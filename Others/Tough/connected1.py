max_size = 0
array = [[1,0,0,0,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]
max_row , max_col = len(array) , len(array[0])
visited = [[0 for i in range(max_col)] for j in range(max_row)]

def array_value(A,row,column):
    global max_row
    global max_col
    if row<0 or column<0 or row>=max_row or column>=max_col:
        return 0
    else:
        return A[row][column]

def find_max_size(A,row,column,current_size):
    global max_size
    current_size += 1
    if(current_size>max_size):
        max_size = current_size
    visited[row][column] = 1
    adjacent = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for i in range(len(adjacent)):
        new_row = row  + adjacent[i][0]
        new_column = column + adjacent[i][1]
        if array_value(A,new_row,new_column) == 1 and visited[new_row][new_column] == 0:
            find_max_size(A,new_row,new_column,current_size)
    visited[row][column] = 0

def traverse(A):
    global max_size
    global max_row
    global max_col
    for row in range(max_row):
        for column in range(max_col):
            if(A[row][column]==1):
                find_max_size(A,row,column,0)
    return max_size

print(traverse(array))