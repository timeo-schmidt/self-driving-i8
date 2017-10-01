void setup() {

  Serial.begin(115200);
  Serial.println("Whats Up");

  int forward = 16;
  int backward = 5;
  int left = 4;
  int right = 14;
  int intervalTime = 500;

  pinMode(forward, OUTPUT);
  pinMode(backward, OUTPUT);
  pinMode(left, OUTPUT);
  pinMode(right, OUTPUT);

  digitalWrite(forward, LOW);
  digitalWrite(backward, LOW);
  digitalWrite(left, LOW);
  digitalWrite(right, LOW);

  Serial.println("Set All Pins Low");

  //Do the Actual Test
  Serial.println("Forward");
  digitalWrite(forward, HIGH);
  delay(intervalTime);
  digitalWrite(forward, LOW);


  delay(1000);


  Serial.println("Backward");
  digitalWrite(backward, HIGH);
  delay(intervalTime);
  digitalWrite(backward, LOW);


  delay(1000);

  
  Serial.println("Left");
  digitalWrite(left, HIGH);
  delay(intervalTime);
  digitalWrite(left, LOW);

  delay(1000);

  Serial.println("Right");
  digitalWrite(right, HIGH);
  delay(intervalTime);
  digitalWrite(right, LOW);

}

void loop() {

}
