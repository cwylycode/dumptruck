import random

def generate_password(char_length:int):
    if char_length > 50 or char_length < 8: return "Stoopid"
    exclude = (' ','{','}','[',']','(',')','|','/','\\',"'",'"','`','~',',',';',':','.','<','>')
    chars_list = tuple(filter(lambda x: (x not in exclude),(chr(i) for i in range(32,127))))
    password = []
    for i in range(char_length):
        while True:
            c = random.randrange(0,len(chars_list))
            if password.count(chars_list[c]) > 2: continue
            else: break
        password.append(chars_list[c])
    return "".join(password)

print("Generate a random password\n")
initial = int(input("How many characters long should the password be? (8-50)\n>"))
while True:
    print(f"Your password is: {generate_password(initial)}")
    again = input("\nPress enter to try again.")