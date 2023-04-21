try:
	import cv2
	import pyttsx3
	from cvzone.HandTrackingModule import HandDetector
except:
	import os 
	os.system("pip3 install mediapipe")
	os.system("pip3 install opencv")
	os.system("pip3 install cvzone")
	os.system("pip3 install tensorflow")
finally:
	import cv2
	import pyttsx3
	from cvzone.HandTrackingModule import HandDetector

engine=pyttsx3.init()
font=cv2.FONT_HERSHEY_SIMPLEX
place=(10,50)
scale=1
color=(0,0,0)
thickness=2
linetype=2
fingers={1:"One",2:"Two",3:"Three",4:"Four",5:"Five",0:"No Finger Detected"}

detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
	_, frame = video.read()
	frame = cv2.flip(frame, 1)
	hand = detector.findHands(frame, draw=False)
	if hand:
		pointer = hand[0]
		if pointer:
			fingerup = detector.fingersUp(pointer)
			fingerup=fingerup.count(1)
			finger_text=fingers[fingerup]
			cv2.putText(frame,fingers[fingerup],place,font,scale,color,thickness,linetype)
			engine.say(finger_text)
			engine.runAndWait()
		else:
			cv2.putText(frame,"No Hands Detected",place,font,scale,color,thickness,linetype)
	cv2.imshow("Fingers Detection And Counting", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
video.release()
cv2.destroyAllWindows()