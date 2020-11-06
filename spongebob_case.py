#This is a load of barnacles
import random

def spongebob_case(txt: str = ""):
    final = ""
    txt = txt.strip().lower()
    for i in range(0, len(txt)):
        toggle = bool(random.randint(0, 1))
        last_two = final[i - 2 if (i - 2) > 0 else 0:i]
        if toggle:
            if last_two.isupper(): final += txt[i].lower()
            else: final += txt[i].upper()
        else:
            if last_two.islower(): final += txt[i].upper()
            else: final += txt[i].lower()
    return final

text = "You can't just come in here and make a Spongebob meme!"
print(spongebob_case(text))