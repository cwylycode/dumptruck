# Optimus Primes - can probably be better, but, ugh...
import math


def primes(min_num: int, max_num: int):
    '''
    Generator of prime numbers starting at min and ending at max. Min will always be at least 2 since there are no primes less than 2.
    '''
    i = min_num if min_num > 1 else 2
    while i <= max_num:
        if i % 2 == 0 and i > 2:
            i += 1
            continue
        for n in range(3, int(math.sqrt(i))+1, 2):
            if i % n == 0:
                break
        else:
            yield i
        i += 1


if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if args > 1:
        num_range = (int(sys.argv[1]), int(sys.argv[2]))
    elif args > 0:
        num_range = (0, int(sys.argv[1]))
    else:
        num_range = (0, 1000)
    print("Prime Number Generator - accepts a max number arg or min/max range args (default: 0 1000)")
    print(f"Prime numbers from {num_range[0]} to {num_range[1]} are:\n")
    i = 0
    for x in primes(num_range[0], num_range[1]):
        print(x, end=' ')
        i += 1
    print(f"\n\nTotal: {i}")
