# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:36:33 2018

@author: vansh
"""


import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray, 1.3, 5)
    print(ret)                                            
    print(img)
    for (x,y,h,w) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
        
    cv2.imshow("img",img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()    
cv2.destroyAllWindows()
                                        
