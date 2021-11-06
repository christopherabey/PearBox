#calling other functions from other files to connect everything 

#calling speech to text function 
#happens when microphone button is pushed
import speech_to_text

#from speech_to_text import speechRecognition()
speech_to_text.speechRecognition()


#calling text to speech 

#calling translator function
import deepl_interfacing
#from deepl_interfacing import translate(text) 
deepl_interfacing.translate() 




