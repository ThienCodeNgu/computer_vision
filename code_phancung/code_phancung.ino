#include <ESP32Servo.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <WiFi.h>
#include <WebServer.h>
#include <HTTPClient.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();  // địa chỉ mặc định 0x40

#define SERVOMIN  150
#define SERVOMAX  750

const char* ssid = "jqk";
const char* password = "88888888";

WebServer server(80);

int pinled = 2;
bool done = false;
int hongngoai1 = 19;
int hongngoai2 = 34;

int IN1 = 27; 
int IN2 = 26; 
int ENA = 14; 

void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);

  Serial.begin(115200);
  pwm.begin();
  pwm.setPWMFreq(50);
  delay(10);

  pinMode(pinled, OUTPUT);
  pinMode(hongngoai1, INPUT);
  pinMode(hongngoai2, INPUT);

  servoWrite(0, 0);
  servoWrite(1, 150);
  servoWrite(2, 0);
  servoWrite(3, 120);
  servoWrite(4, 0);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.print("WiFi connected: ");
  Serial.println(WiFi.localIP());

  server.begin();
  Serial.println("WebServer started.");
  delay(5000);
}

// Gắp vật
void gap() {
  for (int angle = 0; angle <= 80; angle++) {
    servoWrite(0, angle);
    delay(20);
  }
  servoWrite(1, 150);
  for (int angle = 0; angle <= 55; angle++) {
    servoWrite(2, angle);
    delay(20);
  }
  delay(1000);
  servoWrite(3, 60);
  delay(1000);
  for (int angle = 45; angle >= 0; angle--) {
    servoWrite(2, angle);
    delay(20);
  }
  delay(1000);
}

void hamtha1() {
  for (int angle = 85; angle >= 50; angle--) {
    servoWrite(0, angle);
    delay(20);
  }
  delay(100);
  servoWrite(2, 0);
  delay(1000);
  for (int angle = 150; angle >= 110; angle--) {
    servoWrite(1, angle);
    delay(20);
  }
  delay(100);
  servoWrite(3, 120);
  delay(1000);
}

void hamtha2() {
  for (int angle = 85; angle >= 25; angle--) {
    servoWrite(0, angle);
    delay(20);
  }
  delay(100);
  servoWrite(2, 15);
  delay(1000);
  for (int angle = 150; angle >= 120; angle--) {
    servoWrite(1, angle);
    delay(20);
  }
  delay(100);
  servoWrite(3, 120);
  delay(1000);
}

void servoWrite(uint8_t channel, uint8_t angle) {
  if (angle > 270) angle = 270;
  uint16_t pulselen = map(angle, 0, 270, SERVOMIN, SERVOMAX);
  pwm.setPWM(channel, 0, pulselen);
}
void servo_return(){
  servoWrite(0, 0);
  servoWrite(1, 150); 
  servoWrite(2, 0);
  servoWrite(3, 120);
}
void gat(){
   
   for (int angle = 0; angle <= 150; angle++) {
    servoWrite(4, angle);
    delay(20);
  }
  servoWrite(4, 0);
}
void bangchuyenchay (int speed){
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, speed);
}
void bangchuyendung (){
   digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 220);
}
void loop() {
  int value_hn1 = digitalRead(hongngoai1);
  int value_hn2 = digitalRead(hongngoai2);

  if (value_hn1 == LOW) {   // Có vật đến vị trí đầu băng chuyền
    digitalWrite(pinled, HIGH);

    if (!done) {
      HTTPClient http;
      http.begin("http://192.168.94.125:5000/predict"); // IP máy chạy AI server
      int httpCode = http.GET();

      if (httpCode == 200) {
        String payload = http.getString();
        Serial.println("Kết quả từ AI: " + payload);
        gat();
        delay(2000);
        // Bật băng chuyền chạy
        bangchuyenchay(205);
        done = true;

        // Đợi đến khi vật đến cuối băng chuyền (cảm biến 2)
        while (digitalRead(hongngoai2) == HIGH) {
          // Giữ băng chuyền chạy
          delay(10);  // nhỏ để tránh loop quá nhanh
        }

        // Khi hongngoai2 phát hiện vật thể (thay đổi trạng thái)
        bangchuyendung();  // Dừng băng chuyền

        // Thực hiện gắp và phân loại theo màu
        if (payload == "orange") {
          gap();
          hamtha2();
        } else if (payload == "blue") {
          gap();
          hamtha1();
        }
        servo_return();

      } else {
        Serial.println("Không kết nối được AI Server");
      }
      http.end();
    }
  } else {
    digitalWrite(pinled, LOW);
    done = false;
  }

  server.handleClient();
  delay(50);
}




