__author__ = 'Meghna'

s = []
s.append(5)
print(s.pop())

from collections import deque
q = deque(["A","B","C"])
q.append("D")
print(q.popleft())