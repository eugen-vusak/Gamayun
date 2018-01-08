#include <MPU_6050.h>
#include <Wire.h>

const int MPU_addr = 0x68; // I2C address of the MPU-6050

MPU_6050 mpu(MPU_addr);

void setup() {
  mpu.wakeUp();
  Serial.begin(9600);

  Data data1 = mpu.measure();
  Data data2 = mpu.measure();
  Data data3 = data1.add(data2);

  data1.print();
  data2.print();
  data3.print();
  data3 = data3.div(2);
  data3.print();

  data1.sub(data3).print();
  data2.sub(data3).print();
}

void loop() {
}
