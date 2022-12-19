# There are useful and witty comments peppered throughout the script, you just can't see them because they are encrypted with a hidden subsitution cipher - I swear!
__doc__ = """CRYPTOGRAM DOCUMENTATION

Encode or decode a cryptogram written in a substitution cipher. A substitution cipher replaces each letter of the alphabet with a different letter. The cipher affects only alphabet letters and works by swapping out each letter with a different one. For example, all A's get changed to 'H' and all T's get changed to 'U' and so on.

At least one (and only one) of the following flags must be used when running this script: -g -p -e -d. The first two simply write out a default cipher keyfile or print out these docs, while the other two are used for encoding and decoding and will need a cipher keyfile and a message to properly run the script.

The message can be provided either as a path to a file with the message inside it, or typed directly into the console as a text string. The message can be either in a decoded or encoded form. The appropriate flag must be set to either encode (-e) or decode (-d) the message.

A cipher key is needed to encode/decode messages and comes from a text file (the keyfile). The file's cipher MUST be the same cipher that was used for either encoding or decoding a message. This keyfile should be line-by-line separated and have all 26 capitalized letters, with the corresponding letter to encode be included on the same line and having the two letters separated by an '=' sign. Furthermore, the letters on each side must be unique with no duplicates. To assist with making (and understanding) a keyfile, simply execute this script with the -g/--generate-default-keyfile flag selected and a new key will be generated at the directory path you provide. This keyfile can then be modified at the user's discretion by changing out the letters on the right-hand side of the '=' sign.

Alternatively, it's possible to modify the cipher and the message in realtime using interactive mode.

----------
INTERACTIVE MODE:

After setting the -i/--interactive-mode flag, you'll be presented with a screen showing the message. This message is split line-by-line, with the bottom line being the original message line and the top being the one you modify. Further down is the cipher key showing it's current state, as well as a prompt at the bottom for you to change the letters for the cipher. To change a letter to a different one, simply type the letter to change into the prompt, followed by the letter you wish to change it to. For example, to change all A's in the message to U's, type 'au' into the prompt and press enter - the letters are not case sensitive. When you change the letters, the cipher key and the message both update immediately to reflect the changes. If you want to start over with the original cipher, type 'reset' into the prompt and press enter.

When you have finished, type '0' into the prompt and press enter. If you happened to change any of the letters and had updated the cipher, you will then be presented with a new prompt to save the new cipher. Press 'Y' or 'N' (or some appropriate variant) to either overwrite the cipher in the provided cipher keyfile and exit, or just exit without overwriting. Any other input is invald.

----------
EXAMPLES:

cryptogram.py -g <some/directory/path/file>
result: Write a default cipher key to a file located at the path.

cryptogram.py -e <path/to/keyfile> <path/to/message/file>
result: Message from file gets encoded with cipher and then printed to the console.

cryptogram.py -d -s <path/to/keyfile> 'ASQW TRWSJKG TTJKL.'
result: Message from text string (with the -s flag) gets decoded with cipher and then printed to the console.

cryptogram.py -e -o <path/to/output/file> <path/to/keyfile> <path/to/message/file>
result: Message from file gets encoded with cipher and then written to a file at the output path.

cryptogram.py -i -e -s <path/to/keyfile> 'Some random message.'
result: Message from text string (with the -s flag) gets encoded with cipher in realtime in interactive mode by user. After exiting the mode, the encoded message gets printed to the console.

cryptogram.py <path/to/keyfile> <path/to/message/file> -o <path/to/output/file> -d -i
result: Message from file gets decoded with cipher in realtime in interactive mode by user. After exiting the mode, the encoded message is then written to a file at the output path.

----------
AS A MODULE:

This script can be used as a module to be imported into other python projects. Encoding, decoding and read/write functions can be called directly, and the cipher_key variable can be modified without the need for a keyfile.

----------
TIPS:

In case you don't happen to have the cipher needed to decode a message, here are some tips for manually cracking a substitution cryptogram...

Scan through the cipher, looking for single-letter words. They're almost definitely A or I.

Count how many times each symbol appears in the puzzle. The most frequent symbol is probably E. It could also be T, A, or O, especially if the cryptogram is fairly short.

Pencil in your guesses over the ciphertext. Do typical word fragments start to reveal themselves? Be prepared to erase and change your guesses!

Look for apostrophes. They're generally followed by S, T, D, M, LL, or RE.

Look for repeating letter patterns. They may be common letter groups, such as TH, SH, RE, CH, TR, ING, ION, and ENT.

Try to decipher two-, three-, and four-letter words.

    - Two-letter words almost always have one vowel and one consonant. The five most common two-letter words, in order of frequency, are OF, TO, IN, IS, and IT.

    - The most common three-letter words, in order of frequency, are THE, AND, FOR, WAS, and HIS.

    - The most common four-letter word is THAT. An encrypted word with the pattern 1 - - 1 is likely to be THAT. However, the pattern 1 - - 1 also represents 30 other words, so keep this in mind!

Scan for double letters. They're most likely to be LL, followed in frequency by EE, SS, OO, and TT (and on to less commonly seen doubles).

*Above excerpt regarding crytogram deciphering tips provided by dummies.com"""

import string

cipher_key = {k: v for (k, v) in zip(list(string.ascii_uppercase), list(reversed(string.ascii_uppercase)))}


def encode(key: dict, message: str):
    d_keys = list(key.keys())
    string = ""
    for char in message.upper():
        c = char
        if char in d_keys:
            c = key[char]
        string += c
    return string


def decode(key: dict, message: str):
    reversed_key = {v: k for (k, v) in key.items()}
    d_keys = list(reversed_key.keys())
    string = ""
    for char in message.upper():
        c = char
        if char in d_keys:
            c = reversed_key[char]
        string += c
    return string


def read_keyfile(file_dir: str):
    global cipher_key
    letters_remaining_keys = string.ascii_uppercase
    letters_remaining_vals = string.ascii_uppercase
    new_key = []
    with open(file_dir, 'r') as f:
        for line in f.readlines():
            if line[0] not in letters_remaining_keys or line[1] != '=' or line[2] not in letters_remaining_vals:
                raise Exception("Invalid cipher - please generate a default keyfile and look at it to see how the cipher should be structured.")
            letters_remaining_keys = letters_remaining_keys.replace(line[0], "")
            letters_remaining_vals = letters_remaining_vals.replace(line[2], "")
            new_key.append((line[0], line[2]))
    cipher_key = dict(new_key)


def write_keyfile(file_dir: str):
    key = []
    for k, v in cipher_key.items():
        key.append(f"{k}={v}\n")
    with open(file_dir, 'w') as f:
        f.writelines(key)


if __name__ == "__main__":
    import argparse
    import sys
    import os
    import textwrap

    DEBUG_MODE = False
    IGNORE_MODE = any(x in sys.argv for x in ["-g", "--generate-default-keyfile", "-p", "--print-tips"])

    parser = argparse.ArgumentParser(
        prog="Cryptogram Encoder/Decoder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Simple program to encode/decode a cryptogram using a substitution cipher. Run this script with the -p/--print-docs flag set for additional information.")
    parser.add_argument(
        "keyfile",
        help="Path to file containing cipher key for encoding/decoding. Ignored if -g or -p flag is set.",
        nargs='?' if IGNORE_MODE else 1)
    parser.add_argument(
        "message",
        help="Text message to encode if plain text, or decode if encrypted. Arg can be either a string (if the -s flag is set) or a text file. Ignored if -g or -p flag is set.",
        nargs='?' if IGNORE_MODE else 1)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument(
        "-g", "--generate-default-keyfile",
        help="Generate and write out a keyfile for the user to modify as needed for the cipher and exit. Cannot be used with the -p, -e or -d flag set.",
        metavar="PATH")
    modes.add_argument(
        "-p", "--print-docs",
        help="Print the documentation for this program and exit. Cannot be used with the -g, -e or -d flag set. Documentation includes usage information and some useful tips about manually decoding a substitution-based cryptogram.",
        action="store_true")
    modes.add_argument(
        "-e", "--encode",
        help="Encode the message with the cipher key. Cannot be used with the -g, -p or -d flag set.",
        action="store_true")
    modes.add_argument(
        "-d", "--decode",
        help="Decode the message with the cipher key. Cannot be used with the -g, -p or -e flag set.",
        action="store_true")
    parser.add_argument(
        "-o", "--outfile",
        help="File path to write out the encoded/decoded message to. If arg is not provided, the message will instead be printed out to the console. Ignored if -g or -p flag is set.",
        metavar="PATH")
    parser.add_argument(
        "-s", "--string-message",
        help="This flag needs to be set if the provided message arg is typed out as a string instead of coming from a text file path. Ignored if -g or -p flag is set. Note: to prevent accidentally invoking terminal features when typing a message into the arg (such as using '!' which will use your history entries), please wrap your message in SINGLE quotes and properly escape apostrophes (\\') if needed.",
        action="store_true")
    parser.add_argument(
        "-i", "--interactive-mode",
        help="Start in interactive mode. Ignored if -g or -p flag is set. Interactive mode allows the user to modify the provided cipher keyfile against the provided message in order to manually encode or decode the message in realtime.",
        action="store_true")
    if DEBUG_MODE:
        args = parser.parse_args(["-e", "-s", "cipher.txt", "hello"])
    else:
        args = parser.parse_args()

    if args.print_docs:
        print(__doc__)
        parser.exit()

    if args.generate_default_keyfile:
        key_dir = args.generate_default_keyfile
        print(f"Generating a default cipher keyfile at '{key_dir}'\n...")
        write_keyfile(key_dir)
        print("Done.")
        parser.exit()

    read_keyfile(args.keyfile[0])
    if args.string_message:
        msg = args.message[0]
    else:
        try:
            with open(args.message[0], 'r') as f:
                msg = f.read()
        except FileNotFoundError:
            raise ValueError("If this is a typed out message, you will need to set the '-s' flag to handle strings instead of files.")

    def coded_msg():
        if args.encode:
            return encode(cipher_key, msg)
        if args.decode:
            return decode(cipher_key, msg)

    if args.interactive_mode:
        def clear():
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        old_cipher = dict(cipher_key)
        while True:
            clear()
            print("Interactive Mode - type in a letter followed by the letter you want to replace it with then press enter. Example: to change all A's to F's, type 'af' into the prompt. For comparison, the original message is on each of the bottom lines and the changed message is on top.\n\n")
            print("Message:\n\n")
            top_words = textwrap.wrap(coded_msg(), width=75)
            bottom_words = textwrap.wrap(msg.upper(), width=75)
            for (t, b) in zip(top_words, bottom_words):
                print(t)
                print(b, '\n\n', sep='')
            if args.decode:
                reversed_ciph_text = sorted([f" {v}={k} |" for k, v in cipher_key.items()])
                ciph_text = [text+("\n|" if i % 10 == 0 else '') for i, text in enumerate(reversed_ciph_text, 1)]
            else:
                ciph_text = [f" {k}={v} |"+("\n|" if i % 10 == 0 else "") for i, (k, v) in enumerate(cipher_key.items(), 1)]
            print("Cipher:\n\n", '|', *ciph_text, '\n\n', sep='')
            usr = input("Change letters here (or enter '0' to quit or 'reset' to reset cipher) >").strip().upper()
            if usr == '0':
                break
            if usr == "RESET":
                cipher_key = dict(old_cipher)
            if len(usr) == 2 and usr[0] in string.ascii_uppercase and usr[1] in string.ascii_uppercase:
                y, z = 1, 0
                if args.decode:
                    y, z = 0, 1
                other = [x for x in cipher_key if cipher_key[x] == usr[y]][0]
                cipher_key[usr[z]], cipher_key[other] = cipher_key[other], cipher_key[usr[z]]
        if old_cipher != cipher_key:
            while True:
                clear()
                usr = input("Overwrite keyfile with modified cipher? (Y/N)\n\n>").strip().upper()
                if usr in ['Y', 'YES']:
                    write_keyfile(args.keyfile[0])
                    break
                if usr in ['N', 'NO']:
                    break
        clear()

    if args.outfile:
        with open(args.outfile, 'w') as f:
            f.write(coded_msg())
        print(f"Message written out to '{args.outfile}'\n")
    else:
        print("Message:\n\n")
        print(coded_msg(), "\n\n")
