# Jesus: Treat others the way you want to be treated.
# Apostles: Even the lepers and those who worship other gods?
# Jesus: D-Did I s-stutter?
# Apostles: Um... yes?
# Jesus: I s-see... I t-think I-I'm having a s-stroke.
# Apostles: Oh, really? Well, then, son of God, heal thyself!
# (Everyone laughs - some laugh so hard they vomit)

import random
import string
import re


def stutter_string(text: str, frequency: float = 0.5):
    """
    Give y-your string the s-stutter t-treatment. C-Change frequency for a g-greater or lesser e-effect (between 1.0 and 0.0).
    """
    words = []
    for word in re.split(r'(\s+)', text):
        if word and word[0] in string.ascii_letters:
            extra = random.choices([f"{word[0]}-", ""], [frequency, 1.0-frequency])[0]
            words.append(extra+word)
            continue
        words.append(word)
    return "".join(words)


if __name__ == "__main__":
    print(stutter_string("Don't make me angry. You won't like me when I'm angry."))
