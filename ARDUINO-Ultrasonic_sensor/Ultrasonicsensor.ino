#include <Servo.h>
Servo myservo;
int pos = 0;
boolean check = 0;
const int trigger_pin = 9;
const int echo_pin = 10;
float distance;
float time;

void setup() {
  pinMode(trigger_pin, OUTPUT);
  pinMode(echo_pin, INPUT);
  myservo.attach(11);
  Serial.begin(9600);
}
void loop() {
  digitalWrite(trigger_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigger_pin, HIGH);
  delayMicroseconds(1000);
  digitalWrite(trigger_pin, LOW);

  time = pulseIn(echo_pin, HIGH);
  distance = (time / 2) / 29.15;
  Serial.println(distance);
  
  if (distance >= 15) {
    check = 1;
  }
  if (distance <= 4) {
    check = 0;
  }

  if(check){
    Serial.println(distance);
    myservo.write(90);
    delay(500);
  }
  else{
    Serial.println(distance);
    myservo.write(0);
    delay(500);
  }
  
}

