import processing.serial.*;
import java.io.FileWriter;
import java.util.Arrays;
import java.lang.*;


Serial myPort;  //port on which is arduino
FileWriter outWriter = null; //fileWriter for output file

int gesture_counter = 0;

//booleans for connection
boolean dataAhead = false; 
boolean outputAhead = false;
int data_cnt = 0;
int output_cnt = 0;

//rectangle used to output message
int message_rect_height = 0;
boolean message_available = false;
boolean error_happened = false;
String output_string = "";

void setup() {
  size(600, 400);
  frameRate(240);
  try {
    //println(Serial.list()[0]);
    String portName = Serial.list()[0];
    myPort = new Serial(this, portName, 115200);
    myPort.bufferUntil('\n');
    println("connected to " + portName);
    myPort.clear();
    //setMessage("connected to" + portName, false);
  }
  catch(RuntimeException e) {
    e.printStackTrace();
    //setMessage(e.getMessage(),true);
  }

  String fileName = "/home/euzenmendenzien/Documents/FER/PPP/Data/ZaSlike/noisy_data.csv";
  try {
    outWriter = new FileWriter(fileName, false);
  }
  catch(IOException e) {
    println("ERROR unable to open file");
    e.printStackTrace();
  }
}


void draw() {
  background(#373737);
  /*if(message_available){
   output_message();
   }*/
}

void stop() {
  try {
    outWriter.close();
  }
  catch(IOException e) {
    error_happened = !error_happened;
    message_rect_height = 0;
    println("ERROR: unable to close file");
    e.printStackTrace();
  }
}

void keyPressed() {
  myPort.write(key);
}

void serialEvent(Serial myPort) {

  //get string from serial port
  String input = myPort.readStringUntil('\n');
  input = trim(input);
  println(input);

  if ("Done".equals(input)) {    
    outputAhead = false;
    appendToFile("\n", outWriter);
    println(data_cnt);
    print(output_cnt);
    print(++gesture_counter);
    return;
  }

  if ("Data".equals(input)) {
    dataAhead = true;
    data_cnt = 0;
    return;
  }

  if ("Output".equals(input)) {
    dataAhead = false;
    outputAhead = true;
    output_cnt = 0;
    return;
  }

  if (dataAhead) {
    try {
      for (String data : input.split(",")) {
        println(Float.parseFloat(data));
        data_cnt++;
      }
    }
    catch(NumberFormatException e) {
      println(e);
    }   
    appendToFile(input + ",", outWriter);
    return;
  }  

  if (outputAhead) {
    try {
      for (String data : input.split(",")) {
        println(Float.parseFloat(data));
        output_cnt++;
      }
    }
    catch(NumberFormatException e) {
      println(e);
    }   
    appendToFile(input, outWriter);
    return;
  }
}

void appendToFile(String string, FileWriter fw) {
  try {
    fw.write(string);
    fw.flush();
  }
  catch(IOException e) {
    println("ERROR: Unable to write to file");
  }
} 
/*
void setMessage(String message, boolean isError){
 message_rect_height = 0;
 message_available = true;
 error_happened = isError;
 output_string = message;
 }
 
 void output_message(){
 if(error_happened){
 fill(#F44336);
 }
 else{
 fill(#8BC34A);
 }
 noStroke();
 if(message_rect_height < 40){
 message_rect_height+=4;
 }
 rect(0,0,displayWidth, message_rect_height);
 if(message_rect_height == 40){
 //textSize(18);
 textFont(createFont("Roboto",16, true));
 textAlign(CENTER);
 fill(255,255,255,255);
 text(output_string,300,25 );
 }
 }*/