# Android Unlock Patterns
count = 0
visited = [False]*9
not_reachable = {'02':1,'06':3,'08':4,'17':4,'26':4,'28':5,'35':4,'68':7}
def android_lock(current_position):
    global count
    global visted
    visited[current_position] = True
    for new_position in range(0,9):
        if not visited[new_position] and valid_move(current_position,new_position):
            android_lock(new_position)
    if sum(visited) >= 4  : count += 1
    visited[current_position] = False  

def valid_move(a,b):
    global not_reachable
    index = str(min(a,b))+str(max(a,b))
    if index in not_reachable and not visited[not_reachable[index]]:
        return False
    else:
        return True

for start_position in range(0,9):
    android_lock(start_position)
print(count)