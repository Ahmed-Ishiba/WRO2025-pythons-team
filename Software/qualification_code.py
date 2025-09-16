import cv2
import numpy as np
from libcamera import controls
from picamera2 import Picamera2
from time import sleep
import serial 
import time
from gpiozero import DistanceSensor

ultrasonic1 = DistanceSensor(echo=20,trigger=6) #,pin_factory=factory
ultrasonic2 = DistanceSensor(echo=21,trigger=26)


ser = serial.Serial('/dev/ttyAMA2',9600, timeout=1)
ser.reset_input_buffer()

ser2 = serial.Serial('/dev/ttyAMA0',9600, timeout=1)
ser2.reset_input_buffer()

picam2 = Picamera2(0)
picam2.preview_configuration.main.size=(640,640) #full screen : 3280 2464
picam2.preview_configuration.main.format = "RGB888" #8 bits

picam2.start()
"""
hoigher =  (189, 167, 62)
lower =  (0, 2, 16)
"""

orange_corner = False
blue_corner = False

black_lower = np.array([0, 2, 16], np.uint8)
black_upper =np.array([189, 167, 62], np.uint8)
def left_wall(frame):
   
    cropped_image = frame[300:380,20:110]
    global black_lower
    global black_upper
    cv2.rectangle(im, (20,300),(110,380),(0,255,0),4) #green region
    
    hsvf = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
    black_mask = cv2.inRange(hsvf, black_lower, black_upper)
    black_result = cv2.bitwise_and(cropped_image, cropped_image, mask=black_mask)
    black_contours, black_hierarchy = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(black_contours) > 0:
        largest_black = max(black_contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_black)
        #cv2.drawContours(cropped_image, largest_black, -1, (255, 0, 0), 3)
        x, y, w, h = cv2.boundingRect(largest_black)
        #area = w*h
        #cv2.rectangle(cropped_image,(x,y),(x+w,y+h), (220,220,220), 2)
        return area
    else:
        return 0


def right_wall(frame):
    cropped_image = frame[300:380,550:640]#frame[230:350,455:545]
    global black_lower
    global black_upper
    cv2.rectangle(im, (550,290),(620,370),(0,255,0),4) #green region
    #for i,region in enumerate(cropped_image):
    hsvf = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
    black_mask = cv2.inRange(hsvf, black_lower, black_upper)
    black_result = cv2.bitwise_and(cropped_image,cropped_image, mask=black_mask)
    black_contours, black_hierarchy = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(black_contours) > 0:
        largest_black = max(black_contours, key=cv2.contourArea)
        selected_black=largest_black
        area = cv2.contourArea(selected_black)
        #cv2.drawContours(cropped_image, largest_black, -1, (255, 0, 0), 3)
        x, y, w, h = cv2.boundingRect(largest_black)
        #area = w*h
        #cv2.rectangle(cropped_image,(x,y),(x+w,y+h), (220,220,220), 2)
        return area
    else:
        return 0
        

def blue(frame):
    global blue_corner
    cropped_image = frame[500:550,200:480]#frame[230:350,455:545]
    """
    hoigher =  (114, 201, 175)
	lower =  (99, 134, 68)
    """
    blue_lower = np.array([104, 152, 49], np.uint8)
    blue_upper =np.array([145, 255, 168], np.uint8)
    #for i,region in enumerate(cropped_image):
    hsvf = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
    blue_mask = cv2.inRange(hsvf, blue_lower, blue_upper)
    blue_result = cv2.bitwise_and(cropped_image,cropped_image, mask=blue_mask)
    blue_contours, blue_hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(blue_contours) > 0:
        largest_blue = max(blue_contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_blue)
        cv2.drawContours(cropped_image, largest_blue, -1, (255, 0, 0), 3)
        x, y, w, h = cv2.boundingRect(largest_blue)
        if area>=1000:
            blue_corner = True
            
        #area = w*h
        #cv2.rectangle(cropped_image,(x,y),(x+w,y+h), (220,220,220), 2)


def orange(frame):
    global orange_corner
    cropped_image = frame[500:550,200:480]#frame[230:350,455:545]
    cv2.rectangle(im, (200,500),(480,550),(255,0,0),4) #green region
    """
    hoigher =  (17, 154, 167)
	lower =  (3, 90, 65)
    """
    orange_lower = np.array([3, 90, 65], np.uint8)
    orange_upper =np.array([17, 154, 167], np.uint8)
    #for i,region in enumerate(cropped_image):
    hsvf = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
    orange_mask = cv2.inRange(hsvf, orange_lower, orange_upper)
    orange_result = cv2.bitwise_and(cropped_image,cropped_image, mask=orange_mask)
    orange_contours, orange_hierarchy = cv2.findContours(orange_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(orange_contours) > 0:
        largest_orange = max(orange_contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_orange)
        #cv2.drawContours(cropped_image, largest_orange, -1, (255, 0, 0), 3)
        x, y, w, h = cv2.boundingRect(largest_orange)
        if area >=100:
            orange_corner = True
            
        
        #area = w*h
        #cv2.rectangle(cropped_image,(x,y),(x+w,y+h), (220,220,220), 2)
        
    else:
        return 0
counter = 0
dist_counter = 0
corner_flag = False
while True:
    im = picam2.capture_array()
    #im = im[70:,60:550] # [start_y:end_y, start_x:end_x]
    im = cv2.flip(im, -1)
    #cv2.rectangle(im, (10,200),(100,280),(0,255,0),4) #green region
    #cv2.rectangle(im, (390,200),(490,280),(0,255,0),4) #green region
    left_ultra=ultrasonic1.distance*100
    right_ultra=ultrasonic2.distance*100

    left_wall_area=left_wall(im)
    right_wall_area=right_wall(im)
    blue(im)
    orange(im)
    cv2.imshow("r",im)
    print("right wall area: ",right_wall_area)
    print("left wall area: ",left_wall_area)
    print(" ")
    print("corner counter: ", counter)
    wall_diffrence = right_wall_area - left_wall_area
    if counter //4 == 3:
        ser2.write(b"S\n")
        print("laps finished")
    else:
        if orange_corner and right_ultra == 100:
            ser2.write(b"R\n") # Z
            time.sleep(0.1)    
            if dist_counter >500:
                counter+=1
                dist_counter = 0
            print("orange corner")
        elif blue_corner and left_ultra == 100:
            ser2.write(b"L\n")
            time.sleep(0.1)
            print("blue corner")
            if dist_counter> 500:
                dist_counter = 0
                counter+=1
        else:
            dist_counter+=1
            print("distance between 2 corners: ",dist_counter)
            if -550<=wall_diffrence<=550:
                ser2.write(b"F\n")
                print("forward")
            elif -550>wall_diffrence:
                print("right")
                ser2.write(b"R\n")
            elif 550<wall_diffrence:
                print("left")
                ser2.write(b"L\n")
    print("diffrence in area: ", wall_diffrence)
    if cv2.waitKey(1)==ord('q'):
        break

picam2.stop()
cv2.destroyAllWindows()


