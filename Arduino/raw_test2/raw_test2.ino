#include <MPU_6050.h>
#include <Wire.h>

#define N 150
const int MPU_addr = 0x68; // I2C address of the MPU-6050

MPU_6050 mpu(MPU_addr);
Data stableStateData(0,0,0,0,0,0);

void setup() {
  mpu.wakeUp();
  Serial.begin(9600);
  
  Serial.println("Setup started");
  
  for(int i = 0; i < N; i++){
    if(i%5==0){
      Serial.print(".");
    }
    stableStateData = stableStateData.add(mpu.measure());
    delay(10);
  }
  stableStateData = stableStateData.div(N);

  Serial.println("\nSetup complete");
  
}

void loop() {
  Data data = mpu.measure();
  data.sub(stableStateData).print();
  delay(8);
}
