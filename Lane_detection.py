# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:51:43 2019

@author: Lenovo
"""

import cv2
import numpy as np

cap=cv2.VideoCapture('Lane.mp4')

while 1:
    _,img=cap.read()
    img=cv2.resize(img,None,fx=0.8,fy=0.8)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    height=img.shape[0]
    width=img.shape[1]
    points=np.array([(0,height),(width/2,height/1.29),(width,height)],np.int32)
    mask=np.zeros((height,width),np.uint8)
    convexhull=cv2.convexHull(points)
    canny=cv2.Canny(gray,220,255)
    cv2.fillConvexPoly(mask,convexhull,255)
    lane_image=cv2.bitwise_and(canny,canny,mask=mask)
    
    lines=cv2.HoughLinesP(lane_image,1,np.pi/180,1)
    for line in lines:
        x,y,w,h=line[0]
        cv2.line(img,(x,y),(w,h),(0,255,0),4)
    
    cv2.imshow('Image',img)
    k=cv2.waitKey(20) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()