#include<MPU_6050.h>
#include<Wire.h>

const int MPU_addr = 0x68;
MPU_6050 mpu(MPU_addr);

Data smoothData(0, 0, 0, 0, 0, 0);
float smoothStrength = 10;   // amount of smoothing (default 10)

Data stableStateData(0, 0, 0, 0, 0, 0);
int i = 0;



void setup() {
  mpu.wakeUp();
  Serial.begin(115200);

  resetMPU(150);
}

void loop() {
  Data data = mpu.measure().sub(stableStateData).div(1000);
  smoothData = smooth(data, smoothData);
  Serial.println(smoothData.toString());
  delay(8);
}

Data smooth(Data raw, Data last_smoothed) {
  return last_smoothed.add(raw.sub(last_smoothed).div(smoothStrength));
}

//returns stable state data over n iterations
Data resetMPU(int n) {
  for (int i = 0; i < n; i++) {
    stableStateData = stableStateData.add(mpu.measure());
    delay(10);
  }
  stableStateData = stableStateData.div(n);
}
