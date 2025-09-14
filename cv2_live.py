import cv2


vs=cv2.VideoCapture('dai.mp4')


while True:
    ret,frame=vs.read()
    framer = cv2.resize(frame, (640,480), interpolation = cv2.INTER_AREA)


    
    cap=cv2.rectangle(framer,(50,50),(590,430),(0,23,0),4)
    cap=cv2.circle(framer,(320,240),50,(0,234,0),4)
    cap=cv2.line(framer,(320,50),(320,190),(0,234,0),4)
    cap=cv2.line(framer,(320,430),(320,290),(0,234,0),4)
    cap=cv2.line(framer,(50,240),(270,240),(0,234,0),4)
    cap=cv2.line(framer,(590,240),(370,240),(0,234,0),4)
    
    if not ret:
        break
    cv2.imshow("result",framer)
    if cv2.waitKey(100) & 0xFF==ord("q"):
       
        break
vs.release()
cv2.destroyAllWindows()
