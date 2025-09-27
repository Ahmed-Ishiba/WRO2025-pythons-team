from ultralytics import YOLO
import cv2
import numpy as np
from libcamera import controls
from picamera2 import Picamera2
from time import sleep
import serial 
import time
from gpiozero import DistanceSensor

ultrasonic1 =0#DistanceSensor(echo=20,trigger=6) #,pin_factory=factory
ultrasonic2 =0#DistanceSensor(echo=21,trigger=26)


ser = serial.Serial('/dev/ttyAMA2',9600, timeout=1)
ser.reset_input_buffer()

ser2 = serial.Serial('/dev/ttyAMA0',9600, timeout=1)
ser2.reset_input_buffer()

picam2 = Picamera2(0)
picam2.preview_configuration.main.size=(640,640) #full screen : 3280 2464
picam2.preview_configuration.main.format = "RGB888" #8 bits
picam2.start()

model = YOLO("/home/pi/yolo/model_- 24 september 2025 0_49_edgetpu.tflite", task='detect') 

orange_corner = False
blue_corner = False

see_black_left = False
see_black_right = False

go_back = False

back_right = False
back_left = False

counter = 0
dist_counter = 0

corner_flag = False

box_flag = False

saw_red, saw_green = False, False

"""
hoigher =  (179, 164, 72)
lower =  (0, 0, 27)

"""

black_lower = np.array([0, 0, 27], np.uint8)
black_upper =np.array([179, 164, 72], np.uint8)
def left_wall(frame):
   
    cropped_image = frame[290:380,20:110]
    global black_lower
    global black_upper
    global see_black_left
    global back_left
    cv2.rectangle(im, (20,290),(110,380),(0,255,0),4) #green region
    
    hsvf = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
    black_mask = cv2.inRange(hsvf, black_lower, black_upper)
    black_result = cv2.bitwise_and(cropped_image, cropped_image, mask=black_mask)
    black_contours, black_hierarchy = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(black_contours) > 0:
        largest_black = max(black_contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_black)
        cv2.drawContours(cropped_image, largest_black, -1, (255, 0, 0), 3)
        x, y, w, h = cv2.boundingRect(largest_black)
        #area = w*h
        #cv2.rectangle(cropped_image,(x,y),(x+w,y+h), (220,220,220), 2)
        if 6500>area:
            see_black_left = True
            back_left = False
            return area//10
        if area >=6500:
            back_left = True
            return area//10
        else:
            see_black_left = False
            back_left = False
            return 0
        
    else:
        see_black_left = False
        return 0


def right_wall(frame):
    cropped_image = frame[290:380,530:620]#frame[230:350,455:545]
    global black_lower
    global black_upper
    global see_black_right
    global back_right
    cv2.rectangle(im, (530,290),(620,380),(0,255,0),4) #green region
    #for i,region in enumerate(cropped_image):
    hsvf = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
    black_mask = cv2.inRange(hsvf, black_lower, black_upper)
    black_result = cv2.bitwise_and(cropped_image,cropped_image, mask=black_mask)
    black_contours, black_hierarchy = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(black_contours) > 0:
        see_black_right = True
        largest_black = max(black_contours, key=cv2.contourArea)
        selected_black=largest_black
        area = cv2.contourArea(selected_black)
        cv2.drawContours(cropped_image, largest_black, -1, (255, 0, 0), 3)
        x, y, w, h = cv2.boundingRect(largest_black)
        #area = w*h
        #cv2.rectangle(cropped_image,(x,y),(x+w,y+h), (220,220,220), 2)
        if 6500>area:
            back_right = False
            return area//10
        if area>=6500:
            back_right = True
            return area//10
            
        else:
            back_right = False
            see_black_right = False
            return 0
    else:
        see_black_right = False
        return 0


def middle_region(frame):
    cropped_image = frame[280:450,280:520]#frame[230:350,455:545]
    global black_lower
    global black_upper
    global see_black_middle, go_back
    #cv2.rectangle(im, (120,280),(520,450),(0,255,0),4) #left region
    #for i,region in enumerate(cropped_image):
    hsvf = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
    black_mask = cv2.inRange(hsvf, black_lower, black_upper)
    black_result = cv2.bitwise_and(cropped_image,cropped_image, mask=black_mask)
    black_contours, black_hierarchy = cv2.findContours(black_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(black_contours) > 0:
        
        largest_black = max(black_contours, key=cv2.contourArea)
        
        area = cv2.contourArea(largest_black)
        cv2.drawContours(cropped_image, largest_black, -1, (255, 0, 0), 3)
        x, y, w, h = cv2.boundingRect(largest_black)
        #area = w*h
        #cv2.rectangle(cropped_image,(x,y),(x+w,y+h), (220,220,220), 2)
        
        if area>=16000:
            go_back = True
            return area//10
            
        else:
            go_back = False
            return 0
    else:
        
        return 0


def blue(frame):
    global blue_corner
    cropped_image = frame[500:550,200:480]#frame[230:350,455:545]
    """
    hoigher =  (121, 199, 139)
    lower =  (92, 121, 35)

    """
    blue_lower = np.array([92, 121, 35], np.uint8)
    blue_upper =np.array([121, 199, 139], np.uint8)
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
        if area >= 100:
            blue_corner = True
            
        #area = w*h
        #cv2.rectangle(cropped_image,(x,y),(x+w,y+h), (220,220,220), 2)


def orange(frame):
    global orange_corner
    cropped_image = frame[500:550,200:480]#frame[230:350,455:545]
    cv2.rectangle(im, (200,500),(480,550),(255,0,0),4) #green region
    """
    hoigher =  (37, 158, 155)
	lower =  (0, 55, 100)
    """
    orange_lower = np.array([0, 55, 100], np.uint8)
    orange_upper =np.array([37, 158, 155], np.uint8)
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
        if area>=100:
            range_corner = True
        print("orange corner flag: ", orange_corner)
          
    else:
        return 0

while True:
    im = picam2.capture_array()
    #im = im[70:,60:550] # [start_y:end_y, start_x:end_x]
    im = cv2.flip(im, -1)
    im_ = im[280:, 20:640]
    #cv2.rectangle(im, (10,200),(100,280),(0,255,0),4) #green region
    #cv2.rectangle(im, (390,200),(490,280),(0,255,0),4) #green region
    left_ultra=ultrasonic1*100
    right_ultra=ultrasonic2*100
    
    ultra_diff = right_ultra-left_ultra
    
    print("ultra diffrence: ", right_ultra-left_ultra)
    results=model.track(im_, imgsz=(320,320), conf=0.6)
    
    image_ = results[0].plot()
    
    left_wall_area=left_wall(im)
    right_wall_area=right_wall(im)
    middle_area = middle_region(im)
    blue(im)
    orange(im)
    
    cv2.imshow("r",image_)
    #cv2.imshow("main",im)
    print("area of middle region",middle_area)
    print("right wall area: ",right_wall_area)
    print("left wall area: ",left_wall_area)
    print("corner counter: ", counter)
    print("right ultrasonic: ", right_ultra)
    print("left ultrasonic: ", left_ultra)
    print("do i see orange: ",orange_corner)
    print("do i see blue: ",blue_corner)
    wall_diffrence = right_wall_area - left_wall_area
    if counter //4 == 3:
        last_time = True
        ser2.write(b"F\n")
        time.sleep(1)
        ser2.write(b"S\n")
        time.sleep(5)
        print("laps finished")
    else:
        if orange_corner and dist_counter>30:
            dist_counter = 0
            counter+=1
            ser2.write(b"HR\n") # Z
            print("orange corner")
            #time.sleep(0.3)
        elif blue_corner and dist_counter > 30 :
            dist_counter = 0
            counter+=1
            ser2.write(b"HL\n")
            print("blue corner")
            #time.sleep(0.3)
            
        else:
            
            box = results[0].boxes.xywh.tolist()
            if results[0].boxes:
                
                box_flag = True
                cls = int(results[0].boxes.cls[0])
                print("box variable: ", box)
                #print("name of object: ", r.names[cls])
                if cls == 0:
                    saw_green = True
                    print("green detected")
                    if 400>box[0][0]>300 and 80>=box[0][3] >=20:
                        print("turn left box")
                        ser2.write(b"LC\n")
                        time.sleep(0.1)
                        #ser2.write(b"R\n")
                        #time.sleep(0.1)
                    elif box[0][0] <=300 and box[0][3] > 80:
                        print("hard left box")
                        ser2.write(b"HL\n")
                        time.sleep(0.2)
                        #ser2.write(b"Z\n")
                        #time.sleep(0.1)
                    elif box[0][0] >= 400:
                        print("forget boxes drive accordnig to walls, green")
                        box_flag = False
                    
                elif cls == 1:
                    saw_red = True
                    print("red detected")
                    if 250>box[0][0]>200 and 50>box[0][3] >=20:
                        print("turn right box")
                        ser2.write(b"RC\n")
                        #time.sleep(0.1)
                    elif box[0][0] >=250 and box[0][3] >=50:
                        print("hard right box")
                        ser2.write(b"HR\n")
                        time.sleep(0.1)
                        #ser2.write(b"G\n")
                        #time.sleep(0.1)
                    elif box[0][0] <=200:
                        box_flag = False
                        print("forget boxes drive accordnig to walls, red")
                    else:
                        box_flag = False
            else:
                box_flag = False
            dist_counter+=1
            print("distance between 2 corners: ",dist_counter)
            if not(box_flag):
                if dist_counter >= 40:
                    orange_corner = False
                    blue_corner = False
                if go_back:
                    print("going back wall is too close")                    
                    if back_right:
                        ser2.write(b"BR\n")
                        time.sleep(0.2)
                        saw_red = False
                    if back_left:
                        ser2.write(b"BL\n")
                        time.sleep(0.1)
                        saw_green = False
                if see_black_left or see_black_right:
                    print("do i see black left: ", see_black_left)
                    print("do i see black right: ", see_black_right)
                    if -100<=wall_diffrence<=100:
                        ser2.write(b"F\n")
                        print("forward")
                    elif -100>wall_diffrence:
                        print("right")
                        ser2.write(b"R\n")
                    elif 100<wall_diffrence:
                        print("left")
                        ser2.write(b"L\n")
                else:
                    print("cant see black")                    
                    if middle_area:
                        if back_right:
                            ser2.write(b"BR\n")
                            time.sleep(0.1)
                            saw_red = False
                        if back_left:
                            ser2.write(b"BL\n")
                            time.sleep(0.1)
                            saw_green = False
    print("diffrence in area: ", wall_diffrence)
    print(" ")
    if cv2.waitKey(1)==ord('q'):
        break
picam2.stop()
cv2.destroyAllWindows()



