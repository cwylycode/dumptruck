# Say whaaaaaa...

import re

def look_and_say(depth:int, start:str="1"):
    """
    From Wikipedia:
    
    In mathematics, the look-and-say sequence is the sequence of integers beginning as follows:

    1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ... (sequence A005150 in the OEIS).
    
    To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:

    1 is read off as "one 1" or 11.

    11 is read off as "two 1s" or 21.

    21 is read off as "one 2, then one 1" or 1211.

    1211 is read off as "one 1, one 2, then two 1s" or 111221.

    111221 is read off as "three 1s, two 2s, then one 1" or 312211.
    """
    current,i = start,0
    if depth < 0: return ""
    yield start
    while i < depth:
        arr = []
        i += 1
        for x,y in re.findall(r"(.)(\1*)",current):
            arr.append(str(len(x+y))+x)
        current = "".join(arr)
        yield current