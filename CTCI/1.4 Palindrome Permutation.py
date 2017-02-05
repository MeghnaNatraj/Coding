# Assuming characters between a-z, use a bit vector and toggle for
# each character occurance.
# In the end, check if maximum one of the bits is 1
def palindromePerm(s):

    # (Base case : handle this with True or False)
    if not s:
        return False

    # make lowercase
    s = s.lower()
    start = ord("a")
    bit_vector = 0

    for i in range(len(s)):
        val = ord(s[i]) - start
        bit_vector ^= 1 << val

    return not bit_vector & (bit_vector - 1)

palindromePerm("aac")


