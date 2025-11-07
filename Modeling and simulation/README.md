# Detailed explanation of each model 

# Table of content:  

1. [Electric model](#electric-model)
2. [Map function](#map-function)
3. [Simulink model](#simulink-model)
4. [Cool animation using robotics playground](#animation-using-robotics-playground)




## Electric model:

<img width="2793" height="775" alt="model" src="https://github.com/user-attachments/assets/0dc1673b-fbcd-4bf7-a2f9-15e421545e0c" />  

This model represents the electrical power distribution of a small robotic system. It includes a DC battery, a buck converter for regulated low-voltage supply, an H-Bridge driving a DC motor, a servo motor subsystem, and load models representing microcontrollers and sensors. The goal is to simulate real power consumption, voltage drops, and motor behavior under different load conditions.

### 🟦 Overview of Simscape

Simscape is a MATLAB/Simulink toolbox that allows modeling using physical components rather than manual equations. Components are connected using physical conserving ports (e.g., electrical +/− terminals), ensuring simulations follow real laws like Kirchhoff’s Current/Voltage Law and mechanical rotational dynamics.  

This is useful for:   

- Testing system behavior before hardware assembly.  

- Observing current and voltage profiles.

- Evaluating different power configurations.

- Detecting instability or saturation in motor loads.

### 🔌 System Components and Their Roles   

| **Component**       | **Purpose in the System**                                                                                        | **Important Parameters to Configure**                                         |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| DC Battery          | Supplies the main power to the system, representing the real robot battery.                                      | Nominal voltage, internal resistance, capacity (optional).                    |
| Buck Converter      | Steps down battery voltage to a lower regulated voltage for electronics and low-power devices.                   | Output voltage, inductor value, capacitor value, switching frequency.         |
| Constant Power Load | Models microcontrollers and sensors that draw nearly constant power regardless of voltage.                       | Power consumption (W), minimum operating voltage.                             |
| H-Bridge            | Controls motor direction and speed using PWM input signals.                                                      | Control mode (PWM/Logic), supply voltage, dead-time/shoot-through protection. |
| DC Motor            | Converts electrical power into mechanical rotational power. Represents drivetrain motors.                        | Armature resistance, back-EMF constant, rated torque, inertia.                |
| Servo Motor         | Provides controlled angular positioning (steering / joints). Modeled as DC motor with internal control feedback. | Supply voltage, stall torque, rated speed, control input range (e.g., angle). |
| Current Sensor      | Measures current drawn by a component for monitoring and analysis in simulation.                                 | No parameters (acts as a probe).                                              |
| Voltage Sensor      | Measures voltage across nodes (e.g., battery output, motor terminals).                                           | No parameters (acts as a probe).                                              |
| Scope               | Displays real-time signals from sensors during simulation.                                                       | Number of traces, time display range.                                         |

### How to Recreate the Model Step-By-Step

1. Start Simscape Environment
2. Open Simulink → Simscape → Simscape Electrical → Specialized Power Systems.
3. Add the Power Source
4. Place DC Battery (Simscape → Electrical → Sources).
5. Set nominal voltage matching your real battery.
6. Build the Power Distribution Path
7. Add Buck Converter (Simscape → Electrical → Converters).
8. Connect battery output → buck input.
9. Place Voltage Sensor after buck output to monitor regulated voltage.
10. Add Load for Microcontroller
11. Insert Constant Power Load block.
12. Connect to the buck output to represent electronics load.
13. Add Drive Motor Path
14. Insert H-Bridge and DC Motor blocks.
15. Connect H-Bridge output terminals to motor armature.
16. Drive the H-Bridge with a PWM signal (from a Pulse Generator or control logic).
17. Add Servo Motor
18. Place a Servo DC Motor or build a small subsystem using:

    DC motor + position control + gear constraint.

19. Connect it to the same or separate power bus depending on design.
20. Run the Simulation


## Map function:  

```matlab
function mapped_value = map_value(value)
%MAP_VALUE maps a value from one range to another

    from_low=-50;
    from_high= 50;
    to_low=30;
    to_high=160;
    % Avoid division by zero
    if (from_high - from_low) == 0
        mapped_value = to_low;
        return;
    end

    % mapping equation
    mapped_value = (value - from_low) / (from_high - from_low) * ...
                   (to_high - to_low) + to_low;
end
```

What the Code Does:  
1. Defines the input range

```matlab
from_low = -50;
from_high = 50;

```
2. Defines the output (desired) range
```matlab
to_low = 30;
to_high = 160;

```

3. Applies the linear mapping formula
```matlab
mapped_value = (value - from_low) / (from_high - from_low) * ...
               (to_high - to_low) + to_low;
```

### Simulink model:   

<img width="2758" height="942" alt="model_using_sine" src="https://github.com/user-attachments/assets/fb8efefb-125a-4019-8e4b-66f2f1f56a6a" />

This is the main model with input sine wave to simulate the inputs 
- The input camera is passed through a gain to *convert* it to distance area this gain is through trial and error I then pass it to the filter block
- The ultrasonic readings are subtracted to get difference
- After the filter block I pass it to the PID controller tuned using the PID tuner app
- Then map it and display it on the scope

#### Filter sub-system:   

<img width="2215" height="1020" alt="filter_subsystem" src="https://github.com/user-attachments/assets/069f6a5a-597a-4b3e-9a00-70a85558ac5e" />    

This diagram just calculates the weighted average using the formula:   

<img width="1184" height="66" alt="Screenshot 2025-11-07 005839" src="https://github.com/user-attachments/assets/6c070be4-0a7f-4c2e-8281-6e56b42b33fb" />   

