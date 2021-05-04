#I honestly can't think of anything funny to say.

__code ={
        'A':".-",
        'B':"-...",
        'C':"-.-.",
        'D':"-..",
        'E':".",
        'F':"..-.",
        'G':"--.",
        'H':"....",
        'I':"..",
        'J':".---",
        'K':"-.-",
        'L':".-..",
        'M':"--",
        'N':"-.",
        'O':"---",
        'P':".--.",
        'Q':"--.-",
        'R':".-.",
        'S':"...",
        'T':"-",
        'U':"..-",
        'V':"...-",
        'W':".--",
        'X':"-..-",
        'Y':"-.--",
        'Z':"--..",
        '0':"-----",
        '1':".----",
        '2':"..---",
        '3':"...--",
        '4':"....-",
        '5':".....",
        '6':"-....",
        '7':"--...",
        '8':"---..",
        '9':"----.",
        '.':".-.-.-",
        ',':"--..--",
        '?':"..-..",
        "'":".----.",
        '!':"-.-.--",
        '/':"-..-.",
        '(':"-.--.",
        ')':"-.--.-",
        '&':".-...",
        ':':"---...",
        ';':"-.-.-.",
        '=':"-...-",
        '+':".-.-.",
        '-':"-....-",
        '_':"..--.-",
        '"':".-..-.",
        '$':"...-..-",
        '@':".--.-.",
        ' ':"/",
        '<err>':"*"
        }

def morse_encode(message:str):
    """Encode a text message into morse code.\n
    All ASCII (32-126) chars are accepted with the exceptions of: ~ ` # % ^ * { } [ ] < > \\ |\n
    Spaces are encoded as / and illegal chars are encoded as * .
    """
    string = ""
    for c in message.upper():
        if c in __code.keys(): string = string + __code.get(c,"") + " "
        else: string = string + __code["<err>"] + " "
    return string.strip()

def morse_decode(message:str):
    """Decode a morse message. Message must contain (with no spacing between chars) periods or hyphens(minus symbol) or forward slashes/astericks. Any other chars - including incorrect morse code - will be stripped out from the decoded message'. A single space must be used to separate each letter.\n
    All decoded alpha chars will be capitalized. Any forward slashes will be interpreted as a single space, and astericks will be decoded as ' \<err\> ' to mark an illegal character in the message.
    """
    chars,string = message.strip().split(" "),""
    for c in chars:
        for k,v in __code.items():
            if c == v:
                string = string + k
                break
    return string.strip()