"""
Little code challenge to look for a word in one of those "find the word in the box" puzzles you often find in puzzle books and such.
"""

puzzle = (
    ('a', 'c', 'a', 't', 'e'),
    ('w', 'b', 'g', 'd', 'i'),
    ('f', 'l', 'o', 'w', 't'),
    ('q', 'r', 'k', 'u', 's'),
    ('e', 'm', 'e', 'h', 't'),
)

words = (
    "cat",
    "flow",
    "theme",
    "erode",
    "about"
)

DIRECTIONS = (
    (-1, 0, "Up"),
    (-1, 1, "Diagonally Up Right"),
    (0, 1, "Right"),
    (1, 1, "Diagonally Down Right"),
    (1, 0, "Down"),
    (1, -1, "Diagonally Down Left"),
    (0, -1, "Left"),
    (-1, -1, "Diagonally Up Left")
)


def look_for_word(word: str):
    num_of_rows = len(puzzle)
    num_of_columns = len(puzzle[0])
    for row in range(num_of_rows):
        for col in range(num_of_columns):
            if puzzle[row][col] == word[0]:  # Found first letter in word in puzzle.
                for d in DIRECTIONS:  # Starting with the up direction and moving clockwise from there.
                    i = 0
                    letters = []
                    for letter in word:
                        offsetRow = d[0] * i
                        offsetCol = d[1] * i
                        try:
                            if puzzle[row+offsetRow][col+offsetCol] == letter:
                                letters.append(letter)
                                i += 1  # Next letter in word found - keep looking in this direction.
                            else:
                                break  # Not the right letter - word wasn't found in this direction.
                        except:
                            break  # Reached end of row or column - prevent crash from index out of range exception.
                    if "".join(letters) == word:
                        return f'Word "{word}" found starting at row {row+1} and column {col+1}. Look {d[2]}.'
    return f'Word "{word}" not found.'
