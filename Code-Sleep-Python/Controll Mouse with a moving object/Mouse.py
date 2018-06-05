import cv2
import numpy as np

import win32api
global cam
cam = cv2.VideoCapture(0)

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)
def main():
    global cam
    t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    while True:
          ret, frame = cam.read()
          hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
          lower_hsv = np.array([0, 130, 147])
          higher_hsv = np.array([22, 255, 215])
          mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
          mask = cv2.erode(mask, None, iterations=5)
          mask = cv2.dilate(mask, None, iterations=5)
          cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
              cv2.CHAIN_APPROX_SIMPLE)
          cnt=cnts[0]
          if len(cnts)>0:
              x,y,w,h = cv2.boundingRect(cnt)
              xx,yy=(2*x+w)/2 , (2*y+h)/2
              if xx>0 and xx<1366 and yy>0 and yy<768:
                  win32api.SetCursorPos((1366-(xx*3),yy*3))


          (cnts) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
          t_minus = t
          t = t_plus
          t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
          cv2.imshow("Mouse", frame)
          key = cv2.waitKey(10)
          if key == 27:
            cv2.destroyWindow(winName)
            break
main()
        
        
