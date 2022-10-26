def multiply_persistence(number: int, print_path: bool = False) -> int:
    count = 0
    digits = str(number)
    while len(digits) > 1:
        n = 1
        count += 1
        for d in digits:
            n *= int(d)
        if print_path:
            s = ' * '.join([d for d in digits])
            print(f"{count}). {s} = {n}")
        digits = str(n)
    return count


x = 39
print(multiply_persistence(x, True))

# 39 -> 3 (3*9=27, 2*7=14, 1*4=4, end)
# 999 -> 4 (9*9*9=729, 7*2*9=126, 1*2*6=12, 1*2=2, end)
# 4 -> 0 (4, end)
# 11111 -> 1 (1*1*1*1*1=1, end)