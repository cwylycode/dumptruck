# Execute or exile the unordered comrades!

def stalin_sort_1(nums:list):
    # C-style in-place sorting
    i = 1
    while True:
        try:
            if nums[i] > nums[i-1]:
                i += 1
                continue
            del nums[i]
        except:
            break

# x = [3,1,4,5,9,2,1]
# stalin_sort_1(x)
# print(x)

def stalin_sort_2(nums:list):
    # Returnable reference sorting
    nums_sorted = [nums[0]]
    for i in range(1,len(nums)):
        if nums[i] < nums_sorted[-1]:
            continue
        nums_sorted.append(nums[i])
    return nums_sorted

# x = [3,1,4,5,9,2,1]
# y = stalin_sort_2(x)
# print(y)