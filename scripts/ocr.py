from PIL import Image
import pytesseract
# import argparse
import cv2
import os


#python3 ocr.py --image ../images/apple.png
def ocr(path):
    print(os.getcwd())
    # argument parse and parse the arguments
    #ap = argparse.ArgumentParser()
    # args = vars(ap.parse_args())
    # load example image and convert to grayscale
    # image = cv2.imread(args["image"])
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # check if we have to apply thresholding to preprocess the image
    # if args["preprocess"] == "thresh":
    #     gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # # make a check to see if median blurring should be done to remove noise
    # elif args["preprocess"] == "blur":
        #gray = cv2.medianBlur(gray, 3)

    # write the grayscale image to disk as a temporary file so we can apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    #load the image as PIL/Pillow image, apply OCR, and then delete the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)

    #show the output images
    cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    cv2.waitKey(0)


ocr("images/apple.png")