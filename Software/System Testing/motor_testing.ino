#include <Servo.h>

Servo myservo;  // create Servo object to control a servo
// twelve Servo objects can be created on most boards

#define SERVO_PIN 4
#define MOTOR_PIN_A 2
#define MOTOR_PIN_B 3  
#define BUTTON1_PIN 5
#define BUTTON2_PIN 6
#define LED1_PIN 10
#define LED2_PIN 11

int pos = 0;    // variable to store the servo position
int i =1;
void setup() {
  myservo.attach(4);  // attaches the servo on pin 9 to the Servo object
    pinMode(MOTOR_PIN_A, OUTPUT);
  pinMode(MOTOR_PIN_B, OUTPUT);
}

void loop() {
      myservo.write(100);
      if(i ==1){
      i++;
      analogWrite(MOTOR_PIN_A, 0);
      analogWrite(MOTOR_PIN_B, 200);
      delay(2000);
      
      }
      else{
      analogWrite(MOTOR_PIN_A, 0);
      analogWrite(MOTOR_PIN_B, 0);
      }
}
