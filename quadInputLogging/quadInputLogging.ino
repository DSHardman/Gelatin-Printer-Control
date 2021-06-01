int sensorPin1 = A0;    // select the input pin for the potentiometer
int sensorPin2 = A1;
int sensorPin3 = A2;
int sensorPin4 = A3;

int sensorValue1 = 0;  // variable to store the value coming from the sensor
int sensorValue2 = 0;
int sensorValue3 = 0;
int sensorValue4 = 0;
 
void setup() {
  // begin the serial monitor @ 9600 baud
  Serial.begin(9600);
}
 
void loop() {
  // read the value from the sensor:
  sensorValue1 = analogRead(sensorPin1);
  sensorValue2 = analogRead(sensorPin2);
  sensorValue3 = analogRead(sensorPin3);
  sensorValue4 = analogRead(sensorPin4);
 
  Serial.print(sensorValue1);
  Serial.print(" ");
  Serial.print(sensorValue2);
  Serial.print(" ");
  Serial.print(sensorValue3);
  Serial.print(" ");
  Serial.println(sensorValue4);
  Serial.print(" ");
 
  delay(10000);
}
