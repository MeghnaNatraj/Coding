# iterate over larger string, idx++ of smaller string only if char is equal.
# if not then set flagDiff to True. If this repeats, return False.
# Check code to handle all cases (more code) for +1,-1 char or update.
def oneAway(s1,s2):

    if abs(len(s1) - len(s2)) > 1 :
        return False

    if len(s1) < len(s2): s1 , s2 = s2, s1

    foundDiff = False
    j=0

    for i in range(len(s1)):
        if s1[i] != s2[j]:
            if foundDiff:
                return False

            foundDiff = True
            if len(s1)!=len(s2): continue
        j += 1

    return True

print oneAway("pale","bale")
