import pyttsx3 as tts, time
def text_to_speech(text):
    engine = tts.init()
    engine.setProperty('rate', 100)
    engine.say(text)
    engine.runAndWait() 
    engine.stop()


