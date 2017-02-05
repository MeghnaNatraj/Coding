# 1. Sort a dictionary by keys/values

from heapq import heappop, heappush
a = {"500": 2.3, "201":3.5, "436":4.2,"302":4.9}

h = []
for key, value in a.items():
    heappush(h, (value,key))
sorted_values = []

import operator
sorted_x = sorted(a.items(), key=operator.itemgetter(1))
print sorted_x
