# Modular programming tutorial

## This repository host all the files in the Morse Code tutorial.

This repository is to support the video and written morse code tutorials:
* [defcodeblog](https://wp.me/p8k2yu-4)
* [defCode YouTube](https://www.youtube.com/channel/UCUkbK6jMUr05WKzGQ0IzpBg/)

How to design and program a morse code module and integrate it into other scripts to illustrate modular programming. `morsepi.py` module can be leverage by other applications, such as:

* A terminal UI
* Voice interface
* Web interface
* Raspberry pi GPIO integration
* Possible Alexa integration

File name | Location | Description
---------|----------|---------
 morsepi.py | root | primary morse code module
 import_morsepi.py | root | script imports morsepi for testing
 morse_logic.png | media | script logic info-graphic

---
---

## The `morsepi.py` module has the following programming logic:
The module will have a morse code dictionary with the alphabet, numbers and characters with each character's corresponding morse code. The string will be contained in a variable, it will turn into lower case characters and then reassign to the same variable. A loop will iterate through each character in the message, and compare to every key in the dictionary, if the character matches a key, then a list will be appended with the corresponding morse code, this list will have to be converted into a single string for further use.

![Logic diagram](media/morse_logic.png)

---

## Python String foramt()
reference: https://www.programiz.com/python-programming/methods/string/format