int ledPin = LED_BUILTIN;
int ledState = LOW;
char SPACE = ' ';

void setup()
{
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  establishContact();
}

void loop()
{
  Serial.println('L');
  if(Serial.available() > 0){
    char inByte = Serial.read();
    if(inByte == SPACE){
      toggleLED();
    }
  }
  delay(5000);
}
void establishContact() {
  while(Serial.available() <= 0){
    Serial.println("A");
    delay(5000);
  }
}

void toggleLED(){
  ledState = !ledState;
  digitalWrite(ledPin, ledState);
}

