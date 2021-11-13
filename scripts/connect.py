#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
#
#buttonPinST=1
#buttonPinTS=2
#buttonPinT=3
#
#GPIO.setup(buttonPinST, buttonPinTS, buttonPinT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
#while True:
#    buttonState1= GPIO.input(buttonPinST)
#    buttonState2= GPIO.input(buttonPinTS)
#    buttonState3= GPIO.input(buttonPinT)
#    if buttonState1 ==True:
#        speech_to_text.speechRecognition()
#    if buttonState2 ==True:
#        text_to_speech.textSpeech()
#    if buttonState3 ==True:
#        deepl_interfacing.translate()
#    else:
#        GPIO.output(GPIO.HIGH)

        
#calling other functions from other files to connect everything 

#calling speech to text function 
#happens when microphone button is pushed


from gpiozero import Button
import pyttsx3 as tts
import requests;
import json;
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import speech_recognition as sr
from os import path

from speech_to_text import speechRecognition
from text_to_speech import textSpeech
from deepl_interfacing import translate
from ocr import OCR



buttonTts = Button(4)
buttonStt = Button(18)
buttonTranslate = Button(24)
buttonOCR = Button(20)

if (buttonTts.is_pressed):
    speech_to_text.speechRecognition()
    #speechRecognition()
elif (buttonStt.is_pressed):
    text_to_speech.textSpeech()
    #textSpeech()
elif (buttonTranslate.is_pressed):
    deepl_interfacing.translate()
    #translate()
elif (buttonOCR.is_pressed):
    ocr.OCR()
    #OCR()













 






