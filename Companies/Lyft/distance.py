__author__ = 'Meghna'


# For the 4 points provided, I have considered 6 routes that we can take.
# The criteria is that we must got to point A before point B and we must go to point C before point D
# The gives us 6 possible routes : ["ABCD","CDAB","CABD","ACBD","ACDB","CADB"]
# We calculate all the distances using the Havesine's Formula to calculate the distance between 2 points with a (lat,long)
# We pick the smallest path all amongst possible 6 paths.

import math
metric = True
Radius = 6371 if metric == True else Radius = 3963.1676

def toRadians(num): return num * math.pi/180;

def calcDistance(X, Y) :
    xLat = toRadians(X[0])
    yLat = toRadians(Y[0])
    diffLat = toRadians(xLat - yLat)
    diffLon = toRadians(X[1] - X[1])

    a = math.pow(math.sin(diffLat/2), 2) + (math.cos(xLat) * math.cos(yLat) * math.pow(math.sin(diffLon/2), 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return Radius * c

def calcRoute():
    A = [1,1]
    B = [3,3]
    C = [2,2]
    D = [4,4]

    distAB = calcDistance(A, B)
    distAC = calcDistance(A, C)
    distAD = calcDistance(A, D)
    distBC = calcDistance(B, C)
    distBD = calcDistance(B, D)
    distCD = calcDistance(C, D)

    alist = [distAB + distBC + distCD, distAB + distAD + distCD,
             distAB + distAC + distBD, distAC + distBC + distBD,
             distAC + distBD + distCD, distAC + distAD + distBD]
    routes = ["ABCD","CDAB","CABD","ACBD","ACDB","CADB"]
    print "The shortest route is : ",routes[alist.index(min(alist))]
calcRoute()

