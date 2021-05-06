# Optimus Primes - can probably be better, but, ugh...
import math

def primes(count:int):
    '''
    Get prime number at count.
    '''
    i = 1
    p = 0
    while i <= count:
        i += 1
        if i % 2 == 0 and i > 2: continue
        for n in range(3,int(math.sqrt(i))+1,2):
            if i % n == 0: break
        else: p += 1
    return p