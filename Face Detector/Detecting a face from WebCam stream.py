# Face Detector app

import cv2

#loading pre-trained data on frontal faces from OpenCV
trained_face_data = cv2.CascadeClassifier("C:\\Users\\OJASWIN KHAMKAR\\.spyder-py3\\Face Detector\\haarcascade_frontface_default.xml")

#To capture video from Web Cam
webcam = cv2.VideoCapture(0)

#The while loop will keep iterating over the frames
while True:
    successful_frame_read, frame = webcam.read() #reads the current frame
    
    #The images need to be converted into "Greyscale" so that the algorithm becoomes less complicated
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Detect faces
    face_coordinates = trained_face_data.detectMultiScale(gray_img)
    
    #Drawing a rectangle around the face
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)   #Wait key pauses the execution of the program

    if key == 81 or key == 113:  #ASCII characters for letter 'q'
        break

webcam.release() #releases the VideoCapture object




print("Code Completed")
