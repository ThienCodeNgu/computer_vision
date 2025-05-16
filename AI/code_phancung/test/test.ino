#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "jqk";
const char* password = "88888888";
int pinled = 2;

WebServer server(80);

void handleResult() {
  if (server.method() == HTTP_POST) {
    String body = server.arg("plain");  // hoặc đọc từng phần nếu gửi dạng json
    Serial.println("Nhận từ AI: " + body);
    server.send(200, "text/plain", "ESP32 nhận được");
    Serial.println(body);
   String cleanBody = body;
  cleanBody.trim(); // loại bỏ khoảng trắng đầu cuối
  cleanBody.replace("\"", ""); // loại bỏ dấu ngoặc kép nếu có
   Serial.println(cleanBody);
if (cleanBody == "orange") {
  digitalWrite(pinled, HIGH);
}
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.print("WiFi connected: ");
  Serial.println(WiFi.localIP());

  server.on("/result", HTTP_POST, handleResult);
  server.begin();
  Serial.println("WebServer started.");
  pinMode(pinled, OUTPUT);
  digitalWrite(pinled, LOW);
}

void loop() {
  server.handleClient();
}
