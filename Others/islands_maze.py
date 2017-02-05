__author__ = 'Meghna'

maze_list = [[1,0,0,0,0,0],[1,1,1,1,1,0],[0,1,0,0,0,0],[0,1,0,0,0,0],[1,1,1,0,1,1],[0,0,1,1,1,0]]
main_nodes = [[0,0],[4,5]]

# get_node – returns the value of a node in the maze if it is a valid move, else returns None
def get_node(row,column):
    global maze_list
    max_row , max_column = len(maze_list) , len(maze_list[0])
    if row < 0 or column < 0  or row >= max_row or column >= max_column :
	    return None
    elif maze_list[row][column] == 0 :
	    return None
    else:
	    return maze_list[row][column]


def maze(path = []):
    global maze_list
    global main_nodes
    current = path[-1]
    if current == main_nodes[1]:
        print("Found the path : "+str(path))
        return True
    neighbors = [[-1,0],[0,-1],[0,1],[1,0]]
    for item in range(len(neighbors)):
        new_row = current[0] + neighbors[item][0]
        new_column = current[1] + neighbors[item][1]
        if [new_row,new_column] not in path and get_node(new_row,new_column) == 1:
                path.append([new_row,new_column])
                if(maze([item for item in path])): return True
                path.pop()
    return False

for item in maze_list:
    print(item)
print()
if not maze([main_nodes[0]]) : print("Path not found")



