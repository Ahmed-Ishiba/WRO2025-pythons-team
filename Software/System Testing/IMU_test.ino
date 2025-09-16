#include "Wire.h"
#include "I2Cdev.h"
#include "MPU6050_6Axis_MotionApps20.h"

// Use GPIO 4 (SDA) and 5 (SCL) for ESP32-C3 Super Mini (you can change if needed)
#define SDA_PIN 8
#define SCL_PIN 9

int yaw =0;
#define RX 20
#define TX 21

MPU6050 mpu;

bool dmpReady = false;
uint8_t mpuIntStatus;
uint8_t devStatus;
uint16_t packetSize;
uint16_t fifoCount;
uint8_t fifoBuffer[64];

Quaternion q;
VectorFloat gravity;
float ypr[3]; // yaw, pitch, roll

void setup() {
  Serial.begin(115200);
  Serial1.begin(9600, SERIAL_8N1, RX, TX);
  delay(1000);

  Wire.begin(SDA_PIN, SCL_PIN);
  mpu.initialize();

  Serial.println("Initializing MPU6050...");
  devStatus = mpu.dmpInitialize();

  // Set your own offsets (these vary per sensor)
  mpu.setXAccelOffset(0);
  mpu.setYAccelOffset(0);
  mpu.setZAccelOffset(0);
  mpu.setXGyroOffset(0);
  mpu.setYGyroOffset(0);
  mpu.setZGyroOffset(0);

  if (devStatus == 0) {
    mpu.CalibrateAccel(6);
    mpu.CalibrateGyro(6);
    mpu.PrintActiveOffsets();

    Serial.println("Enabling DMP...");
    mpu.setDMPEnabled(true);
    dmpReady = true;

    packetSize = mpu.dmpGetFIFOPacketSize();
  } else {
    Serial.print("DMP Initialization failed (code ");
    Serial.print(devStatus);
    Serial.println(")");
  }
}

void loop() {
  if (!dmpReady) return;

  fifoCount = mpu.getFIFOCount();

  if (fifoCount == 1024) {
    mpu.resetFIFO();
    Serial.println("FIFO overflow!");
  } else if (fifoCount >= packetSize) {
    while (fifoCount >= packetSize) {
      mpu.getFIFOBytes(fifoBuffer, packetSize);
      fifoCount -= packetSize;
    }

    mpu.dmpGetQuaternion(&q, fifoBuffer);
    mpu.dmpGetGravity(&gravity, &q);
    mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
    yaw = ypr[0] * 180/M_PI;
    Serial1.println(String(yaw));
    delay(100);
    Serial.println(yaw);
  }
}
