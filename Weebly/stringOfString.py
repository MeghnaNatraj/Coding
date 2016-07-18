def stringOfString(alist,result):
    if type(alist) == str:
        result.append(alist)
        return
    for item in alist:
        stringOfString(item,result)
    return result
print stringOfString([[[["String1"],[["String2"]]]],"String3"],[])