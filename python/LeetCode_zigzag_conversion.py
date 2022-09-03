'''
LeetCode challenge (medium difficulty)
https://leetcode.com/problems/zigzag-conversion/

Funny enough, I had many different ways to solve this on a technical level using loops for rows and columns, but, looking at the examples they gave, I couldn't understand why the output pattern looked the way it did with all the seemingly random spaces and structuring.

I eventually realized that it really was supposed to "zigzag" from side-to-side in a vertical fashion and only figured it out after I literally tilted my head 90 degrees anticlockwise and saw the pattern.

It was one of those moments where you can feel like a genius, but somehow fail the common sense test without even realizing it.
'''


def zigzag(string: str, rows: int) -> str:
    """
    Output a string as if it were a zigzagged pattern. See link to the LeetCode challenge for a general idea of how the zigzag pattern works.
    """
    if string is None or rows <= 1:
        return string
    result = ""
    step = 2 * rows - 2
    for r in range(rows):
        for i in range(r, len(string), step):
            result += string[i]
            if r != 0 and r != rows - 1 and (i + step - 2 * r) < len(string):
                result += string[i + step - 2 * r]
    return result


string = 'paypalishiring'
print(zigzag(string, rows=4))
