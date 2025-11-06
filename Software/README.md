# Raspberry pi system:
our algorithm is divided into 2 sections: centering the robot in the track to avoid walls, detecting the boxes and move accordingly
## centering of robot:
For centering the robot we used combination of algorithms: centering using the ultrasonic distance readings, measuring wall area and getting diffrence to know what wall is closer then combining the 2 using our own complementary filter 

### how do we combine 2 fundementally different measurements like area and distance?
well I have a pretty nice analogy, if your eyes were closed and you are in a maze with another person and your task was to go to find this person knowing that this person will shout every 3 seconds or so how will you find him?  

well that is easy you can use your hands to feel the maze and see where to go and at the same time hear the shouting of this person to know if you are getting closer or farther, well now you have used 2 different senses to know where to go.

### What is this complementary filter?

A complementary filter in general is a way to filter the noisy inputs or inaccurate in order to produce stable output

how does it work?  

it realies on a mathematical formula known as **weighed average** this formula tells us that if you have 2 inputs that somewhat have same nature and measure same thing you can combine them in a way where you can *trust* an input more than the other thus calling it a weighted average because you provide weight to each input symbolizing how much you trust said input

complementary filter formula:  
<img width="1184" height="66" alt="Screenshot 2025-11-07 005839" src="https://github.com/user-attachments/assets/7f3c2708-0393-4e59-9a6c-92ae191f5b36" />

knowing that the alpha is the weight we decide  

implemented in code as: 
```python
def complementary_filter(wall_area_diff, ultrasonic_diff, alpha=0.7):
    """
    Complementary filter for fusing two distance-related signals.
    """
    return alpha * wall_area_diff + (1 - alpha) * ultrasonic_diff


# Example
filtered_value = complementary_filter(0.35, 0.32, alpha=0.7)
print("Filtered Output:", filtered_value)

```  
### PID controller:  
A PID controller (Proportional–Integral–Derivative controller) is a feedback control method used to minimize the error between a desired setpoint and the actual measured value.
It does this by calculating a correction value made of three components:

- Proportional (P): Reacts to the current error

- Integral (I): Accumulates past errors to eliminate steady-state offset

- Derivative (D): Predicts future error based on the rate of change

By combining these three terms, the PID controller can respond quickly, remain stable, and reduce long-term error.  

PID formula:  

$$
e(t) = \text{setpoint} - \text{measurement}
$$

$$
u(t) = K_p \, e(t) \+\ K_i \int_{0}^{t} e(\tau)\ d\tau \+\ K_d \frac{d e(t)}{dt}
$$


code implementation:  
```python
class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.integral = 0
        self.prev_error = 0

    def compute(self, setpoint, measurement, dt):
        # Calculate error
        error = setpoint - measurement
        
        # Proportional term
        P = self.Kp * error
        
        # Integral term
        self.integral += error * dt
        I = self.Ki * self.integral
        
        # Derivative term
        derivative = (error - self.prev_error) / dt
        D = self.Kd * derivative
        
        # Save error for next cycle
        self.prev_error = error
        
        # PID output
        return P + I + D


# Example usage:
pid = PIDController(Kp=1.2, Ki=0.4, Kd=0.05)
output = pid.compute(setpoint=1.0, measurement=0.85, dt=0.02)
print("PID Output:", output)

```
## Detecting the boxes:
For detecting the boxes we used a custom trained Ultralytics YOLO V8, it has proven to be very reliable, as for taking action on where are the boxes and how to maneuver them we get the x-coordinate of box to decide type of turning motion(hard or normal turn) and get the height of robot to know if we are close or not to the box 

## Flow chart of code:  

 <img width="759" height="1131" alt="flow_chart drawio" src="https://github.com/user-attachments/assets/cf2a2ca1-d456-4619-83a6-8ebfc6729507" />


### General flow of code:
First we check for corners and give it highest priority, then we check for boxes and lastly check for walls and this is the lowest priority  

<img width="531" height="61" alt="Untitled Diagram drawio" src="https://github.com/user-attachments/assets/7dc40b80-0634-4923-b08b-cd6a7f72f918" />


# KB2040 system:
The code used in the KB2040 microcontroller is just simple motor control and servo control which can be included on the raspberry pi but we decided to sperate them for simplicity and not to put too much load on the raspberry pi

