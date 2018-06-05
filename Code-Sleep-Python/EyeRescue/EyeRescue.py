# -*- coding: utf-8 -*-

from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import notify2
from playsound import playsound

notify2.init('Eye Rest Notifier')

EyeRestNeedTime=1#minutes
WalkNeedTime=120


def eye_aspect_ratio(eye):
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])
	C = dist.euclidean(eye[0], eye[3])
	ear = (A + B) / (2.0 * C)
	return ear

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor",
	help="path to facial landmark predictor")
ap.add_argument("-v", "--video", type=str, default="",
	help="path to input video file")
args = vars(ap.parse_args())
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3
COUNTER = 0
TOTAL = 0
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
print("[INFO] starting video stream thread...")
vs = VideoStream(src=0).start()
fileStream = False
time.sleep(1.0)
eyeCloseTime=0
working=0
workTime=0
rtime=0
restNeed=time.time()
walkNeed=time.time()
noti=0
ss=0
while True:
	if fileStream and not vs.more():
		break
	frame = vs.read()
	frame = imutils.resize(frame, width=450)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	rects = detector(gray, 0)

        drtime=time.time()-rtime if rtime else 0
	if (drtime)>60*10:
                working=0
                workTime=0
                try:
                        n.close()
                        noti =0
                except:
                        pass

	if not rects:
                if not rtime:
                        rtime=time.time()
                else:
                        drtime=time.time()-rtime if rtime else 0
                        cv2.putText(frame, "Resting Time: {:.2f}".format(drtime), (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        if drtime>20:
                                restNeed=time.time()
	for rect in rects:
                rtime=0
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)
		ear = (leftEAR + rightEAR) / 2.0
		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
                ectime=time.time()-eyeCloseTime if eyeCloseTime else 0
                working=1
                
                if ectime>20:
                        restNeed=time.time()
                        try:
                                
                                n.close()
                                ectime=0
                                eyeCloseTime=time.time()
                                playsound('2.mp3')

                                noti =0
                        except Exception as e:
                                print e
                                        
                if not workTime:
                        workTime=time.time()
                wtime=time.time()-workTime if workTime!=0 else 0
                if wtime>EyeRestNeedTime and (time.time()-restNeed>EyeRestNeedTime*60):
                        if 1:
                                n = notify2.Notification('You Need rest!!!','Your Eyes need some rest.Please Close your eyes for atleast 20 seconds',"notification-message-im")
                                n.show()
                                playsound('1.mp3')
                                noti =1
                        restNeed=time.time()

                        cv2.putText(frame, "You Need rest!!!  ", (100, 100),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

		if ear < EYE_AR_THRESH-0.01:

                        if not eyeCloseTime:
                                eyeCloseTime=time.time()
                        else:
                                pass
                        COUNTER += 1

		else:


                        eyeCloseTime=0
			if COUNTER >= EYE_AR_CONSEC_FRAMES:
				TOTAL += 1

			COUNTER = 0
                if wtime>WalkNeedTime*60 and not noti:
                        n = notify2.Notification('You Need walk!!!','You are using computer for more than 2 hours.Take a 10-minute bathroom break , even if you don’t have to go',"notification-message-im")
                        n.show()
                        playsound('3.mp3')

                        noti =1
                        
		cv2.putText(frame, "Working Time: {:.2f}".format(wtime), (10, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		#cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30),
		#	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		#cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
		#	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		cv2.putText(frame, "Eye Close: {:.2f}".format(ectime), (10, 50),
			cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		needr=EyeRestNeedTime*60-(time.time()-restNeed) if (EyeRestNeedTime*60-(time.time()-restNeed))>0 else 0
		cv2.putText(frame, "Needs rest in : {:.2f} Seconds".format(needr), (10, 70),
			cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		#needw=WalkNeedTime*60-(time.time()-wtime) if (WalkNeedTime*60-(time.time()-wtime))>0 else 0
		
		#cv2.putText(frame, "Needs to walk in : {:.2f} Seconds".format(needw), (10, 90),
		#	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		#print (WalkNeedTime*60-(time.time()-wtime))

	cv2.imshow("EyeRescue", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

cv2.destroyAllWindows()
vs.stop()
