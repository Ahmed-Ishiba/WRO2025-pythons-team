# Software system of robot:
our software algorithm is divided into 2 sections: centering the robot in the track to avoid walls, detecting the boxes and move accordingly
## centering of robot:
For centering the robot we used combination of algorithms: centering using the ultrasonic distance readings, measuring wall area and getting diffrence to know what wall is closer 

## Detecting the boxes:
For detecting the boxes we used a custom trained Ultralytics YOLO V8, it has proven to be very reliable, as for taking action on where are the boxes and how to maneuver them we get the x-coordinate of box to decide type of turning motion(hard or normal turn) and get the height of robot to know if we are close or not to the box 

### General flow of code:
First we check for corners and give it highest priority, then we check for boxes and lastly check for walls and this is the lowest priority
