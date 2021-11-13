import pyttsx3 as tts
engine = tts.init()
def textSpeech(text):
    engine.say(text)
    engine.runAndWait() 

textSpeech('word')
engine.stop()