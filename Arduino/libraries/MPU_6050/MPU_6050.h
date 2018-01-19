#ifndef MPU_6050_h
#define MPU_6050_h

#include "Arduino.h"
#include <Wire.h>

class Data
{
	public:
		Data();
		Data(double ax, double ay, double az, double gx, double gy, double gz);
		void print();
		String toString();
		Data add(Data other);
		Data sub(Data other);
		Data div(double c);
	private:
		double _ax;
		double _ay;
		double _az;
		double _gx;
		double _gy;
		double _gz;
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