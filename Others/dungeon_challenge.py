data = [5,6,0,4,2,4,1,0,0,4]
data = [0,0,0]
memo = [None]*len(data)
def traverse(i, data):
    if memo[i] is None:
        if data[i] == 0:
            memo[i]=float("inf")
        elif i + data[i] >= len(data):
            memo[i]=1
        else:
            traversals = [traverse(j, data)+1 for j in range(i+1,i+1+data[i])]
            memo[i] = min(traversals)
    return memo[i]

def path(i):
    print i
    if i + data[i] >= len(data):
        print("out")
    else:
        next_hop = memo[i+1:i+1+data[i]]
        path(i+1+next_hop.index(min(next_hop)))


traverse(0,data)
if memo[0] == float("inf"):
    print "failure"
else:
    path(0)
