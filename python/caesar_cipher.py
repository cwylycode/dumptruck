__alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(txt:str="",shift:int=1)->str:
    """Encrypts and returns a text message by shifting letters to the left or right on the alphabet.\n
    E.G. Shift = 2, 'A' -> 'C' | Shift = -2, 'A' -> 'Y'\n
    Only alpha characters are shifted and will become uppercased. Numbers/symbols/spacing are preserved in place."""

    encoded = []
    txt = txt.strip()
    for c in txt:
        i = __alpha.find(c.lower())
        if i != -1: encoded.append(__alpha[(i+shift) % len(__alpha)])
        else: encoded.append(c)
    return "".join(encoded).upper()

def decrypt(txt:str="",shift:int=0):
    """Decrypts a text message that has been encrypted by Caesar's cipher by shifting letters through the alphabet.\n
    If the character shifting is known, input it and the whole message will be returned. If unknown, input 0 and the first ten words will be shifted through the entire alphabet and printed each cycle. Human comprehension required to determine correct shift for remainder of message."""

    txt = txt.strip()
    def cycle(t,s):
        decoded = []
        for c in t:
            i = __alpha.find(c.lower())
            if i != -1: decoded.append(__alpha[(i+s) % len(__alpha)])
            else: decoded.append(c)
        return "".join(decoded).upper()
    if shift != 0: return cycle(txt,shift)
    else:
        print("Starting manual decryption...")
        words = " ".join(txt.split(" ")[0:10 if len(txt)>=10 else len(txt)])
        for shi in range(1,len(__alpha)+1):
            print(f"\nShift: {shi}\n{cycle(words,shi)}")
        print("\nDecryption finished. Find anything?")