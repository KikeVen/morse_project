""" By calling morse_this(), the module takes a string argument
and returns the morse code equivalent"""

morse_dictionary = {
    'a' : '.-',
    'b' : '-...',
    'c' : '-.-.',
    'd' : '-..',
    'e' : '.',
    'f' : '..-.',
    'g' : '--.',
    'h' : '....',
    'i' : '..',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm' : '--',
    'n' : '-.',
    'o' : '---',
    'p' : '.--.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...-',
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    'z' : '--..',
    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '.' : '.-.-.-',
    ',' : '--..--',
    '?' : '..--..',
    '!' : '-.-.--',
    '(' : '-.--.',
    ')' : '-.--.-',
    ':' : '---...',
    ';' : '-.-.-.',
    '=' : '-...-',
    '+' : '.-.-.',
    '/' : '-..-.',
    " " : '/',
    '-' : '-....-',
    '_' : '..--.-',
    '$' : '...-..-',
    '@' : '.--.-.',
    '"' : '.-..-.',
    "'" : '.----.',
}

def morse_this(text_message):
    """It takes a text string and compares each character to every key in the morse_dictionary,
    if the morse_key is found in the text string, it adds it corresponding value to a list.
    Then that list i turned into a string with the .join() method
    """
    return' '.join([morse_dictionary[morse_key] for morse_key in text_message.lower()
                    if morse_key in morse_dictionary])

if __name__ == '__main__':
    my_message = "Sos"
    my_separator = '_' * 53
    morse_message = morse_this(my_message)
    print(my_separator)
    print()
    print('You wrote:        ', my_message)
    print('The morse code:   ', morse_message)
    print(my_separator)
    