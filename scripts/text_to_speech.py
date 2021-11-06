import pyttsx3 as tts, time
#engine = tts.init()
def text_to_speech(text):
    engine = tts.init()
    engine.setProperty('rate', 125)
    engine.say(text)
    engine.runAndWait() 
    engine.stop()

text_to_speech('word')
#engine.stop()