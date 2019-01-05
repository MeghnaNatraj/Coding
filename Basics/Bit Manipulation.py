__author__ = 'Meghna'

# https://wiki.python.org/moin/BitManipulation
# while parity > 1 : parity = (parity & 1) ^ (parity >> 1)

a = 32
parity = 0

# # METHOD 1
# while a :
#     parity ^= a & 1
#     a >>= 1

# # METHOD 2
# while a :
#     parity ^= 1
#     a &= (a-1) // drops the lowest bit set of a

# print parity


# How to swap bits

def swapbits(x,i,j):
    if (x>>i&1 != x>>j&1):
        x ^= 1 << i | 1 << j
    return x
print(swapbits(73,1,6))
