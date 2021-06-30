int sensorPin1 = A0;
int mosfetPin1 = 7; // controlling syringe heaters
int sensorPin2 = A1;
int mosfetPin2 = 6;

float targetTemp1 = 45; // in Celsius
float targetTemp2 = 45;

float resistor = 820; // Value of upper resistors in potential divider

int n = 20; // Number of samples averaged per reading

float sensorValue1 = 0;
float sensorValue2 = 0;
 
void setup() {
  pinMode(mosfetPin1, OUTPUT);
  digitalWrite(mosfetPin1, LOW);
  pinMode(mosfetPin2, OUTPUT);
  digitalWrite(mosfetPin2, LOW);
}
 
void loop() {

  // Take average of n readings for smoother operation
  sensorValue1 = 0;
  sensorValue2 = 0;
  for (int i=0; i<n; i++) {
    sensorValue1 += analogRead(sensorPin1);
    //sensorValue2 += analogRead(sensorPin2);
    sensorValue2 += analogRead(sensorPin1); // ONLY USE ONE TEMPERATURE SENSOR
    delay(100);
  }

  // DEAL WITH FIRST SYRINGE
  sensorValue1 = sensorValue1/(n*1023); // Convert to fraction of operating voltage
  sensorValue1 = (sensorValue1*resistor)/(1 - sensorValue1); // convert to resistance
  sensorValue1 = (sensorValue1 - 2000)/7.7 - 4; // convert to temperature of Pt2000 thermistor, assuming linearity
  // -4 gives a response matching that of the previous K-type thermocouple being used

  // Implement bang-bang temperature control, with small amount of hysteresis:
  if (sensorValue1 < (targetTemp1 - 0.5)) {
    digitalWrite(mosfetPin1, HIGH);
  }
  else if (sensorValue1 > (targetTemp1 + 0.5)) {
    digitalWrite(mosfetPin1, LOW);
  }

  // DEAL WITH SECOND SYRINGE
  sensorValue2 = sensorValue2/(n*1023); // Convert to fraction of operating voltage
  sensorValue2 = (sensorValue2*resistor)/(1 - sensorValue2); // convert to resistance
  sensorValue2 = (sensorValue2 - 2000)/7.7 - 4; // convert to temperature of Pt2000 thermistor, assuming linearity
  // -4 gives a response matching that of the previous K-type thermocouple being used

  // Implement bang-bang temperature control, with small amount of hysteresis:
  if (sensorValue2 < (targetTemp2 - 0.5)) {
    digitalWrite(mosfetPin2, HIGH);
  }
  else if (sensorValue2 > (targetTemp2 + 0.5)) {
    digitalWrite(mosfetPin2, LOW);
  }
 
}
