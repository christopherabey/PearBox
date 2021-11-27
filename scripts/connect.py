#imports from functions and files that will be called
from gpiozero import Button
import pyttsx3 as tts
import requests
import json
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import speech_recognition as sr
from os import path
from picamera import PiCamera
from time import sleep

#importing the functions from the files
from speech_to_text import speechRecognitionToFile
from text_to_speech import tts_from_file
from deepl_interfacing import translate_file
from ocr import ocr_file

camera = PiCamera()

#setting up the GPIO locations for the buttons on the breadboard
buttonTTS = Button(4)
buttonSTT = Button(5)
buttonTranslate = Button(24)
buttonOCR = Button(20)

#once button is pressed, action is called
while True:

    if (buttonTTS.is_pressed):
        #text_to_speech.textSpeech('This is a test for pearbox audio')
        tts_from_file()
    elif (buttonSTT.is_pressed):
        #speech_to_text.speechRecognition()
        speechRecognitionToFile()
    elif (buttonTranslate.is_pressed):
        #deepl_interfacing.translate()
        translate_file("EN", "FR")

    elif (buttonOCR.is_pressed):
        print("3")
        ocr_file("../images/avril.jpg")













    
 

