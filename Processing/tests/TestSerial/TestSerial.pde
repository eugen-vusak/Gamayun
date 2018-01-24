import processing.serial.*;

Serial myPort;
String val;

void setup(){
  //print(Serial.list());
  String portName = Serial.list()[0];
  
  myPort = new Serial(this, portName, 115200);
}

void draw()
{
  /*if(myPort.available() > 0){
    val = myPort.readStringUntil('\n');
    print(val);
  }*/ 
}

void keyPressed(){
  print(key);
  myPort.write(key);
}