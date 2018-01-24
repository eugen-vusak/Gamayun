boolean ledState = false;
int ledPin = LED_BUILTIN;
unsigned long timerStartTime = 0;
char SPACE = ' ';

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin,LOW);
  Serial.begin(115200);
}

void loop() {
  //Serial.print("Hello world!\n");
  //delay(100);

  if(ledState == true && millis() - timerStartTime >= 2000){
    turnLedOff(ledPin);
  }

  char val;
  if(Serial.available()){
    val = Serial.read();
    if(val == SPACE){
      if(ledState == false){
        turnLedOn(ledPin);
        timerStartTime = millis();   
      }
      else{
        turnLedOff(ledPin);
      }
    }
  }
}


void turnLedOn(int ledPin){
  digitalWrite(ledPin, HIGH);
  ledState = true;
}

void turnLedOff(int ledPin){
  digitalWrite(ledPin, LOW);
  ledState = false;
}

