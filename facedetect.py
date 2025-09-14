import cv2

face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

vs=cv2.VideoCapture(0)

while True:
    ret,frame=vs.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+y,w+h),(0,255,0),2)

    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
vs.release()
cv2.destroyAllWindows()

   
