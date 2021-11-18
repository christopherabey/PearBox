import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

buttonPinST=1
buttonPinTS=2
buttonPinT=3

GPIO.setup(buttonPinST, buttonPinTS, buttonPinT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    buttonState1= GPIO.input(buttonPinST)
    buttonState2= GPIO.input(buttonPinTS)
    buttonState3= GPIO.input(buttonPinT)
    if buttonState1 ==True:
        speech_to_text.speechRecognition()
    if buttonState2 ==True:
        text_to_speech.textSpeech()
    if buttonState3 ==True:
        deepl_interfacing.translate()
    else:
        GPIO.output(GPIO.HIGH)

        
#calling other functions from other files to connect everything 

#calling speech to text function 
#happens when microphone button is pushed




 






