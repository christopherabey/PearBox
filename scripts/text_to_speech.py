import pyttsx3 as tts
engine = tts.init()
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait() 

text_to_speech('word')
engine.stop()