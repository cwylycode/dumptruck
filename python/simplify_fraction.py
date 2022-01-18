# Simpletons

def simplify_fraction(fraction:str):
    try:
        nums = fraction.split("/")
        fnums = [float(nums[0]),float(nums[1])]
        div = fnums[0] / fnums[1]
    except: return fraction
    if not fnums[0].is_integer() or not fnums[1].is_integer():
        return f"{nums[0]}/{nums[1]}"
    if div > 1 and div.is_integer():
        return int(div)
    n1,n2 = int(fnums[0]),int(fnums[1])
    for n in range(n1,0,-1):
        r = [(n1/n),(n2/n)]
        if r[0].is_integer() and r[1].is_integer():
            return f"{int(r[0])}/{int(r[1])}"
    return f"{n1}/{n2}"

def fraction(number:float):
    n = float(round(number,4))
    x = str(n)
    if n.is_integer(): return int(float(x))
    deci_count = x[::-1].find(".")
    if deci_count > 0:x = str(n*(10**deci_count))+"/"+str(1*(10**deci_count))
    return simplify_fraction(x)

# f = [
#     "10/11",
#     "100/400",
#     "4/6",
#     "8/4",
#     "5/2.5",
#     "3/18",
#     "10/15",
#     "6/5",
#     "88",
# ]
# print(*[simplify_fraction(x) for x in f],sep='\n')

# d = [
#     0,
#     1,
#     2.5,
#     2.000041,
#     0.1,
#     0.2,
#     0.5,
#     10,
#     0.9,
#     0.01,
#     0.000008,
#     0.0001,
#     342.52,
# ]
# print(*[fraction(x) for x in d],sep='\n')