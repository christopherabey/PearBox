import pyttsx3 as tts, time
def speak(text):
    engine = tts.init()
    engine.setProperty('rate', 100)
    engine.say(text)
    engine.runAndWait() 
    engine.stop()

def tts_from_file():
    text = 'empty'

    #takes the text from text.txt, reads it, translates it, and saves it back to the file
    try:
        with open('../text.txt', 'r') as file:
            text = file.read()
            speak(text)
    
    #if there is a problem finding the file we're reading from, tells the user that.
    except FileNotFoundError:
        print('There was an error with locating the input file.  Please try again later.')
