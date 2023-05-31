import cv2
cam = cv2.VideoCapture(0)
while True:
    v,frame = cam.read()
    cv2.imshow('My Cam',frame)
    cv2.waitKey(2)
    