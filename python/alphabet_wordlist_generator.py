#This was originally supposed to be a multithreading exercise - turns out, the code runs better without it. Go figure.
from os import name,system
from time import time,sleep
from datetime import timedelta
from itertools import product

def main():
    progress_percent,progress_eta,progress_update = 0,0,True
    min_chars,max_chars,lines = 0,0,0

    def clear_screen():
        if name == "nt": system("cls")
        else: system("clear")

    def calculate_lines(a,b):
        x = 0
        for i in range(b,a-1,-1): x += 26**i
        return x

    def word_generator(min_char_len:int=1,max_char_len:int=16,capitalize:bool=True):
        alpha = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
        i = min_char_len
        while i <= max_char_len:
            for combo in product(alpha,repeat=i):
                word = "".join(combo)
                yield word.capitalize() if capitalize else word
            i += 1

    def update_screen():
            clear_screen()
            remaining = progress_eta if progress_eta > 0 else 0
            print("\nCreating wordlist...this may take a ridiculously long time")
            print("\nTip: The wordlist is stored in the same directory as this python file. Go find it.\n")
            print(f"Progress: {round(progress_percent if progress_percent <= 100 else 100)}%")
            print(f"Estimated Time Remaining: {timedelta(seconds=remaining)}")

    while True:
        print("\nGenerate a wordlist of all possible alphabet combinations")
        print("\nEnter the minimum(>0) and maximum(<65) character length - separated by a comma")
        usr = input().split(",")
        if len(usr) == 2:
            try:
                min_chars = int(usr[0].strip())
                max_chars = int(usr[1].strip())
                if (0 < min_chars <= max_chars) and max_chars <= 64: break
            except: pass
        clear_screen()
        print("\nWrong! Try again.")

    with open("wordlist.txt","w") as file:
        words = word_generator(min_chars,max_chars,False)
        temp,write,chunk_size = [],True,(10**6)
        lines = calculate_lines(min_chars,max_chars)
        st = time()
        update_screen()
        while write:
            for i in range(chunk_size):
                try: temp.append(next(words)+"\n")
                except StopIteration:
                    write = False
                    break
            file.writelines(temp)
            temp.clear()
            progress_percent += (chunk_size / lines) * 100
            progress_eta = (100 - progress_percent) * (time() - st) / progress_percent
            update_screen()

    progress_update = False
    update_screen()
    done = input("\nDone! Your wordlist is finished and might be enormous. Handle with care.\nPress enter to exit...")

if __name__ == "__main__":
    main()