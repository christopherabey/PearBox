import pyttsx3 as tts, time
def speak(text):
    engine = tts.init()
    engine.setProperty('rate', 100)
    engine.say(text)
    engine.runAndWait() 
    engine.stop()


