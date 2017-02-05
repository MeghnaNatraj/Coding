__author__ = 'Meghna'
from itertools import product
from collections import Counter

def evaluate(guess, secret):
    matches = sum((Counter(secret) & Counter(guess)).values())
    bulls = sum(c == g for c, g in zip(secret, guess))
    return bulls, matches - bulls

ALL_CODES = [''.join(c) for c in product('ABCDEF', repeat=4)]
def knuth(secret):
    assert(secret in ALL_CODES)
    codes = ALL_CODES
    key = lambda g: max(Counter(evaluate(g, c) for c in codes).values())
    guess = 'AABB'
    while True:
        feedback = evaluate(guess, secret)
        print("Guess {}: feedback {}".format(guess, feedback))
        if guess == secret:
            break
        codes = [c for c in codes if evaluate(guess, c) == feedback]
        print codes
        if len(codes) == 1:
            guess = codes[0]
        else:
            guess = min(ALL_CODES, key=key)            