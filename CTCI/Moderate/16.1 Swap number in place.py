def swap(a,b):

    a = a-b
    b = b+a
    a = b-a

    # or
    # a ^= b
    # b ^= a
    # a ^= b

    return a,b

print swap(6,5)
