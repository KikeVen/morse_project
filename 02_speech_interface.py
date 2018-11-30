import time
import pyttsx3
import morsepi as mp
import witai
import speech_recognition as sr

#-------------------- Keys and constants -------------------------------#

WIT_AI_KEY = "YOUR WIT.AI KEY HERE"
LADY_VOICE = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
r = sr.Recognizer()
MICROPHONE = sr.Microphone()

#------------------- define text to speech function ---------------------#

def broadcast(message, mode):
    """ converts message string to speech"""
    engine = pyttsx3.init()
    if mode == 0:
        print(message)
        engine.say(message)
    elif mode == 1:
        print(message)
    else: 
        engine.say(message)
    engine.runAndWait()

#------------------- invoke Context Manger with/as ---------------------#

with MICROPHONE as source:
    print()
    broadcast('executing a one second calibration for ambient noise...', 0)
    r.adjust_for_ambient_noise(source, duration=1)
    broadcast('almost done...', 0)
    time.sleep(0.5)
    broadcast('Say something!', 0)
    audio = r.listen(source)

#------------------- connect to wit.ai & send audio ---------------------#

def wit_me():
    """ Connects to wit.ai server, sends the audio and wit key to the server for a response,
    the server returns a string or an exception"""
    print()
    broadcast('sending audio to Wit.ai, please wait ...', 1)
    try:
        return r.recognize_wit(audio, key=WIT_AI_KEY)
    except sr.UnknownValueError:
        broadcast("Wit.ai could not understand audio", 0)
    except sr.RequestError as e:
        broadcast("Could not request results from Wit.ai service; {0}".format(e), 0)

#--------------------- says the returnned morse code  ---------------------#

def sing_it_man(sing_this):
    """Says the returned morse code by morsepi """
    sing_engine = pyttsx3.init()
    rate = sing_engine.getProperty('rate')
    sing_engine.setProperty('rate', rate+10)
    sing_engine.setProperty('voice', LADY_VOICE)
    sing_string = []
    for x in sing_this:
        if x == '.': 
            sing_string.append('dot ')
        if x == '-':
            sing_string.append('dash ')
        if x == ' ':
            sing_string.append(' ')
        if x == '/':
            sing_string.append('space ')
        else:
            sing_string.append('')
    broadcast(''.join(sing_string), 0)
    sing_engine.runAndWait()

 #--------------------- run as main example  ---------------------#

if __name__ == '__main__':
    WHAT_YOU_SAID = wit_me()
    MORSED = mp.morse_this(WHAT_YOU_SAID)
    print()
    broadcast("Wit thinks you said: " + WHAT_YOU_SAID, 0)
    print()
    print('This is your message in morse code: ' + MORSED)
    broadcast('This is your message in morse code:', 3)
    print()
    broadcast('Cindy will now drop some rimes for you ', 0)
    print()
    sing_it_man(MORSED)
    print()
    broadcast('Thank you for using morse pi ', 0)
    print()
