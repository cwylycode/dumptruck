#Sing along with your drunk friends. But not me! I don't drink or sing! ... and I don't have any friends :(
from time import sleep
init_bottles = int(input("How many bottles of beer on the wall we got?\n"))
bottles = 0 if init_bottles < 0 else init_bottles
lyrics = ["_ bottles of beer"," on the wall","Take one down,","pass it around,","Go to the store,","and buy some more,"]
def song_update():
    first_section = [lyrics[0].replace("_","No more" if bottles == 0 else str(bottles),1),lyrics[1]]
    last_section = [lyrics[2],lyrics[3]] if bottles != 0 else [lyrics[4],lyrics[5]]
    if bottles == 1:first_section[0] = first_section[0].replace("s","",1)
    return first_section,last_section
while True:
    song = song_update()
    print("\n"+song[0][0]+song[0][1])
    sleep(2.5)
    print(song[0][0]+"...")
    sleep(2.2)
    print(song[1][0])
    sleep(1.4)
    print(song[1][1])
    sleep(1.4)
    bottles -= 1
    if init_bottles <= 0:init_bottles = 99
    if bottles < 0:bottles = init_bottles
    song = song_update()
    print(song[0][0]+song[0][1])
    sleep(2.6)