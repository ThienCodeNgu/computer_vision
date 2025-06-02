#include <Arduino.h>

// Chân kết nối
const int motor1Pin1 = 27;
const int motor1Pin2 = 26;
const int enable1Pin = 14;



void setup() {
  Serial.begin(115200);

  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(enable1Pin, OUTPUT);
}

void loop() {
  // Quay tiến
  Serial.println("Tiến");
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH);
  analogWrite(enable1Pin, 200);
 
}
