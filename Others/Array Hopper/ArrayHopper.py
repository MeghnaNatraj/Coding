def check(path):
    lines = [int(line.rstrip('\n')) for line in open(path)]
    flag = True
    hops = []
    limit_reach,max_reach,best_reach = 0,0,0
    for i in range(len(lines)):
            if i > max_reach : flag = False; break
            if i > limit_reach:
                limit_reach = max_reach
                hops.append(str(best_reach))
                if limit_reach >= len(lines): break
            reachability = i + lines[i]
            if reachability > max_reach:
                best_reach = i
                max_reach = reachability
    if flag : hops.append(str(best_reach))
    if (limit_reach < len(lines) - 1 or not hops): print "failure"
    else:
        hops.append("out")
        print str(hops)
test_files = ["GivenSampleInput.txt"]
for i in range(1,8):
    test_files.append("CustomInput"+str(i)+".txt")
for test_file in test_files:
    check(test_file)