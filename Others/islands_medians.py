def ifValid(r, c, max_r, max_c):
    if r>=0 and c>=0 and r<=max_r-1 and c<=max_c-1:
        return True
    return False

def checkAround(island, r, c, max_r, max_c, visited):
    count = 1
    visited[r][c] = 1
    neighbors = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    for (nr, nc) in neighbors:
        new_r = r + nr
        new_c = c + nc
        if ifValid(new_r, new_c, max_r, max_c) and island[new_r][new_c] and not visited[new_r][new_c] :
            count+= checkAround(island, new_r, new_c, max_r, max_c, visited)
    return count


def medianIslands(island):
    count_islands = []
    max_r = len(island)
    max_c = len(island[0])
    visited = [[False for c in range(max_c)] for r in range(max_r)]
    for r in range(max_r):
        for c in range(max_c):
            if island[r][c] and not visited[r][c]:
                count_islands.append(checkAround(island, r, c, max_r, max_c, visited))
    return count_islands

if __name__ == "__main__":
    a = [[1, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [1, 0, 0, 0]]
    for i in a:
        print i
    print
    print medianIslands(a)

