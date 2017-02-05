def factorial (n):
    if n==1:
        return n
    else:
        return n * factorial(n-1)

def numOfPalindrones(string):
    d = {}
    numerator = 0
    denominator = 1
    odd = 0
    even = 0
    for i in range(len(string)):
        if string[i] not in d:
            d[string[i]] = 1
        else:
            d[string[i]] += 1
    for key, value in d.iteritems():
        if value % 2 == 1 :
            if odd: return 0
            odd += 1
        else:
            denominator *= factorial(value/2)
            numerator += factorial(value/2)
    print numerator,denominator
    numerator = factorial(numerator) / denominator
    return numerator

numOfPalindrones("done")