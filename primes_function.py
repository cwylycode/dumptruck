#Optimus Primes
def primes(start:int,end:int):
    pl = []
    if start < 0: start = 0
    for i in range(start,end+1):
        if (i % 2 == 0 and i > 2) or (i in [0,1]): continue
        for n in range(3,int(i**0.5)+1,2):
            if i % n == 0: break
        else: pl.append(i)
    return pl