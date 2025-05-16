#include <ESP32Servo.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();  // địa chỉ mặc định 0x40

#define SERVOMIN  150  // xung ngắn nhất
#define SERVOMAX  750  // xung dài nhất
// int motor1Pin1 = 27; 
// int motor1Pin2 = 26; 
// int enable1Pin = 14; 
int pinled = 2;
bool done = false;
int hongngoai1 = 19;

// Setting PWM properties
// const int freq = 30000;
// const int pwmChannel = 0;
// const int resolution = 8;
// int dutyCycle = 200;

void setup() {
  Serial.begin(115200);
  pwm.begin();
  pwm.setPWMFreq(50);  // servo dùng tần số 50Hz
  delay(10);
  // sets the pins as outputs:
  // pinMode(motor1Pin1, OUTPUT);
  // pinMode(motor1Pin2, OUTPUT);
  // pinMode(enable1Pin, OUTPUT);
  pinMode(pinled, OUTPUT);
  pinMode(hongngoai1, INPUT);
  // // configure LEDC PWM
  // ledcAttachChannel(enable1Pin, freq, resolution, pwmChannel);

  // Serial.begin(115200);
  // góc ban đầu của các servo
  servoWrite(0, 0);//servo đế
  servoWrite(1, 130);
  servoWrite(2, 0);
  servoWrite(3, 120);
 delay(5000);
}
//hàm gắp vật 
void gap(){
  
  servoWrite(0, 105);
  delay(2000);
  servoWrite(1, 95);
  delay(1000);
  servoWrite(2, 38);
  delay(5000);
  servoWrite(3, 60);
  delay(1000);
  servoWrite(1, 130);
}
void hamtha1 (){
  servoWrite(0, 55);
  delay(2000);
  servoWrite(2, 0);
  delay(1000);
  servoWrite(1, 95);
  delay(5000);
  servoWrite(3, 120);
  delay(1000);
}
void hamtha2 (){
  servoWrite(0, 20);
  delay(2000);
  servoWrite(2, 0);
  delay(1000);
  servoWrite(1, 95);
  delay(5000);
  servoWrite(3, 120);
  delay(1000);
}
// Hàm điều khiển servo bằng góc
void servoWrite(uint8_t channel, uint8_t angle) {
  if (angle > 270) angle = 270; // Giới hạn góc
  uint16_t pulselen = map(angle, 0, 270, SERVOMIN, SERVOMAX);
  pwm.setPWM(channel, 0, pulselen);
}
void loop() {
  int value = digitalRead(hongngoai1);
  if (value == LOW){
    digitalWrite(pinled, HIGH);
  }else {
    digitalWrite(pinled, LOW);
  }
  if (!done){
 gap();
 hamtha2();
 done = true;
  }
 
  
  
  // // Move the DC motor forward at maximum speed
  // Serial.println("Moving Forward");
  // digitalWrite(motor1Pin1, LOW);
  // digitalWrite(motor1Pin2, HIGH); 
  // delay(2000);

  // // Stop the DC motor
  // Serial.println("Motor stopped");
  // digitalWrite(motor1Pin1, LOW);
  // digitalWrite(motor1Pin2, LOW);
  // delay(1000);

  // // Move DC motor backwards at maximum speed
  // Serial.println("Moving Backwards");
  // digitalWrite(motor1Pin1, HIGH);
  // digitalWrite(motor1Pin2, LOW); 
  // delay(2000);

  // // Stop the DC motor
  // Serial.println("Motor stopped");
  // digitalWrite(motor1Pin1, LOW);
  // digitalWrite(motor1Pin2, LOW);
  // delay(1000);

  // // Move DC motor forward with increasing speed
  // digitalWrite(motor1Pin1, HIGH);
  // digitalWrite(motor1Pin2, LOW);
  // while (dutyCycle <= 255){
  //   ledcWrite(enable1Pin, dutyCycle);   
  //   Serial.print("Forward with duty cycle: ");
  //   Serial.println(dutyCycle);
  //   dutyCycle = dutyCycle + 5;
  //   delay(500);
  // }
  // dutyCycle = 200;

  
}


