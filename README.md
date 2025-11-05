<p align=center>
<img width="964" height="259" alt="mainThepythons-removebg-preview" src="https://github.com/user-attachments/assets/ca71d4ee-6c42-4b0f-98d4-a79505348210" />

</p>
<p align="center">
  <a href="https://the-pythons.com" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-blue?logo=google-chrome&logoColor=white" alt="Website Badge"/>
  </a>
  <a href="mailto:ahmedishiba9@gmail.com">
          <img src="https://img.shields.io/badge/Contact-Ahmed_Ishiba-red?logo=gmail&logoColor=white" />
  </a>
    <a href="https://github.com/ahmed-ishiba">
    <img src="https://img.shields.io/badge/Ahmed%20Elsayed-Contributor-blue?logo=github" alt="Ahmed Elsayed"/>
  </a>
  <a href="https://github.com/Eyad005">
    <img src="https://img.shields.io/badge/Eyad%20Nazary-Contributor-green?logo=github" alt="Eyad Nazary"/>
  </a>
    <a href="https://www.youtube.com/@thepythonseg">
    <img src="https://img.shields.io/badge/Youtube-The%20Pythons%20Team-red?logo=Youtube" alt="Youtube Channel"/>

  </a>
</p>  

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
5. [Matlab Modeling & simulation](#modeling-and-simulation)  
    5.1. [Model Overview](#model-overview)  
    5.2. [Problem context and strategy](#problem-context-and-strategy)  
    5.3. [Modeling and simulation](#modeling-and-simulation)  
    5.4. [Testing and verification](#testing-and-verification)  
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
<img width="517" height="465" alt="system_diagram_main drawio" src="https://github.com/user-attachments/assets/bc966d70-36db-492f-ba29-251a000bfefb" />

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
  ### Model Overview:  
  Here I will not go into much detail, you can find a detailed explanation, model files and statflow files in the [Modeling and simulation directory](/Modeling%20and%20simulation/)  
  </br>
  When designing our wall centering algorithm we used the simplest algorithm possible due to how hard it is to tune advanced control algorithms like PID or applying filters however when MathWorks created this award I had no reason not to use it and apply any algorithm I wanted especially after giving us license for the newest Matlab version for free.  
  </br>
  now I can apply all the algorithms I want and all my crazy ideas, here is what I did:  
  When centering in the previous algorithm I only used the area of the 2 walls seen by my arducam however it was really noisy and changes too fast which is not that good for wall centering, however when I tried to use an ultrasonic sensor the distance readings where precise but the rate at which it changes was really slow  
  </br>
  so now I have 2 methods to measure the same thing each have their pros and cons so I got the idea to fuse them both with a simple weighted sum formula so I can have control over it and ensure it's smoothness  
  
  After I get the result of the formula which measures the deviation of the robot from the center of the lane I then pass it into a PID controller then I take the output of the controller and pass it into a map function that I implemented myself in order to convert the range of the PID output into a range that my servo accepts(from 0 to 180)  
  
  ### Problem context and strategy:  
  the main challanges that I faced were:  
  - Creating the weighted sum formula and tuning the weights
  - Tuning the PID
  - Making sure the map function works correctly
  - and a problem that I realised later is that I don't know how to test this!
  - I also discovered when I was talking to my friend that I can simulate our electrical system on simscape electrical so I had to check it out
  As for our strategy:
  1. I started by writing psuedo code for my algorithm and knew it's buidling blocks
  2. For simplicity I divided this algorithm into 2 parts: the complementery filter, the PID controller, my map function and creating a statflow diagram then tackeled each in this order
  3. I then decided what Mathworks products help with this which were: Simuluink for creating a subsystem for my filter and used it's wide variety of blocks to save time on implementing a PID algorithm from scratch, Matlab for writing code of my mapping function, simscape electrical for simulating my electrical system and stateflow for creating a diagram of my algorithm using states  
  </br>
  Using Matlab, simulink, simscape and state flow saved so much time and were extremely helpful

  - using Matlab for writing the mapping code was extremely easy especially with matlab's easy syntax
  - simulink was by far the best tool I used because not only can I tune algorithms and filters without needing any hardware I can just tune it with only clicking one button! not to mention the clear modular look that helped me troubleshoot where exactly my model went wrong, the graphing that helps me understand the behaviour of my robot and derive meaningful data from it and realizing logical problems in minutes that would've taken days to realize
  - stateflow was really helpful in dividing the algorithm like a flow chart but stateflow is much more brief, helped me in verifying my code since the code is divided into states just like stateflow and it also helped me in verfiying condition if changing states and overall is a vital tool
  - for simscape electric I unfortunately discovered it a little late but after using it I realized how increadible it is for simulating a circuit and finding out stall current, max current draw and I used it to correct our choice of battery since we kept having power issues but using simscape we corrected a mistake that would've cost us the competition, this is also a tool that we would definately use for future robotics projects


  ### Modeling and simulation:  
  now for the main model as I said everything is explained in detail in the modeling directory.  
  <img width="2743" height="665" alt="simulink_model" src="https://github.com/user-attachments/assets/ba717568-8d41-4b9a-b2dc-d03ecc2fd308" />  

  This is the main model and as you can see I take input from 2 sources that somewhat measure the same thing then pass it into my complementery filter that outputs an estimated deviation from the center of the lane and passes it to a PID controller and finally map it to servo range using the map function and send it to the servo  
  
 this algorithm is from my perspective as simple as it gets while at the same time maintaining it's simplicity for fast and easy troubleshooting (not that there is room for error after tuning it)  

 as for the complementery filter I created a sub-system for it which is by far the most useful feature in simulink since the logic for the filter is very confusing when put with the main system, here is the diagram for the compelemetery filter (explained in detail in the modeling directory):  
 
  <img width="2215" height="1020" alt="filter_subsystem" src="https://github.com/user-attachments/assets/ba2a756d-4e1d-4925-9a7c-14c39b6509c1" />  

  Also here is the stateflow diagram for you to understand how my code is divided  

  <img width="2647" height="993" alt="stateflow_chart" src="https://github.com/user-attachments/assets/09cf25d1-6080-4537-be46-1af9da436630" />  

Here is the mapping function I implemented which is just a formula nothing too complicated  

<img width="1333" height="792" alt="mapping_function" src="https://github.com/user-attachments/assets/b2c33d0e-713c-4348-82fd-19b691f7c8e8" />


  ### Testing and verification:    
  For testing this model I had to think and come up with ideas I then came to the conclusion to use the simulink function generator  
  
  I used a sin wave to simulate changing input and I of course got an output in shape of sin wave which is both scientifically and physically correct since this model is considered a linear time-invariant system so only the amplitude changes and physically correct since when error increases from the setpoint(the rise of the sine wave) the output should also increase to compensate and correct this error  

  <img width="2758" height="942" alt="model_using_sine" src="https://github.com/user-attachments/assets/3a6dbd48-d4e8-44ee-a9e9-65a878e14a8a" />  


  <img width="1642" height="1536" alt="complementary_filter_and_pid" src="https://github.com/user-attachments/assets/e523abe5-24c2-4811-b2c5-64aa3196de27" />  

this is the graph of the compelmentery filter and the PID controller and above it is the model but I used the sin generator as the input.

<img width="2379" height="1706" alt="Screenshot 2025-11-05 002140" src="https://github.com/user-attachments/assets/ef41a2ba-69e5-4b26-b495-79c965bd8cca" />  

This is the output(servo degree) resulting from the model and as you can see it changes reasonably with the changing the input both following the same graph  

</br>

I also used step function generator to simulate specific cases that I encountered when working on my robot and coincitentally found them

<img width="2729" height="744" alt="model_using_step" src="https://github.com/user-attachments/assets/08b10d94-d160-4325-ad85-de4bb901372a" />  

<img width="2880" height="1920" alt="step_output" src="https://github.com/user-attachments/assets/3533cf66-be00-4951-a87c-76d260adf74b" />

this is the output (servo degree) resulting from my model and above it is the model using the step function generator

  
## Testing and calibration:
After completing the robot assembly, we performed a series of tests to ensure that every subsystem was functioning correctly.
We ran the test scripts located in the [Software Testing Directory](/Software/System%20Testing/)

- Communication between the microcontrollers and sensors
- Sensor testing and calibration
- Motor operation and direction control
- Servo steering response
- Camera functionality and data transmission

## Future improvments:
In the future if we participate again and for other teams looking at this repo here are some improvments I wished to implement:
- Use better sensor fusion algorithms
- Better weight distribution in the robot design
- Put built-in voltage sensor
- add cloud-based data logging for better debugging
- create a GUI that combine camera frame and terminal output (looks cool no other reason)

