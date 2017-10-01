import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib
import imutils
import os

FILE_OUTPUT = 'output.avi'

# Checks and deletes the output file
# You cant have a existing file or it will through an error
if os.path.isfile(FILE_OUTPUT):
    os.remove(FILE_OUTPUT)

cap = cv2.VideoCapture("http://192.168.1.102:8080/live.jpg")
ret, frame = cap.read()

height, width, _ = frame.shape


fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (height,width)) #inversed on purpose

cap.release()



while True:
    cap = cv2.VideoCapture("http://192.168.1.102:8080/live.jpg")
    ret, frame = cap.read()


    rotated = imutils.rotate_bound(frame, -90)

    edges = cv2.Canny(rotated,80,1000)

    out.write(rotated)
    cv2.imshow('Stream', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
