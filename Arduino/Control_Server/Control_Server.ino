#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>

const char* ssid = "_";
const char* password = "top-secret";

ESP8266WebServer server(80);

int steeringOffset = 100;

int forward = 16;
int backward = 5;
int left = 4;
int right = 14;

void handleRoot() {
  server.send(200, "text/plain", "Server Running!");
}


void setup(void){

  pinMode(forward, OUTPUT);
  pinMode(backward, OUTPUT);
  pinMode(left, OUTPUT);
  pinMode(right, OUTPUT);

  digitalWrite(forward, LOW);
  digitalWrite(backward, LOW);
  digitalWrite(left, LOW);
  digitalWrite(right, LOW);

  Serial.begin(115200);
  WiFi.begin(ssid, password);



  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  Serial.println(WiFi.localIP());


  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }

  server.on("/forward", [](){
    int duration = server.arg("duration").toInt();
    Serial.println("Moving Forward for: " + String(duration));

    digitalWrite(forward, HIGH);
    server.send(200, "text/plain", "{\"status\": \"moved_forward\"}");
    delay(duration);
    digitalWrite(forward, LOW);
  });

  server.on("/backward", [](){
    int duration = server.arg("duration").toInt();
    Serial.println("Moving Backward for: " + String(duration));

    digitalWrite(backward, HIGH);
    server.send(200, "text/plain", "{\"status\": \"moved_backward\"}");
    delay(duration);
    digitalWrite(backward, LOW);
  });

  server.on("/left", [](){
    int duration = server.arg("duration").toInt();
    Serial.println("Moving Left for: " + String(duration));

    digitalWrite(left, HIGH);
    digitalWrite(forward, HIGH);
    server.send(200, "text/plain", "{\"status\": \"moved_left\"}");
    delay(duration);
    digitalWrite(forward, LOW);
    delay(steeringOffset);
    digitalWrite(left, LOW);
  });

  server.on("/right", [](){
    int duration = server.arg("duration").toInt();
    Serial.println("Moving Right for: " + String(duration));

    digitalWrite(right, HIGH);
    digitalWrite(forward, HIGH);
    server.send(200, "text/plain", "{\"status\": \"moved_right\"}");
    delay(duration);
    digitalWrite(forward, LOW);
    delay(steeringOffset);
    digitalWrite(right, LOW);
  });


  server.begin();

}

void loop(void){
  server.handleClient();
}
