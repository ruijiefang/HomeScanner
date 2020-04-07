import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cnt=0
FOLDER='cap/'

def write(im):
  global cnt
  cv2.imwrite(FOLDER+str(cnt)+'.jpg', im)
  print('CAP: WRITE SUCCESS: ' + str(cnt))
  cnt += 1

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
    gray = cv2.resize(gray, None, fx=1/2, fy=1/2, interpolation = cv2.INTER_CUBIC)

    cv2.imshow('CAPTURE',gray)
    key=cv2.waitKey(1)
    if key&0xFF==ord('q'): 
        break
    elif key&0xFF==ord('w'):
        print("CAP: WRITING FILE...")
        write(gray)

cap.release()
cv2.destroyAllWindows()



