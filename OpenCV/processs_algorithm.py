import cv2
import numpy as np
import urllib



#For Testing Purposes Already Recorded Video is taken
cap = cv2.VideoCapture('Video.mov')

def binaryConversion(input):

    """
    Take Input Picture > Convert to Black n White > Resize to small picture >
    Binary Thresholding1 > GaussianBlur > Binary Thresholding 2 > Output
    """

    #Parameters
    thresh1 = 190
    maxValue1 = 255

    scaleFactor = 0.3
    blurRadius = 5

    #Grayscale Conversion
    grayscale = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)

    #Downscaling
    resized = cv2.resize(grayscale,None,fx=scaleFactor, fy=scaleFactor, interpolation = cv2.INTER_CUBIC)

    #Thresholding 1
    _, th1 = cv2.threshold(resized, thresh1, maxValue1, cv2.THRESH_BINARY);

    # cv2.imshow('Input', input)
    # cv2.imshow('Grayscale', grayscale)
    # cv2.imshow('Resized', resized)
    # cv2.imshow('Thresholding1', th1)
    # cv2.imshow('Output', th1)

    return(th1)




while(cap.isOpened()):




    ret, frame = cap.read()

    cv2.imshow("FRAMECONVERTED", binaryConversion(frame))


    # cv2.imwrite("result.jpg", dst)

    # np.savetxt("myfile", array_np, fmt="%d", comments='')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
