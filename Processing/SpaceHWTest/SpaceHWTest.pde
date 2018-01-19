import processing.serial.*;
import java.io.FileWriter;


Serial myPort;
int i = 0;
FileWriter output = null;

void setup() {
  size(300, 200);

  myPort = new Serial(this, Serial.list()[0], 115200);
  myPort.bufferUntil('\n');
  
  try {
    output = new FileWriter("/home/euzenmendenzien/Documents/FER/PPP/Processing/example.txt", false);
  }
  catch(IOException e) {
    println("It broke!!!");
    e.printStackTrace();
  }
}

void draw() {
  background(#373737 );
}

void stop(){
  try{
    output.close();
  }
  catch(IOException e){
    println("It broke!!!");
    e.printStackTrace();
  } 
}

void keyPressed() {
  myPort.write(key);
}

void serialEvent(Serial myPort) {

  String s = myPort.readStringUntil('\n');
  s = trim(s);
  println(s);
  
  try{
    output.write(s);
    output.flush();
  }
  catch(IOException e){
    println("It broke!!!");
    e.printStackTrace();
  }

  if ("Setup started".equals(s)) {
    //print("Setup started");
  } else if ("Setup complete".equals(s)) {
    //print("Setup complete");
  }
}