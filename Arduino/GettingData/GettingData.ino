#include <MPU_6050.h>
#include <Wire.h>

#define N 50
#define GESTURE_TIME 500
#define TIME_STEPS 100

Data smoothData(0, 0, 0, 0, 0, 0);
// amount of smoothing (default 10)
float smoothStrength = 10;   

//avarage of data in "zero" state
Data stableStateData(0, 0, 0, 0, 0, 0);


// I2C address of the MPU-6050
const int MPU_addr = 0x68;
//sensor MPU_6050
MPU_6050 mpu(MPU_addr);

void setup() {
  mpu.wakeUp();
  Serial.begin(115200);
}


void loop() {

  char val;

  //wait for input on serial port
  if (Serial.available() > 0) {

    //read input from serial port
    val = Serial.read();

    //for inputs 1,2,3,4
    if (val == '1' || val == '2' || val == '3' || val == '4') {
      
      Serial.println("Data");

      //measure gesture data and send it over serial connection
      Data data;
      for (int i = 0; i < TIME_STEPS; i++) {
        data = mpu.measure().sub(stableStateData).div(1000);
        smoothData = smooth(data, smoothData);
        Serial.print(data.get_az());
        Serial.print(",");
        Serial.println(smoothData.get_az());
        delay(8);
      }
      
      //after that send appropriate expected output
      //1,0,0,0 for input '1',
      //0,1,0,0 for input '2', etc...
      
      Serial.println("Output");

      char end_char = ',';
      String output = "";
      for (int i = 0; i < 4; i++) {
        if (i == 3) {
          end_char = '\n';
        }
        if (val - '0' - 1 == i) {
          output += "1";
          output += end_char;
        }
        else {
          output += "0";
          output += end_char;
        }
      }

      Serial.print(output);

      Serial.println("Done");
      
    }

    //if input is r (for reset) get new stable state data
    else if (val == 'r') {
      Serial.println("Setup started");
      resetMPU(N);
      Serial.println("Setup ended");
    }
  }
}

Data smooth(Data raw, Data last_smoothed) {
  return last_smoothed.add(raw.sub(last_smoothed).div(smoothStrength));
}

//returns stable state data over n iterations
void resetMPU(int n) {
  for (int i = 0; i < n; i++) {
    stableStateData = stableStateData.add(mpu.measure());
    delay(10);
  }
  stableStateData = stableStateData.div(n);
}
