import random
import string
import re


def italianize(text: str, italianness: float = 0.5):
    """
    Italianize your English words! Make your text sound like a REAL Italian stereotype! It's fun for the whole family - and needlessly offensive, too!

    Italianness range is 0.0 - 1.0 (no changing words - all valid words get changed)
    """
    words = []
    for word in re.split(r'([.,?!:;*\s]+)', text):
        if word and word[-1] in string.ascii_letters:
            if not word[-1].lower() in ['a', 'e', 'i', 'o', 'y']:
                extra = random.choices(["-a" if word[-1].islower() else "-A", ""], [italianness, 1.0-italianness])[0]
                words.append(word+extra)
                continue
        words.append(word)
    return "".join(words)


if __name__ == '__main__':
    t = "Hello. I would like a lot of spaghetti. Would you bring me a mushroom and some coins with the dish? Also, a peach salad for the princess as well, yes?"
    print(italianize(t))
