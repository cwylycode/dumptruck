def is_anangram(name: str, wordlist: list) -> bool:
    wordlist = [x.lower() for x in wordlist]
    name = name.lower()
    for char in name:
        if char == ' ':
            continue
        char_found = False
        for i in range(len(wordlist)):
            if char in wordlist[i]:
                wordlist[i] = wordlist[i].replace(char, '', 1)
                char_found = True
                break
        if not char_found:
            return False
    if any(wordlist):
        return False
    return True


print(is_anangram("Jeff Goldblum", ["jog", "meld", "bluffs"]))

# is_anagram("Justin Bieber", ["injures", "ebb", "it"]) ➞ True

# is_anagram("Natalie Portman", ["ornamental", "pita"]) ➞ True

# is_anagram("Chris Pratt", ["chirps", "rat"]) ➞ False, Not all letters are used

# is_anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]) ➞ False, "s" does not exist in the original name