#include "Arduino.h"
#include "MPU_6050.h"

Data::Data()
{
	
}

Data::Data(double ax, double ay, double az, double gx, double gy, double gz)
{
  _ax = ax;
  _ay = ay;
  _az = az;
  _gx = gx;
  _gy = gy;
  _gz = gz;
}

void Data::print()
{
  Serial.print("ax = "); Serial.print(_ax);
    Serial.print(" | ay = "); Serial.print(_ay);
    Serial.print(" | az = "); Serial.print(_az);
    Serial.print(" | gx = "); Serial.print(_gx);
    Serial.print(" | gy = "); Serial.print(_gy);
    Serial.print(" | gz = "); Serial.println(_gz);
}

String Data::toString(){
	return String(_ax)+","+
	String(_ay)+","+
	String(_az)+","+
	String(_gx)+","+
	String(_gy)+","+
	String(_gz);
}

Data Data::add(Data other){
	Data data(
		_ax + other._ax,
		_ay + other._ay,
		_az + other._az,
		_gx + other._gx,
		_gy + other._gy,
		_gz + other._gz
		);
	return data;
}

Data Data::div(double c)
{
	Data data(
		_ax / c,
		_ay / c, 
		_az / c,
		_gx / c,
		_gy / c,
		_gz / c
		);
	return data;
}

Data Data::sub(Data other){
	Data data(
		_ax - other._ax,
		_ay - other._ay,
		_az - other._az,
		_gx - other._gx,
		_gy - other._gy,
		_gz - other._gz
		);
	return data;
}


MPU_6050::MPU_6050(int MPU_adr)
{
	 _MPU_adr = MPU_adr;
}

void MPU_6050::wakeUp()
{
	Wire.begin();
  	Wire.beginTransmission(_MPU_adr);
  	Wire.write(0x6B);  // PWR_MGMT_1 register
  	Wire.write(0);     // set to zero (wakes up the MPU-6050)
  	Wire.endTransmission(true);
}

Data MPU_6050::measure()
{
	Wire.beginTransmission(_MPU_adr);
  	Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  	Wire.endTransmission(false);
  	Wire.requestFrom(_MPU_adr, 14, true); // request a total of 14 registers
  	int16_t ax = Wire.read() << 8 | Wire.read(); // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
  	int16_t ay = Wire.read() << 8 | Wire.read(); // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  	int16_t az = Wire.read() << 8 | Wire.read(); // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)
  	int16_t Tmp = Wire.read() << 8 | Wire.read(); // 0x41 (TEMP_OUT_H) & 0x42 (TEMP_OUT_L)
  	int16_t gx = Wire.read() << 8 | Wire.read(); // 0x43 (GYRO_XOUT_H) & 0x44 (GYRO_XOUT_L)
  	int16_t gy = Wire.read() << 8 | Wire.read(); // 0x45 (GYRO_YOUT_H) & 0x46 (GYRO_YOUT_L)
  	int16_t gz = Wire.read() << 8 | Wire.read(); // 0x47 (GYRO_ZOUT_H) & 0x48 (GYRO_ZOUT_L)

  	Data data(ax,ay,az,gx,gy,gz);
    return data;

}