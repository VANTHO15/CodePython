unsigned long timer = 0;

void setup() {
  Serial.begin(9600);

}

void loop() {
  // print a random number from 0 to 100
  if (millis() - timer >= 10)
  {
    timer = millis();
    Serial.write(random(100));
  }
  

  //delay(50);
}
