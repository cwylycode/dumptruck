# I honestly can't think of anything witty to say here.

_code = {
    'A': ".-",
    'B': "-...",
    'C': "-.-.",
    'D': "-..",
    'E': ".",
    'F': "..-.",
    'G': "--.",
    'H': "....",
    'I': "..",
    'J': ".---",
    'K': "-.-",
    'L': ".-..",
    'M': "--",
    'N': "-.",
    'O': "---",
    'P': ".--.",
    'Q': "--.-",
    'R': ".-.",
    'S': "...",
    'T': "-",
    'U': "..-",
    'V': "...-",
    'W': ".--",
    'X': "-..-",
    'Y': "-.--",
    'Z': "--..",
    '0': "-----",
    '1': ".----",
    '2': "..---",
    '3': "...--",
    '4': "....-",
    '5': ".....",
    '6': "-....",
    '7': "--...",
    '8': "---..",
    '9': "----.",
    '.': ".-.-.-",
    ',': "--..--",
    '?': "..-..",
    "'": ".----.",
    '!': "-.-.--",
    '/': "-..-.",
    '(': "-.--.",
    ')': "-.--.-",
    '&': ".-...",
    ':': "---...",
    ';': "-.-.-.",
    '=': "-...-",
    '+': ".-.-.",
    '-': "-....-",
    '_': "..--.-",
    '"': ".-..-.",
    '$': "...-..-",
    '@': ".--.-.",
    ' ': "/",
    '<err>': "*"
}


def morse_encode(message: str):
    """Encode a text message into morse code.

    All ASCII (32-126) characters are accepted with the exceptions of: ~ ` # % ^ * { } [ ] < > \\ |

    Spaces are encoded as / and illegal characters are encoded as * ."""
    string = ""
    for c in message.upper():
        if c in _code.keys():
            string = string + _code.get(c, "") + " "
        else:
            string = string + _code["<err>"] + " "
    return string.strip()


def morse_decode(message: str):
    """Decode a morse message.

    Message must contain (with no spacing between characters) periods or hyphens(minus symbol) or forward slashes/astericks. Any other characters - including incorrect morse code - will be stripped out from the decoded message. A single space must be used to separate each character in the message.

    All decoded alphabet characters will be capitalized, any forward slashes will be interpreted as a single space, and astericks will be decoded as '<err>' to mark an illegal character in the message."""
    chars, string = message.strip().split(" "), ""
    for c in chars:
        for k, v in _code.items():
            if c == v:
                string = string + k
                break
    return string.strip()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="Morse Code - Encoder/Decoder",
        description="Encode or decode a message in Morse code. Select an encode or decode option flag and, for the message argument, either provide a message string (with the '-s' flag set), or a text file path containing a message. The encoded/decoded message can then be written out to a file ('-o' flag set), or the console screen.")
    parser.add_argument(
        "message",
        help="Text message to encode if plain text, or decode if Morse. Arg can be either a string (if the -s flag is set) or a text file.")
    parser.add_argument(
        "-s", "--string-message",
        help="This flag needs to be set if the provided message arg is typed out as a string instead of coming from a text file path. Note: to prevent accidentally invoking terminal features when typing a message into the arg (such as using '!' which will use your history entries), please wrap your message in SINGLE quotes and properly escape apostrophes (\\') if needed.",
        action="store_true")
    parser.add_argument(
        "-o", "--outfile",
        help="File path to write out the encoded/decoded message to. If arg is not provided, the message will instead be printed out to the console.",
        metavar="PATH")
    code_mode = parser.add_mutually_exclusive_group(required=True)
    code_mode.add_argument(
        "-e", "--encode",
        help="Encode a text message into morse code. All ASCII (32-126) characters are accepted with the following exceptions: '~ ` # % ^ * { } [ ] < > \\ |'. Spaces are encoded as / and illegal characters are encoded as * .",
        action="store_true")
    code_mode.add_argument(
        "-d", "--decode",
        help="Decode a morse message. Message must contain (with no spacing between characters) periods or hyphens(minus symbol) or forward slashes/astericks. Any other characters - including incorrect morse code - will be stripped out from the decoded message. A single space must be used to separate each character in the message. All decoded alphabet characters will be capitalized, any forward slashes will be interpreted as a single space, and astericks will be decoded as '<err>' to mark an illegal character in the message.",
        action="store_true")
    args = parser.parse_args()

    if args.string_message:
        msg = args.message
    else:
        try:
            with open(args.message, 'r') as f:
                msg = f.read()
        except FileNotFoundError:
            raise ValueError("If this is a typed out message, you will need to set the '-s' flag to handle strings instead of files.")

    if args.encode:
        final = morse_encode(msg)
    if args.decode:
        final = morse_decode(msg)

    if args.outfile:
        with open(args.outfile, 'w') as f:
            f.write(final)
        print(f"\nMessage written out to '{args.outfile}'\n")
    else:
        print("Message:\n")
        print(final)
