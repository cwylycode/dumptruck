# Reinventing the wheel, one pointless line of code at a time

def random_lcg(minimum:int,maximum:int,seed:int=0):
    """
    A random function using a linear congruential generator algorithm.
    """
    if minimum > maximum:
        raise ValueError("Minimum cannot be greater than maximum")
    a,c,m = 1664525,1013904223,(2**32)
    r,z = seed,1
    while True:
        r = (a*r+c) % m
        x = (maximum + 1 - minimum)
        if z:
            z = 0
            continue
        yield int((r/m)*x + minimum)

def roll_some_dice(limit:int,algorithm,*args):
    dice = algorithm(*args)
    prev_roll = 0
    i = 1
    current_iter = 0

    while i < limit:
        current_iter += 1
        x = next(dice)
        if x == prev_roll: i += 1
        else:
            i = 1
            prev_roll = x

    print(f"It took {current_iter} rolls of the dice to get the same number {limit} times in a row.\nThe dice number was {prev_roll}.")

roll_some_dice(4,random_lcg,1,6,0)