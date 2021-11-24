from PIL import Image
import pytesseract
# import argparse
import cv2
import os
import time
import picamera
import numpy as np

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.framerate = 24
    time.sleep(2)
    output = np.empty((240, 320, 3), dtype=np.uint8)
    camera.capture(output, 'rgb')

def ocr(path):
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # write the grayscale image to disk as a temporary file so we can apply OCR to it
    filename = "{}.jpg".format(os.getpid())
    cv2.imwrite(filename, gray)

    #load the image as PIL/Pillow image, apply OCR, and then delete the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    return text

def ocr_file(path):
    text = ocr(path)

    #writes the result of calling ocr with that path, into the file
    try:
        with open('text.txt', 'w') as file:
            file.write(text)
    #if there is a problem finding the file we're outputting to, tells the user that.
    except FileNotFoundError:
        print('There was an error with locating the output file.  Please try again later.')


#test this on a computer with all of the prerequisites
ocr_file("images/avril.jpg")