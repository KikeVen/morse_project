""" 
Leave for last... It will be easier
"""
# This dictionary has the  morse code for each character of the alphabet
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
    """It takes a text string and iterates each character comparing it to morse_dictionary,
    returning the corresponding morse code"""
    # all the characters in text_message are converted to lower case and re-assigned to text_message
    text_message = text_message.lower()
    # 'morse_code_list' is an empty list that will be appended to hold 
    # the morse values corresponding to the 'text_message' variable
    morse_code_list = []
    # iterate each_character in the input string 'text_message' and
    for each_character in text_message:
        # iterate for each key and value in the morse_dictionary
        for morse_key, morse_values in morse_dictionary.items():
            # if each_character in text_message is equal (==) to the key in morse_dictionary then...
            if each_character == morse_key:
                # append the morse_code_list list with the corresponding morse value from morseDict
                morse_code_list.append(morse_values)
    # In order to remove the extra characters in the list, we need to use the .join() method
    return ' '.join(morse_code_list)

if __name__ == '__main__':
    my_message = 'Kelly'
    my_separator = '__' * 35
    morse_message = morse_this(my_message)
    print(my_separator)
    print()
    print('   You wrote:', my_message)
    print('Your message:', morse_message)
    print(my_separator)
