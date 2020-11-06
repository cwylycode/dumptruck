import random

min_len = 8
max_len = 64
max_dupes = 2
exclude = (' ','{','}','[',']','(',')','|','/','\\',"'",'"','`','~',',',';',':','.','<','>')

def generate_password(char_length:int):
    if char_length > max_len or char_length < min_len: return "Stoopid"
    chars_list = tuple(filter(lambda x: (x not in exclude),(chr(i) for i in range(32,127))))
    password = []
    for i in range(char_length):
        while True:
            c = random.randrange(0,len(chars_list))
            if password.count(chars_list[c]) > max_dupes: continue
            else: break
        password.append(chars_list[c])
    return "".join(password)

print("Generate a random password\n")
initial = int(input(f"How many characters long should the password be? ({min_len}-{max_len})\n>"))
while True:
    print(f"Your password is: {generate_password(initial)}")
    again = input("\nPress enter to try again.")