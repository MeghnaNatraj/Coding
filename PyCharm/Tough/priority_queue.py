__author__ = 'Meghna'
import itertools
import heapq

pq = []
entry_finder = {}
counter = itertools.count()
REMOVED = 'Removed'

def add_task(task, priority=0):
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority,count,task]
    entry_finder[task] = entry
    heapq.heappush(pq,entry)

def remove_task(task):
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    while pq:
        priority,count, task  = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty queue')


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



