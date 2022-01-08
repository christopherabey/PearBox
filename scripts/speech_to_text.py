import pyaudio
import speech_recognition as sr

def speechRecognition():

    try:
        #access recognizer
        r = sr.Recognizer()

        with sr.Microphone() as source:
            # read the audio data from the default microphone
            audio_data = r.record(source, duration=5)
            print("Recognizing...")
            # convert speech to text
            text = r.recognize_google(audio_data)
            print(text)
            return text
    except:
        print("There was an error with the speech recognition. Please try again later.")

def speechRecognitionToFile():

    #listens to the microphone, saves the input from the mic into our text file
    try:
        text = speechRecognition()
        with open('../text.txt', 'w') as file:

            file.write(text)
    #if there is a problem finding the file we're outputting to, tells the user that.
    except FileNotFoundError:
        print('There was an error with locating the output file.  Please try again later.')