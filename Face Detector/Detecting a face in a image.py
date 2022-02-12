# Face Detector app

import cv2
from random import randrange

#loading pre-trained data on frontal faces from OpenCV
trained_face_data = cv2.CascadeClassifier("C:\\Users\\OJASWIN KHAMKAR\\.spyder-py3\\Face Detector\\haarcascade_frontface_default.xml")

#Choosing an photo for the algorithm to detect a face
img = cv2.imread('ben1.jpg')

#The images need to be converted into "Greyscale" so that the algorithm becoomes less complicated
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect faces
face_coordinates = trained_face_data.detectMultiScale(gray_img)

#Drawing a rectangle around the face
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)

cv2.imshow('Face Detector', img)
cv2.waitKey()   #Wait key pauses the execution of the program

print("Code Completed")
