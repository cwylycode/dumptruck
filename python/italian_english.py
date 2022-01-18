import random

def italianize(text:str,italianness:float=0.5):
    """Italianize your English words! Make your text sound like a REAL Italian stereotype! It's fun for the whole family - and needlessly offensive, too!\n
    Italianness range is 0.0 - 1.0 (no changing words - all valid words get changed)
    """
    words = text.split(" ")
    for i,word in enumerate([w.lower() for w in words]):
        c = -1
        for j in range(len(word)-1,-1,-1):
            if word[j] in [".","?","!"]: break
            elif word[j].isalpha():
                c = j
                break
        if c != -1:
            try:
                if words[i+1][0].lower() == "a": continue
            except: pass
            if word[c] in ["a","y"]: continue
            elif word == "the": continue
            else:
                change = random.choices([True,False],[italianness,1.0-italianness],k=1)[0]
                if change: words[i] = words[i][:c+1] + "-a" + words[i][c+1:]
    return " ".join(words)

if __name__ == '__main__':
    t = "Hello. I would like a lot of spaghetti. Would you bring me a mushroom and some coins with the dish? Also, a peach salad for the princess as well, yes?"
    print(italianize(t))