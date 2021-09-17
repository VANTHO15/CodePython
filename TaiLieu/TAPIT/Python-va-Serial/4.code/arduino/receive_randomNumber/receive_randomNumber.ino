void setup() {
  Serial.begin(9600);
  Serial.setTimeout(50);

}

void loop() {
  if(Serial.available()>0)
  {
    String number = Serial.readString();
    Serial.print(number);
  }

}
