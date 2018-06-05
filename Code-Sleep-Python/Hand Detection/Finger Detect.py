import numpy as np
import cv2
from math import *
def diffImg(t0, t1, t2):
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)

cap = cv2.VideoCapture(0)
nl,pl=[0,0,0,0,0],[0,0,0,0,0]
jjjj=[0,0,0,0,0]
while(1):
    ret, frame = cap.read()
    crop_frame = frame[0:300, 0:300]
    gray_image = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray_image, 145, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    mask_inv = cv2.erode(mask_inv, None, iterations=1)
    mask_inv = cv2.dilate(mask_inv, None, iterations=1)
    drawing=mask_inv
    ret,thresh = cv2.threshold(mask_inv,127,255,0)
    im2,contours,hierarchy = cv2.findContours(thresh, 1, 2)
    cv2.rectangle(frame, (0, 0), (300, 300), (255,0,0), 2)


    if len (contours)>0:
        max_area=100
        ci=0	
        for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i  
                
            #Largest area contour 			  
        cnts = contours[ci]
        M = cv2.moments(cnts)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.circle(frame,(cX,cY),10,[100,255,255],3)
        hull = cv2.convexHull(cnts)
        hull2 = cv2.convexHull(cnts,returnPoints = False)
        defects = cv2.convexityDefects(cnts,hull2)
        FarDefect = []
        
        try:
          ccc=0
          for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnts[s][0])
            end = tuple(cnts[e][0])
            far = tuple(cnts[f][0])
            dist = sqrt( (start[0] - end[0])**2 + (start[1] - end[1])**2 )
            
            if 1:
                FarDefect.append(far)
                #print end[0]-far[0],far[1]-end[1]
                a=sqrt((far[0]-end[0])**2+ (end[1]-far[1])**2)
                b=sqrt((start[0]-far[0])**2+ (start[1]-far[1])**2)
                c=sqrt((start[1]-end[1])**2+(start[0]-end[0])**2)
                angle=(a**2+b**2-c**2)/(2*a*b)
                angle=acos(angle)
                
                if (angle*180)/(22/7)<90 and dist>10:
                    cv2.line(frame,(cX,cY),end,[125,255,0],1)
                    cv2.line(frame,(cX,cY),end,[125,255,0] ,1)
                    cv2.circle(frame,end,10,[100,255,255],3)
          cv2.line(frame,(cX,cY),end,[125,255,0],1)        
          cv2.circle(frame,end,10,[100,255,255],3)

        except Exception as e:
            pass
        
        cv2.imshow('Dilation',drawing)
    
    frame = cv2.resize(frame, (1366, 765), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('frame',frame)
    
    #cv2.imshow('cropped frame',crop_frame)
    cv2.imshow('grey cropped frame',gray_image)
    cv2.imshow('t',mask)
    cv2.imshow('t2',mask_inv)
    #cv2.imshow('drawing',drawing)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
