from collections import Counter
def countAnagram(s1, s2):
    initial = s2[:len(s1)]
    s1_d = Counter(s1)
    s2_d = Counter(s2[:len(s1)])
    count = 0
    if s1_d==s2_d: count+=1
    for idx, item in enumerate(s2[len(s1):]):
        s2_d[s2[idx]] -=1
        if s2_d[s2[idx]]==0:
            del s2_d[s2[idx]]
        if item in s2_d:
            s2_d[item] +=1
        else:
            s2_d[item] =1
        if s1_d==s2_d: count+=1
    return count
print countAnagram("hi", "hihhellohiiih")
