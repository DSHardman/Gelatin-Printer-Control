int sensorPin = A0;
int mosfetPin = 7; // controlling syringe heaters

float targetTemp = 45; // in Celsius

float resistor = 820; // Value of upper resistor in potential divider

int n = 20; // Number of samples averaged per reading

float sensorValue = 0;
 
void setup() {
  Serial.begin(9600);
  pinMode(mosfetPin, OUTPUT);
  digitalWrite(mosfetPin, LOW);
}
 
void loop() {

  // Take average of n readings for smoother operation
  sensorValue = 0;
  for (int i=0; i<n; i++) {
    sensorValue += analogRead(sensorPin);
    delay(100);
  }
  sensorValue = sensorValue/(n*1023); // Convert to fraction of operating voltage

  sensorValue = (sensorValue*resistor)/(1 - sensorValue); // convert to resistance

  sensorValue = (sensorValue - 2000)/7.7 - 4; // convert to temperature of Pt2000 thermistor, assuming linearity
  // -4 gives a response matching that of the previous K-type thermocouple being used
 
  Serial.println(sensorValue);
  Serial.print(" ");

  // Implement bang-bang temperature control, with small amount of hysteresis:
  if (sensorValue < (targetTemp - 0.5)) {
    digitalWrite(mosfetPin, HIGH);
    Serial.print("ON\n");
  }
  else if (sensorValue > (targetTemp + 0.5)) {
    digitalWrite(mosfetPin, LOW);
    Serial.print("OFF\n");
  }
 
}
