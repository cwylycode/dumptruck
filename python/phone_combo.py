# Ring ring ring...banana phone

def phone_letter_combos(nums):
    """
    Return all possible letter combinations found on a phone pad from integers entered.
    """
    combos = {
        "0": ["_"],
        "1": [""],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    nums,final = str(nums),[]
    def loop(n,s):
        if n == len(nums):
            final.append(s)
            return
        for v in combos[nums[n]]:
            loop(n+1,s+v)
        return final
    return loop(0,"")