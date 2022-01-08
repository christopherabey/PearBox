# PearBox

### Description

---


Our idea is to make a toolbox that has various devices to aid people that are visually or audibly impaired. Our first device is a camera that recognizes text and says it aloud. We house a *Raspberry Pi Camera Module* on a wooden stick tube that is connected to the box. The second device is a microphone that converts sound into text on a document. It is housed in a similar way to the camera. Some additional features are an internet-connected language converter and sending converted text to a document to be accessed later.


### Inspiration:

---

We were initially motivated to ease reading for the visually impaired. We wanted to create a tool that allowed them to be able to read when Braille was not available or they are in the process of learning it. While finalizing our idea, we noticed how it could be helpful for everyone! These can include people who wanted to instantly save text on a text document, people who want text to be read to them and when people want to save text from an audio and those with Dyslexia.

### How we built it:

---

##### Hardware:
    The box that holds the tools will include most of the hardware components (**battery, speaker, Raspberry Pi, screen**) for portability. The speaker, Raspberry Pi and battery will be in the box, while the screen is placed on the outside of the box. A breadboard is placed on the other side of the box to connect the buttons to the Raspberry Pi. 

###### Software:
    Listed under "Setup" are the API libraries that we implemented in the project. We created a function that connect all of the files together and that recognizes when a button is pushed, so an action will follow, such as Speech-to-Text.

### Challenges we ran into:

---

Downloading all of the required *API libraries* was a challenge because we had to research which ones were appropriate for our intended uses. Also, we had trouble setting up the hardware. 


### What we learned:

---

Majority of us never worked on a *hardware-based* project before, so we had to research and learn. This includes learning about the Raspberry Pi and the breadboard with the GPIO location numbers. Also, the members that did the **woodworking** did not have enough sufficient experience in that area. They had to learn quickly and how to solve problems on the go.





---

### Setup:

##### Install Python 3

> `pip3 install requests`

> `pip3 install SpeechRecognition`

> `pip3 install pyttsx3`

> `pip3 install pyaudio`

> `pip3 install opencv-contrib-python`

> `pip3 install pillow`

> `pip3 install pytesseract`

> `pip3 install evdev`

> `pip3 install python3-gpiozero`

### How to Use

---
To turn on the PearBox, plug the charger into the Raspberry Pi. At this point, you have to plug in a keyboard and turn on the file and you can press the buttons to use the features:

1) This button is for the text to speech function aka our "OCR" function.

2) This button is for the translation.

3) This button is for Speech-to-Text. 

4) This button is for Text-to-Speech.

---

Credit:

|Name|Email|
|----|-----|
|Brandon Gartner|bjgartner@uwaterloo.ca|,
|Chris Abey|cabey@uwaterloo.ca|,
|Kushal Mujral|kmujral@uwaterloo.ca|,
|Avril Chen|a366chen@uwaterloo.ca|,
|Vaishnavi Ratnasabapathy|vratnasa@uwaterloo.ca|


MIT License

Copyright (c) 2021, Brandon Gartner, Chris Abey, Avril Chen, Vaishnavi Ratnasabapathy, Kushal Mujral

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
