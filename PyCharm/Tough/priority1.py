__author__ = 'Meghna'

import itertools
import heapq

pq = []

counter = itertools.count()

def add_task(task,priority=0):

    count = next(counter)
    entry = [priority, count, task]
    heapq.heappush(pq,entry)

def pop_task():
    if pq:
        return heapq.heappop(pq)[2]
    raise KeyError('pop from an empty queue not possible')

add_task("eat",1)
add_task("love",1)
add_task("cry",1)
add_task("sleep",10)
add_task("sleep",0)
add_task("sleep",0)
print(pq)
print()
print(pop_task())
print(pop_task())
print(pop_task())
print(pop_task())
print(pop_task())
print(pop_task())
print(pq)
print()

