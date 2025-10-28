
# WRO2025-pythons-team
Documentation of our self-driving car for the WRO 2025 future engineers category, our team members: Ahmed Ibrahim Elsayed responsible for software part of robot, Eyad Ahmed Nazary responsible for electrical part of robot, Nour Eldin Raoof responsible for mechanical design and fabrication of robot and our coach and mentor Omar Khaled
## Content:
1. [Project overview](#project-overview).  
    1.1. [What is WRO?](#what-is-wro)  
    1.2. [Team Introduction](#team-introduction)  
    1.3. [Our Mission](#our-mission)   
2. [System Design](#system-design)  
    2.1. [Robot architecture](#robot-architecture)  
    2.2. [Our design philosophy](#design-philosophy)  
    2.3. [System diagram](#system-diagram)  
    2.4. [Bill Of Materials](#bill-of-materials)  
3. [Hardware](#hardware)    
    3.1. [Mechanical](#mechanical)  
    3.2. [Electrical](#electrical)  
4. [Software](#software)  
    4.1. [Brief overview](#brief-overview)  
    4.2. [Block diagram](#block-diagram)  
5. [Modeling & simulation](#modeling-and-simulation)
6. [Testing & calibration](#testing-and-calibration)
7. [Future improvments](#future-improvments)

## Project overview:

  ### What is WRO:
  
WRO (World Robot Olympiad) specifically future engineers category is a competition created to foster passion for STEM tracks and the future engineers category is made for university students, the challange in the future engineers category changes every 3 years and this year it is autonomous driving, the robot must be designed to drive around a track autonomously without external human intervention.
  ### Team introduction:
We are the third generation of The Pythons team  
Our team consists of 3 members and a coach :  
1. Ahmed Ishiba (me): software head, 2nd year student at Alexandria university Faculty of engineering      
2. Eyad Ahmed: Electrical head, 1st year student at Arab Academy for Science and Technology  
3. Nour eldin Raoof: mechanical head, 3rd year student at Alexandria university Faculty of science  
4. Omar khaled: Team coach, student at Arab Academy for Science and Technology  
Me and my colleagues started participating in robotics competition all the way back in 2018, we joined the pythons team in 2019
  ### Our mission:
Our main mission for participating in robotics competitions in general is to advance our careers, gain experience and meet like-minded people, however we specifically liked WRO because it rewards open-source work which helps us see other teams and how they tackle certain problems.
## System Design:
  ### Robot architecture:   
The main input sources are the camera, ultrasonic sensors to measure distance from walls, Time Of Flight sensors to measure distance from obstacles and parking lot walls, MPU6050 sensor to measure orientation angle for corner rotation and to ensure parallel parking.  
Then the raspberry pi processes these input data and outputs character to KB2040 to control servo and DC motors

  ### design philosophy:
  When designing our robot we always made sure that our design follows a modular design that is easy to copmrehend and troubleshoot, which helps us in improving on it with ease, this approach also minimizes time delays that may happen due to fabrication and unfortunate mishaps, this also helps anyone without experience in robotics and future teams to pick up where we left off.
  ### System diagram:  
  <img width="517" height="465" alt="system_diagram drawio" src="https://github.com/user-attachments/assets/b5c61035-a9ca-40de-a049-db8e5f727b87" />

This diagram shows the main components of the robot and how they communicate.  
- The Raspberry Pi 5 acts as the central controller, running the main software and decision-making algorithms.  
- It communicates with ESP32 microcontroller and KB2040 via UART.  
- The KB2040 handles all real-time tasks such as controlling the servo and DC motors through PWM signals.  
-  All controllers share a common power source with independent voltage regulation for stability.

<br>  

  ### Bill Of Materials:   
  
| Component Name | Number of Items | Price (EGP) | Price (USD) |
|----------------|-----------------|--------------|--------------|
| Google Coral Accelerator | x1 | 6,250.00 | 125.00 |
| ESP32 Supermini | x1 | 350.00 | 7.00 |
| KB2040 | x1 | 425.00 | 8.50 |
| Raspberry Pi 5 | x1 | 4,000.00 | 80.00 |
| IMU MPU6050 | x1 | 125.00 | 2.50 |
| Step Down Converter 12V→5V | x1 | 450.00 | 9.00 |
| Wheels | x2 | 473.00 | 9.45 |
| Motor | x1 | 350.00 | 7.00 |
| Servo (180°) | x1 | 150.00 | 3.00 |
| Arducam | x1 | 3,000.00 | 60.00 |
| Step Down Converter 12V→3.3V | x2 | 35.00 | 0.70 |
| 12V Battery | x1 | 450.00 | 9.00 |
| Ultrasonic Sensor | x1 | 45.00 | 0.90 |
| Motor Driver IC | x1 | 100.00 | 2.00 |
| Big Ball Bearings | x2 | 100.00 | 2.00 |
| Small Ball Bearings | x2 | 50.00 | 1.00 |
| PCB Fabrication | x1 | 1,250.00 | 25.00 |
| **Total** | — | **17,186.50** | **768.55** |
## Hardware:
This section includes brief overview of hardware section of robot (Mechanical and electrical).  
Each section is explained in detail in it's respective folder  
SLDPRT, DXF and board files are also included in their respective folder to download, print and get down to business.  
  ### Mechanical:
<img width="563" height="443" alt="photo_solid" src="https://github.com/user-attachments/assets/527acc7b-9cac-4c63-a7b2-7b6c962012c3" />  

During the design phase, we chose to stick with a simple structure to save time on fabrication, especially after making a bold decision that I’ll discuss in the next section. Our main focus however was to maximize the steering angles achievable from the servo, which is vital in turning since we can turn faster and closer to the blocks than other cars.   

We also chose big wheels to maximize distance crossed during same revolution this also helps in faster steering.  


  ### Electrical:  
<img width="623" height="400" alt="3d_pcb" src="https://github.com/user-attachments/assets/8a41eeca-e9c2-4021-8c3e-2eb19d8ccdcb" />  

You might’ve noticed that our PCB has a rather unusual shape — that’s because it is the shape of our mechanical design!  
This brings us to the bold decision I mentioned earlier: we chose to make the base itself the main circuit.  
This approach not only improves stability and reduces overall size by eliminating separate circuit boards, but also makes assembly incredibly straightforward — every component has its exact place.  

But wait — there’s another bold decision! Did you notice there’s no motor driver on our robot?  
That’s right — we built our own motor driver using a dedicated IC and a decoupling capacitor.  
This approach helped us further reduce the robot’s size by eliminating the need for bulky modules like the L298N or Cytron drivers.


## Software:
In this section I will also only provide overview on code and thought process since line-by-line documentation can be found in the Software directory.  

  ### Brief overview:
  For our software and programming I divided it into 3 sections: 
  - Wall tracking
  -  Obstacle Avoidance
  -  Parking
1. Wall Tracking:
   For wall tracking I calculated wall area diffrence that camera sees and wall diffrence measured from ultrasonic sensors then used sensor fusion to get accurate data that    I then passed to a PID controller to center the robot all processed on the raspberry pi 5.
   
2. Obstacle Avoidance:
    For obstacle avoidance we used a custom trained yolov8 AI model with 500+ pictures to make sure that the robot detects the traffic signs regardless of environment.
    This approach is better than the traditional image processing approach that relies on the environment since HSV values change according to reflected light.
    Our AI model runs on the google edge TPU to achieve high FPS and faster detection.
3. Parking:
   IN PROGRESS  
  ### Block diagram:
## Modeling and simulation:
IN PROGRESS

## Testing and calibration:

## Future improvments
