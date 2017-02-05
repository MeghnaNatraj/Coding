from collections import deque
graph_tasks = {"wash laundry": ["dry laundry"],
               "wash the dishes": ["have lunch"],
               "cook food": ["have lunch"],
               "have lunch": [],
               "dry laundry": ["fold laundry"],
               "fold laundry": []}

# Topological sort can be done by:
# 1. Kahn's Algorithm
# 2. Modified DFS

# 1. Kahn's Algorithm : repeatedly remove nodes that have zero in-degree
def kahn_s (graph):

    # Find in-degree
    in_degree = {}
    for u, v in graph.iteritems():
        if u not in in_degree:
            in_degree[u] = 0
        for child in v:
            if child not in in_degree:
                in_degree[child] = 1
            else:
                in_degree[child] += 1

    intermediate_q = deque()

    for u, degree in in_degree.iteritems():
        if in_degree[u] == 0:
            intermediate_q.append(u)

    final_q = deque()

    while intermediate_q:
        no_in_degree = intermediate_q.pop()
        final_q.append(no_in_degree)
        for v in graph[no_in_degree]:
            in_degree[v] -=1
            if in_degree[v] == 0:
                intermediate_q.append(v)

    if len(final_q) == len(graph_tasks):
        return final_q
    else:
        return []

print kahn_s (graph_tasks)

# 2. Modified DFS

def dfs_topsort(graph):         # recursive dfs with
    L = []                      # additional list for order of nodes
    visited = { u : False for u in graph }
    found_cycle = [False]
    for u in graph:
        if not visited[u]:
            dfs_visit(graph, u, visited, L, found_cycle)
        if found_cycle[0]:
            return []

    return L.reverse()                   # L contains the topological sort


def dfs_visit(graph, u, visited, L, found_cycle):
    if found_cycle[0]: return
    visited[u] = True
    for v in graph[u]:
        if visited[v]:
            found_cycle[0] = True
            return
        if not visited[v]:
            dfs_visit(graph, v, visited, L, found_cycle)
    visited[u] = True       # when we're done with u,
    L.append(u)             # add u to list (reverse it later!)

order = dfs_topsort(graph_tasks)
for task in order:
    print(task)















