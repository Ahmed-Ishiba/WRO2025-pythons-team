
<p align="center">
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

Documentation of our self-driving car for the **WRO 2025 Future Engineers** category.

Our team members:
- **Ahmed Ibrahim Elsayed** — Software lead  
- **Eyad Ahmed Nazary** — Electrical lead  
- **Nour Eldin Raoof** — Mechanical design & fabrication  
- **Omar Khaled** — Coach and mentor  

---

## Content

1. [Project Overview](#project-overview)  
    1. [What is WRO?](#what-is-wro)  
    2. [Team Introduction](#team-introduction)  
    3. [Our Mission](#our-mission)  
2. [System Design](#system-design)  
    1. [Robot Architecture](#robot-architecture)  
    2. [Design Philosophy](#design-philosophy)  
    3. [System Diagram](#system-diagram)  
    4. [Bill of Materials](#bill-of-materials)  
3. [Hardware](#hardware)  
    1. [Mechanical](#mechanical)  
    2. [Electrical](#electrical)  
4. [Software](#software)  
    1. [Brief Overview](#brief-overview)  
    2. [Code flow chart](#flow-chart)  
5. [MATLAB Modeling & Simulation](#modelling-and-simulation)  
    1. [Model Overview](#model-overview)  
    2. [Problem Context and Strategy](#problem-context-and-strategy)  
    3. [Modeling and Simulation](#modelling-and-simulation)
        1. [Simulink Logical Model](#simulink-logical-model)
        2. [Complementary Filter Subsystem](#complementary-filter-sub-system)
        3. [Stateflow Diagram](#state-flow-diagram)
        4. [MATLAB Function](#matlab-function)
        5. [Simscape Electrical Model](#simscape-electrical-model)  
    4. [Testing and Verification](#testing-and-verification)  
6. [Testing & Calibration](#testing-and-calibration)
7. [Reproduce Our Robot: Step-by-Step Guide](#reproduce-our-robot)
8. [Future Improvements](#future-improvements)
9. [Team photo](#team-photo)  

## Project Overview

### What is WRO?

WRO (World Robot Olympiad), specifically the **Future Engineers** category, is a competition created to foster passion for STEM. The Future Engineers category is designed for university students. The challenge changes every 3 years, and this year the theme is **autonomous driving**.  
The robot must be designed to drive around a track **completely autonomously**, without external human intervention.

### Team Introduction

We are the **third generation** of *The Pythons* team.  
Our team consists of 3 members and a coach:

1. **Ahmed Ibrahim Elsayed (me):** Software lead — 2nd year, Faculty of Engineering, Alexandria University  
2. **Eyad Ahmed Nazary:** Electrical lead — 1st year, AASTMT  
3. **Nour Eldin Raoof:** Mechanical lead — 3rd year, Faculty of Science, Alexandria University  
4. **Omar Khaled:** Team coach — AASTMT

We have been participating in robotics competitions since **2016**, and we joined The Pythons team in **2017**.

### Our Mission

Our main mission in robotics competitions is to **improve ourselves**, gain experience, and meet like-minded people.  
We specifically enjoy WRO because it **encourages open-source work**, allowing teams to learn from each other, share solutions, and build stronger communities.
.
## System Design:
  ### Robot architecture:   
The main input sources are the camera, ultrasonic sensors to measure distance from walls, Time Of Flight sensors to measure distance from obstacles and parking lot walls, MPU6050 sensor to measure orientation angle for corner rotation and to ensure parallel parking.  
Then the raspberry pi processes these input data and outputs character to KB2040 to control servo and DC motors

  ### Design philosophy:
  When designing our robot we always made sure that our design follows a modular design that is easy to comprehend and troubleshoot, which helps us in improving it with ease, this approach also minimizes time delays that may happen due to fabrication and unfortunate mishaps, this also helps anyone without experience in robotics and future teams to pick up where we left off.
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
| Wheels | x4 | 473.00 | 9.45 |
| Motor | x1 | 350.00 | 7.00 |
| Servo (180°) | x1 | 150.00 | 3.00 |
| Arducam | x1 | 3,000.00 | 60.00 |
| Step Down Converter 12V→3.3V | x2 | 35.00 | 0.70 |
| 12V Battery | x1 | 450.00 | 9.00 |
| Ultrasonic Sensor | x2 | 45.00 | 0.90 |
| Motor Driver IC | x1 | 100.00 | 2.00 |
| Big Ball Bearings | x2 | 100.00 | 2.00 |
| Small Ball Bearings | x2 | 50.00 | 1.00 |
| PCB Fabrication | x1 | 1,250.00 | 25.00 |
|Time Of Flight sensor | x2 | _ | _ |
| **Total** | — | **17,186.50** | **363.41** |
## Hardware:
This section includes brief overview of hardware section of robot (Mechanical and electrical).  
Each section is explained in detail in it's respective folder  
SLDPRT, DXF and board files are also included in their respective folder to download, print and get down to business.  
  ### Mechanical:
<img width="749" height="579" alt="Robot 3d Design" src="https://github.com/user-attachments/assets/f3fdd860-52b2-48c4-8d72-d5893f1ccad6" />

During the design phase, we chose to stick with a simple structure to save time on fabrication, especially after making a bold decision that I’ll discuss in the next section. Our main focus however was to maximize the steering angles achievable from the servo by creating a fully free movement system, which is vital in turning since we can turn faster and closer to the blocks than other cars. In order to follow the competition's guidelines of using only _**one**_ motor to provide the forward movement to the whole robot we created a gear system to transfer the motor's movement to the rear wheels, also creating a versatile semi movable component mounting system -as seen in the camera mounting- to eliminate the need for refabrication which in turn cuts down the time needed for assembling the robot. 


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
   For wall tracking I calculated wall area difference that camera sees and wall difference measured from ultrasonic sensors then used sensor fusion to get accurate data that    I then passed to a PID controller to center the robot all processed on the raspberry pi 5.
   
2. Obstacle Avoidance:
    For obstacle avoidance we used a custom trained yolov8 AI model with 500+ pictures to make sure that the robot detects the traffic signs regardless of environment.
    This approach is better than the traditional image processing approach that relies on the environment since HSV values change according to reflected light.
    Our AI model runs on the google edge TPU to achieve high FPS and faster detection.

  <img width="517" height="465" alt="Screenshot 2025-11-07 025213" src="https://github.com/user-attachments/assets/a0b6fed2-e068-4e5d-92f4-ba139c8c52a1" />   

  https://github.com/user-attachments/assets/0746ed6e-e767-420a-9b96-121c0c189ac0




3. Parking:
   IN PROGRESS  
  ### Flow Chart:   

<img width="759" height="1131" alt="flow_chart drawio" src="https://github.com/user-attachments/assets/67a9270c-c505-440a-b1ef-274a783db9c3" />

  
## Modelling and simulation:
  ### Model Overview:  
  Here we will not go into much detail, you can find a detailed explanation, model files and statflow files in the [Modelling and simulation directory](/Modeling%20and%20simulation/)  
  </br>
  When designing our wall centering algorithm we used the simplest algorithm possible due to how hard it is to tune advanced control algorithms like PID or applying filters, however when MathWorks created this award we had no reason not to use it and apply any algorithm we wanted especially after giving us license for the newest MATLAB version for free.  
  </br>
  now we can apply all the algorithms we want and all my crazy ideas, here is what we did:  
  When centering in the previous algorithm we only used the area of the 2 walls seen by our arducam however it was really noisy and changes too fast which is not that good for wall centering, however when we tried to use an ultrasonic sensor the distance readings where precise but the rate at which it changes was really slow  
  </br>
  so now we have 2 methods to measure the same thing each have their pros and cons so we got the idea to fuse them both with a simple weighted sum formula so we can have control over it and ensure it's smoothness  
  
  After we get the result of the formula which measures the deviation of the robot from the center of the lane we then pass it into a PID controller then we take the output of the controller and pass it into a map function that we implemented myself in order to convert the range of the PID output into a range that my servo accepts(from 0 to 180)  
  
  ### Problem context and strategy:  
  the main challenges that we faced were:  
  - Creating the weighted sum formula and tuning the weights
  - Tuning the PID
  - Making sure the map function works correctly
  - and a problem that we realised later is that I don't know how to test this!
  - simulating our electrical system on simscape electrical  

  As for our strategy:   
  1. we started by writing pseudo code for my algorithm and knew it's building blocks
  2. For simplicity we divided this algorithm into 5 parts: the complementary filter, the PID controller, the map function, creating a stateflow diagram and simulating the circuit we then tackled each in this order
  3. we then decided what MathWorks products help with this which were: Simulink for creating a subsystem for my filter and use it's wide variety of blocks to save time on implementing a PID algorithm from scratch, MATLAB for writing code of our mapping function, simscape electrical for simulating my electrical system and stateflow for creating a diagram of my algorithm using states  
  </br>   
  Using MATLAB, Simulink, simscape and state flow saved so much time and were extremely helpful   

  - using MATLAB for writing the mapping code was extremely easy especially with MATLAB's easy syntax
  - Simulink was by far the best tool we used because not only can we tune algorithms and filters without needing any hardware we can just tune it with only clicking one button! not to mention the clear modular look that helped me troubleshoot where exactly our model went wrong, the graphing that helps us understand the behaviour of our robot and derive meaningful data from it and realizing logical problems in minutes that would've taken days to realize
  - stateflow was really helpful in dividing the algorithm like a flow chart but much briefly, helped us in verifying my code since the code is divided into states just like stateflow and it also helped us in verifying condition if changing states and overall is a vital tool
  - simscape electric was used for simulating our circuit and finding out stall current, max current draw and we used it to correct our choice of battery since we kept having power issues but using simscape we corrected a mistake that would've cost us the competition, this is also a tool that we would definitely use for future robotics projects


  ### Modelling and simulation:  
  #### Simulink logical model:  
  
  now for the main model as I said everything is explained in detail in the [Modelling directory.](/Modeling%20and%20simulation/)  
  <img width="2743" height="665" alt="simulink_model" src="https://github.com/user-attachments/assets/ba717568-8d41-4b9a-b2dc-d03ecc2fd308" />  

  This is the main model and as you can see we take input from 2 sources that somewhat measure the same thing then pass it into our complementary filter that outputs an estimated deviation from the center of the lane and passes it to a PID controller and finally map it to servo range using the map function and send it to the servo  
  
 this algorithm is from my perspective as simple as it gets while at the same time maintaining it's simplicity for fast and easy troubleshooting (not that there is room for error after tuning it)  

#### Complementary filter sub-system:  

 For the complementary filter we created a sub-system for it which is by far the most useful feature in simulink since the logic for the filter is very confusing when put with the main system, here is the diagram for the complementary filter (explained in detail in the modelling directory):  
 
  <img width="2215" height="1020" alt="filter_subsystem" src="https://github.com/user-attachments/assets/ba2a756d-4e1d-4925-9a7c-14c39b6509c1" />  

#### State-flow diagram:   

  Here is the stateflow diagram for you to understand how our code is divided  

  <img width="2647" height="993" alt="stateflow_chart" src="https://github.com/user-attachments/assets/09cf25d1-6080-4537-be46-1af9da436630" />     

  
#### MATLAB function:   

Here is the mapping function we implemented which is just a mathematical formula nothing too complicated   

<img width="517" height="465" alt="mapping_function" src="https://github.com/user-attachments/assets/b2c33d0e-713c-4348-82fd-19b691f7c8e8" />

#### Simscape electrical model:   
We used simscape electrical to measure our maximum ampere consumption, required voltage and suitable battery capacity, here is a photo of our model:   

<img width="2793" height="775" alt="model" src="https://github.com/user-attachments/assets/c85061a7-b311-4031-9667-db40fa0159a7" />

  ### Testing and verification:   
  #### Testing Logical model:   
  
  For testing this model we had to think and come up with ideas we then came to the conclusion to use the simulink function generator  
  
  we used a sin wave to simulate changing input and we of course got an output in shape of sin wave which is both scientifically and physically correct since this model is considered a linear time-invariant system so only the amplitude changes and physically correct since when error increases from the setpoint(the rise of the sine wave) the output should also increase to compensate and correct this error  

  <img width="2758" height="942" alt="model_using_sine" src="https://github.com/user-attachments/assets/3a6dbd48-d4e8-44ee-a9e9-65a878e14a8a" />  


  <img width="517" height="465" alt="complementary_filter_and_pid" src="https://github.com/user-attachments/assets/e523abe5-24c2-4811-b2c5-64aa3196de27" />  

this is the graph of the complementary filter and the PID controller and above it is the model but we used the sin generator as the input.

<img width="517" height="465" alt="Screenshot 2025-11-05 002140" src="https://github.com/user-attachments/assets/ef41a2ba-69e5-4b26-b495-79c965bd8cca" />  

This is the output(servo degree) resulting from the model and as you can see it changes reasonably with the changing the input both following the same graph  

</br>
We also used step function generator to simulate specific cases that I encountered when working on my robot and coincidentally found them

<img width="2729" height="744" alt="model_using_step" src="https://github.com/user-attachments/assets/08b10d94-d160-4325-ad85-de4bb901372a" />  

<img width="2880" height="1920" alt="step_output" src="https://github.com/user-attachments/assets/3533cf66-be00-4951-a87c-76d260adf74b" />

this is the output (servo degree) resulting from our model and above it is the model using the step function generator  

</br>

#### Testing the electrical model:  

As for testing our electrical model it was as easy as hitting run then seeing the output voltage and current intensity on our scope  

  <img width="2878" height="1720" alt="voltage_Intensity_graph" src="https://github.com/user-attachments/assets/991cf0b1-0833-4dbf-8810-251972cb08f0" />   

 As you can see we got a max current draw of 7 Amps and voltage of approximately 11.1 volts so we made our decision for battery type by dividing available battery capacities on the internet by the max current and getting how long it will last.  

## Testing and calibration:
After completing the robot assembly, we performed a series of tests to ensure that every subsystem was functioning correctly.
We ran the test scripts located in the [Software Testing Directory](/Software/System%20Testing/)

- Communication between the microcontrollers and sensors
- Sensor testing and calibration
- Motor operation and direction control
- Servo steering response
- Camera functionality and data transmission

## Reproduce Our Robot:  
1. First start with the main body of robot (after buying components of course)
2. Fabricate the pcb since this is the body or if you want to wire everything and don't need a pcb just download our solidworks files and cnc cut it
3. assemble the robot by connecting everything to the pcb like labeled in our fusion360 file or connect using jumper wires
4. setup the raspberry pi and enable i2c and uart
5. clone this repo on raspberry pi
6. test the system using the files in the [Software testing directory](/Software/System%20Testing/)
7. After making sure every component in the system is running normally, run the main code
8. Now you have a working WRO Future engineers self-driving car!



## Future improvements:
In the future if we participate again and for other teams looking at this repo here are some improvements I wished to implement:
- Use better sensor fusion algorithms
- Create a Simulink environment specifically for this competition like the one in robotics playground
- Better weight distribution in the robot design
- Put built-in voltage sensor
- add cloud-based data logging for better debugging
- create a GUI that combine camera frame and terminal output (looks cool no other reason)
## Team photo:  

<img width="640" height="676" alt="Screenshot 2025-11-07 003350" src="https://github.com/user-attachments/assets/3143a9e5-1793-44a2-9231-20ba725bd0d0" />

