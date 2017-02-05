__author__ = 'Meghna'

import time

start_time = time.time()
from operator import mul
def factorial(n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f

def rank_finder(word):

    length = len(word)
    sorted_word = ''.join(sorted(word))
    position = []
    no_greater = []

    for idx in range(length):
        position.append(sorted_word.find(word[idx])+1)

    for idx_outer in range(length):
        count = 0
        for idx_inner in range(idx_outer + 1,length):
            if position[idx_outer] > position[idx_inner]:
                count +=1
        no_greater.append(count)

#     no_greater = []
#     for idx_outer in range(length):
#         no_greater.append(''.join(sorted(word[idx_outer:])).find(word[idx_outer]))



    remove_repetitions = []
    for idx_outer in range(length):
        remove_repetitions.append(word[idx_outer:].count(word[idx_outer]))
    for idx_outer in range(length):
        remove_repetitions[idx_outer] = reduce(mul, remove_repetitions[idx_outer:] , 1)

    total = 0
    for idx in range(length):
        total += factorial(length-idx-1) * no_greater[idx] / remove_repetitions[idx]
    return total + 1


print rank_finder('QUESTION')
print rank_finder('BOOKKEEPER')
print("--- %s seconds ---" % (time.time() - start_time))




import itertools
start_time = time.time()
items = 'QUESTION'
for idx,combination in enumerate(sorted(list(set(itertools.permutations(items, len(items)))))):
    if ''.join(combination) == items :
        print idx+1
        break
items = 'BOOKKEEPER'
for idx,combination in enumerate(sorted(list(set(itertools.permutations(items, len(items)))))):
    if ''.join(combination) == items :
        print idx+1
        break
print("--- %s seconds ---" % (time.time() - start_time))




start_time = time.time()
def fact(n):
    """factorial of n, n!"""

    f = 1

    while n > 1:
         f *= n
         n -= 1

    return f



def rrank(s):
    """Back-end to rank for 0-based rank of a list permutation"""

    # trivial case
    if len(s) < 2: return 0

    order = s[:]
    order.sort()

    denom = 1

    # account for multiple occurrences of letters
    for i, c in enumerate(order):
        n = 1
        while i + n < len(order) and order[i + n] == c:
            n += 1

        denom *= n

    # starting letters alphabetically before current letter
    pos = order.index(s[0])

    #recurse to list without its head
    return fact(len(s) - 1) * pos / denom + rrank(s[1:])



def rank(s):
    """Determine 1-based rank of string permutation"""

    return rrank(list(s)) + 1



strings = [
    "QUESTION", "BOOKKEEPER"
]

for s in strings:
    print s, rank(s)
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
from collections import Counter

def rankperm(perm):
    rank = 1
    suffixperms = 1
    ctr = Counter()
    for i in range(len(perm)):
        x = perm[((len(perm) - 1) - i)]
        ctr[x] += 1
        for y in ctr:
            if (y < x):
                rank += ((suffixperms * ctr[y]) // ctr[x])
        suffixperms = ((suffixperms * (i + 1)) // ctr[x])
    return rank
print(rankperm('QUESTION'))
print(rankperm('BOOKKEEPER'))
print("--- %s seconds ---" % (time.time() - start_time))
