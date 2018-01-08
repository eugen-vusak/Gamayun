#ifndef MPU_6050_h
#define MPU_6050_h

#include "Arduino.h"
#include <Wire.h>

class Data
{
	public:
		Data(long ax, long ay, long az, long gx, long gy, long gz);
		void print();
		Data add(Data other);
		Data sub(Data other);
		Data div(float c);
	private:
		long _ax;
		long _ay;
		long _az;
		long _gx;
		long _gy;
		long _gz;
};

class MPU_6050
{
	public:
		MPU_6050(int MPU_adr);
		void wakeUp();
		Data measure();
	private:
		int _MPU_adr;
};

#endif