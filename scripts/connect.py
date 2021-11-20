#imports from functions and files that will be called
from gpiozero import Button
import pyttsx3 as tts
import requests
import json
from PIL import Image
import pytesseract
import argparse
import os
import speech_recognition as sr
from os import path

#importing the functions from the files
from speech_to_text import speechRecognition
from text_to_speech import speak
from deepl_interfacing import translate
from ocr import OCR


#setting up the GPIO locations for the buttons on the breadboard
buttonTTS = Button(4)
buttonSTT = Button(18)
buttonTranslate = Button(24)
buttonOCR = Button(20)

#once button is pressed, action is called
while True:

    if (buttonTTS.is_pressed):
        #text_to_speech.textSpeech('This is a test for pearbox audio')
        speak('This is a test for pearbox audio')
    elif (buttonSTT.is_pressed):
        #speech_to_text.speechRecognition()
        speechRecognition()
    elif (buttonTranslate.is_pressed):
        #deepl_interfacing.translate()
        translate('Hello World')
    elif (buttonOCR.is_pressed):
        #ocr.OCR()
        OCR()













 






