"""
Import morse_pi and write an ui using the input() and print() methods. Encapsulate in while loop
and add a condition to escape the loop
"""
import morsepi

print()
DYNAMIC_STRING_TEMPLATE = "{:{fill}{align}{width}}"
print(DYNAMIC_STRING_TEMPLATE.format('~ Welcome to morsepi module ~', fill='*', align='^', width=54))
print()

while True:
    TEXT_STRING = input('Please type your message: ')
    if TEXT_STRING.strip() == 'Q!':
        break
    else:
        MORSED_TEXT = morsepi.morse_this(TEXT_STRING)
        print(MORSED_TEXT)
        print()

print()
print('Thank you for using morsepi!')
print()