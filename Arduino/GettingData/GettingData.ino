#include <MPU_6050.h>
#include <Wire.h>

#define N 150
#define GESTURE_TIME 500
#define BUFFER_SIZE 100

int SPACE = ' ';
int i = 0;

const int MPU_addr = 0x68; // I2C address of the MPU-6050
Data stableStateData(0, 0, 0, 0, 0, 0);
Data data;

MPU_6050 mpu(MPU_addr);

void setup() {
  Serial.begin(115200);
}
void loop() {

  char val;
  if (Serial.available() > 0) {
    val = Serial.read();
    if (val == SPACE) {
      String s = measureGesture();
      Serial.println(s);
    }
    else if (val == 'r') {
      Serial.println("Setup started");
      stableStateData = getStableStateData(N);
      Serial.println("Setup ended");
    }
    else{
      Serial.println(val);
    }
  }
}

String measureGesture() {
  String s = "";

  int i = 0;
  while (i > BUFFER_SIZE) {
    data = mpu.measure().sub(stableStateData);
    delay(8);
    s += data.toString() + ",";
  }
  Serial.println("done");
  return s;
}

Data getStableStateData(int n) {
  for (int i = 0; i < n; i++) {
    stableStateData = stableStateData.add(mpu.measure());
    delay(10);
  }
  return stableStateData.div(n);
}

