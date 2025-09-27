#include <Servo.h>

bool motion_flag =true;
bool start_flag = false;
bool start_led = false;
//////////////////////////
#define SERVO_PIN 4
#define MOTOR_PIN_A 2
#define MOTOR_PIN_B 3  
#define BUTTON1_PIN 5
#define BUTTON2_PIN 6
#define LED1_PIN 10
#define LED2_PIN 11

//////////////////////////
Servo myServo;

void setup() {

  pinMode(BUTTON1_PIN, INPUT_PULLDOWN);
  pinMode(BUTTON2_PIN, INPUT_PULLDOWN);
  pinMode(LED1_PIN, OUTPUT);
  pinMode(LED2_PIN, OUTPUT);
  pinMode(MOTOR_PIN_A, OUTPUT);
  pinMode(MOTOR_PIN_B, OUTPUT);
  
  myServo.attach(SERVO_PIN);
  myServo.write(90);
  
  Serial1.begin(9600);
  Serial.begin(115200);
  
  while (Serial1.available()) Serial1.read();
  
  digitalWrite(LED1_PIN, LOW);
  digitalWrite(LED2_PIN, LOW);
  analogWrite(MOTOR_PIN_A, 0);
  analogWrite(MOTOR_PIN_B, 0);
  
}

void loop() {
  bool button1_reading = digitalRead(BUTTON1_PIN);
  bool button2_reading = digitalRead(BUTTON2_PIN);
  if(button1_reading == true){
   start_led = true;
   start_flag = true;
    
  }
  // Handle UART
  if(start_flag){
  if (Serial1.available() > 0) {
    if (start_led){
    digitalWrite(LED1_PIN, HIGH);
    delay(500);
    digitalWrite(LED1_PIN, LOW);    
    start_led = false;
    }
    String cmd = Serial1.readStringUntil('\n');
    cmd.trim();
    if (cmd == "S") {
     myServo.write(100);
      if(motion_flag){
      analogWrite(MOTOR_PIN_A, 0);
      analogWrite(MOTOR_PIN_B, 0);
      
    }
    delay(30000);
    }
    else{
    if (cmd == "F") {
      myServo.write(100);
      if(motion_flag){
      analogWrite(MOTOR_PIN_A, 0);
      analogWrite(MOTOR_PIN_B, 200);
      }
      
    }
    if (cmd == "BR"){
      myServo.write(150);
      analogWrite(MOTOR_PIN_A, 200);
      analogWrite(MOTOR_PIN_B, 0);
    }
    if(cmd == "BL"){
      myServo.write(50);
      analogWrite(MOTOR_PIN_A, 200);
      analogWrite(MOTOR_PIN_B, 0);
    }
    
    if (cmd == "R") {
      myServo.write(140);
      if(motion_flag){
      analogWrite(MOTOR_PIN_A, 0);
      analogWrite(MOTOR_PIN_B, 200);
      }
      
    }
    
    if (cmd == "L") {
      myServo.write(60);
      if(motion_flag){
      analogWrite(MOTOR_PIN_A, 0);
      analogWrite(MOTOR_PIN_B, 200);
      }
    }

    
    if (cmd == "LS") {
      myServo.write(70);
      if(motion_flag){
      analogWrite(MOTOR_PIN_A, 0);
      analogWrite(MOTOR_PIN_B, 200);
      }
    }

    
    if (cmd == "RS") {
      myServo.write(120);
      if(motion_flag){
      analogWrite(MOTOR_PIN_A, 0);
      analogWrite(MOTOR_PIN_B, 200);
      }
    }
    
    if (cmd == "HL") {
     myServo.write(40);
      if(motion_flag){
      analogWrite(MOTOR_PIN_A, 0);
      analogWrite(MOTOR_PIN_B, 255);
      delay(100);
    }
    }
    //-160, -7, -210
    //-116, 151 , -312
    if (cmd == "HR") {
     myServo.write(160);
      if(motion_flag){
      analogWrite(MOTOR_PIN_A, 0);
      analogWrite(MOTOR_PIN_B, 255);
      delay(100);
    }
    }
    if (cmd == "LC"){
      myServo.write(50);
      analogWrite(MOTOR_PIN_A, 0);
      analogWrite(MOTOR_PIN_B, 200);
    }
    if (cmd == "RC"){
      myServo.write(150);
      analogWrite(MOTOR_PIN_A, 0);
      analogWrite(MOTOR_PIN_B, 200);
    }
    
  }
  
}
}
}
