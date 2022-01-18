"""
This script is used for 'writing' songs in musical notation form, with recording of key downs and ups being used to define the time durations and delays of notes. Notes are shown line by line and a single key on your keyboard can be used to set the timing for each note in a song - of course, you'll need to know the song by heart.

All that is needed is the pynput module installed and a file containing your music notes. You will need to pass the music notes file as an argument. To start, call this script from python in the terminal - e.g.:

$ python3 musical_timing_recorder.py <path to your music notes file>

Once all the music notes have been 'played' by you, an out file gets written to in the same directory as your music notes file. This text file will contain 3 separate sections - the notes, the note durations, and the note gaps.
"""

from pynput import keyboard
import time
import os,sys

DEBUG = False
KILL = False

# Keyboard key handling
key_held = False

def key_down(key):
    global key_held,KILL
    key_held = True
    if key == keyboard.Key.esc: KILL = True

def key_up(key):
    global key_held
    key_held = False

kl = keyboard.Listener(on_press=key_down,on_release=key_up,suppress=True)
kl.start()

# Execute
if __name__ == "__main__":
    # Init
    if not DEBUG:
        args = sys.argv
        if os.path.isfile(args[1]): notes_file = args[1]
        else: raise FileNotFoundError("Error: missing positional argument - music notes file")
    else:
        notes_file = "<INSERT MUSIC NOTES FILE HERE>" # Ignore this
    with open(notes_file,"r") as f:
        x = f.readlines()
        lines = [i.strip() for i in x]

    # Clear screen and show greeter
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Musical Timing Recorder ({os.path.basename(notes_file)})\nPress 'Esc' to quit\n\n")
    print("When you are ready, Maestro...\n")

    # Recording loop system
    line_count = len(lines)
    durations,gaps = [],[]
    t,time_d,time_g = 0,0,0
    recording_started = False
    for n,line in enumerate(lines):
        # Print out the current sheet line for the user
        print(f"\nLine: {n+1}\n \t{line}\n> \t",end="")
        if not recording_started:
            # Wait for user to press key for first time
            while not key_held: continue
            if KILL: exit()
            recording_started = True
        # Notes per line recording loop start
        notes = line.split()
        note_count = len(notes)
        for i,note in enumerate(notes):
            while not key_held: continue # Failsafe
            if key_held:
                print(note+" ",end="",flush=True)
                t = time.time()
                while key_held: time_d = (time.time() - t)
                if KILL: exit()
                durations.append(time_d)
            if not key_held:
                # Abruptly stop and don't record gap for last note
                if n+1 >= line_count and i+1 >= note_count:
                    gaps.append(0)
                    break
                t = time.time()
                while not key_held: time_g = (time.time() - t)
                if KILL: exit()
                gaps.append(time_g)
        durations.append("\n")
        gaps.append("\n")
        print("\n")
    # Finished recording - cleanup and write data to output file
    out_file = os.path.basename(notes_file).split(".")[0]+"_output.txt"
    melody = []
    for l in lines:
        clean = l.split()
        x = [f"\"{n}\"," for n in clean]
        x.append("\n")
        melody.extend(x)
    for i in range(len(gaps)):
        if gaps[i] == "\n":continue
        durations[i] = f"{durations[i]:.3F},"
        gaps[i] = f"{gaps[i]:.3F},"
    with open(f"{out_file}","w") as f:
        f.write("Melody:\n")
        f.writelines(melody)
        f.write("Durations:\n")
        f.writelines(durations)
        f.write("Gaps:\n")
        f.writelines(gaps)
    print(f"Finished - Data written to ./{out_file}")