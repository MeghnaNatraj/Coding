__author__ = 'Meghna'

import itertools
print(["".join(i) for i in itertools.product("01", repeat=3)])

def append(x,L):
    return [x + bit for bit in L]

def nbinary(n):
    if(n==1): return ["0","1"]
    else:
        n_minus_1 = nbinary(n-1)
        return (append("0",n_minus_1)+append("1",n_minus_1))


print nbinary(4)

