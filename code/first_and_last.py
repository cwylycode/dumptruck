#First And Last - find the starting and ending indexes of target (iter should be ordered)

#Algorithm 1: Find first target from start of iter going forward and then last target from end of iter going backward
def fal_ends(elems:list,target):
    first,last = -1,-1
    for i in range(0,len(elems)):
        if elems[i] == target:
            first = i
            break
    if first == -1: return [first,last]
    for i in range(len(elems)-1,-1,-1):
        if elems[i] == target:
            last = i
            break
    return [first,last]

#Algorithm 2: Find first target from start of iter going forward and then keep counting until last target found
def fal_gap(elems:list,target):
    first,last = -1,-1
    for i in range(0,len(elems)):
        if elems[i] == target:
            first = i
            break
    if first == -1: return [first,last]
    for i in range(first,len(elems)):
        if elems[i] == target:
            last = i
            continue
        break
    return [first,last]

nums = sorted((4,5,4,7,2,3,4,5,6,9,8,7,1,3,1,9,9,9,8,7,8))
s = sorted(("hello","help","barf","goodbye","asset","hello","bar","barf","cheese","barf"))
print(nums)
#print(s)
print(fal_ends(nums,9))
#print(fal_gap(nums,9))