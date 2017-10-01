import cv2
import numpy as np

#Print Numpy Array Full Length without ...
np.set_printoptions(threshold=np.nan)

import urllib
import imutils
import tkinter as tk
import urllib.request
import os

#Script Parameters
streamImgURL = "192.168.1.102:8080/live.jpg"
remoteESPURL = "192.168.1.104"
driveTime = "200"
trainingDataOutput="trainingData/svmlight.txt"


def moveVehicle(direction):
    req = urllib.request.Request("http://" + remoteESPURL + "/" + direction + "?duration=" + driveTime)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
       return(str(the_page))

def binaryConversion(input, maxValue1):

    thresh1 = 190
    # maxValue1 = 255
    scaleFactor = 0.3
    blurRadius = 5

    grayscale = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(grayscale,None,fx=scaleFactor, fy=scaleFactor, interpolation = cv2.INTER_CUBIC)
    _, processed = cv2.threshold(resized, thresh1, maxValue1, cv2.THRESH_BINARY);

    return(processed)

def appendToSVMLIGHT(x):

    flatImage = currentFrame.flatten()

    lineString = ""
    lineString+=str(x) + " "

    for index,pixel in enumerate(flatImage, start=0):
        lineString+= str(index) + ":"
        lineString+=str(pixel) + " "

    lineString+=os.linesep

    with open(trainingDataOutput, "a") as myfile:
        myfile.write(lineString)


def key(event):
    """
    Steering: (0=LEFT;1=FORWARD;2=RIGHT)
    """
    keyID = event.char

    if keyID == "w" or keyID == "\uf700":
        print("Moving Forward")
        print("Remote Response: " + moveVehicle("forward"))
        appendToSVMLIGHT(1)

    if keyID == "a" or keyID == "\uf702":
        print("Moving Left")
        print("Remote Response: " + moveVehicle("left"))
        appendToSVMLIGHT(0)

    if keyID == "s" or keyID == "\uf701":
        print("Moving Backward")
        print("Remote Response: " + moveVehicle("backward"))

    if keyID == "d" or keyID == "\uf703":
        print("Moving Right")
        print("Remote Response: " + moveVehicle("right"))
        appendToSVMLIGHT(2)

root = tk.Tk()
frame = tk.Frame(root, width="100", height="100")
frame.bind("<Key>", key)
frame.pack()
frame.focus_set()

while True:

    root.update_idletasks()
    root.update()

    #Video Stream
    stream = cv2.VideoCapture("http://" + streamImgURL)
    ret,frame = stream.read()

    #Show Driver's View
    drivers_view = cv2.resize(frame,None,fx=3, fy=3, interpolation = cv2.INTER_CUBIC)
    cv2.imshow("Driver's View", drivers_view)

    #Show NeuralNetwork Training Input
    cv2.imshow("Processed Binary Image", binaryConversion(drivers_view, 255))

    global currentFrame
    currentFrame = binaryConversion(frame, 1)

cap.release()
cv2.destroyAllWindows
