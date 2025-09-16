import cv2
from libcamera import controls
from picamera2 import Picamera2
from time import sleep
picam2 = Picamera2(0)
picam2.preview_configuration.main.size=(3280,2464) #full screen : 3280 2464
picam2.preview_configuration.main.format = "RGB888" #8 bits

picam2.start()

#picam2.set_controls({"AfMode":controls.AfModeEnum.Manual,"LensPosition": 3.0})

while True:
    im = picam2.capture_array()
    #im = cv2.resize(im,(320,240))
    #im = im[70:,60:550] # [start_y:end_y, start_x:end_x]
    im = cv2.flip(im, -1)
    #############################################
    # for frame of size 640 640
    #cv2.rectangle(im, (20,300),(110,380),(0,255,0),4) #green region
    #cv2.rectangle(im, (550,300),(640,380),(0,255,0),4) #green region
    #cv2.rectangle(im, (200,500),(480,550),(255,0,0),4) #green region
    #############################################
    #for frame of size 640 480
    """
    cv2.rectangle(im, (10,220),(100,280),(0,255,0),4) #green region
    cv2.rectangle(im, (390,220),(480,280),(0,255,0),4) #green region
    cv2.rectangle(im, (390,220),(480,280),(255,0,0),4) #green region
    """
    cv2.imshow("preview",im)
    if cv2.waitKey(1)==ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()

