import matplotlib.pyplot as plt
import math 
import random

class Gesture:

	def __init__(self, x_axis, y_axis):
		self.x_axis = x_axis
		self.y_axis = y_axis

	def plot(self, a,b,c):
		plt.subplot(a,b,c)
		plt.ylim([-4,4])
		plt.plot([x for x in range(len(self.x_axis))], self.x_axis, color = '#4CAF50')
		plt.plot([x for x in range(len(self.x_axis))], self.y_axis , color = '#FF9800')


random.seed()

num = 50

x_axis_zero = [random.random()-0.5 for x in range(num)]
y_axis_zero = [random.random()-0.5 for x in range(num)]
x_axis_not_zero = [random.randint(3,5)*random.random()*math.cos(x) for x in range(num)]
y_axis_not_zero = [random.randint(3,5)*random.random()*math.cos(x) for x in range(num)]

SG = Gesture(x_axis_zero, y_axis_zero)
SG.plot(2,2,1)

LRG = Gesture(x_axis_zero, y_axis_not_zero)
LRG.plot(2,2,2)

UDG = Gesture(x_axis_not_zero, y_axis_zero)
UDG.plot(2,2,3)

LURG = Gesture(x_axis_not_zero, y_axis_not_zero)
LURG.plot(2,2,4)


'''
with open("testing_data.csv", "w") as file:

	for i in range(10):

		print(i)

		x_axis_zero = [random.random()-0.5 for x in range(num)]
		y_axis_zero = [random.random()-0.5 for x in range(num)]
		
		SG = Gesture(x_axis_zero, y_axis_zero)
		file.write(",".join(str(x) for x in (SG.x_axis + SG.y_axis + [1,0,0,0])) + "\n")

		x_axis_zero = [random.random()-0.5 for x in range(num)]
		y_axis_not_zero = [random.randint(3,5)*random.random()*math.cos(x) for x in range(num)]

		LRG = Gesture(x_axis_zero, y_axis_not_zero)
		file.write(",".join(str(x) for x in (LRG.x_axis + LRG.y_axis + [0,1,0,0])) + "\n")
		
		y_axis_zero = [random.random()-0.5 for x in range(num)]
		x_axis_not_zero = [random.randint(3,5)*random.random()*math.cos(x) for x in range(num)]

		UDG = Gesture(x_axis_not_zero, y_axis_zero)
		file.write(",".join(str(x) for x in (UDG.x_axis + UDG.y_axis + [0,0,1,0])) + "\n")

		x_axis_not_zero = [random.randint(3,5)*random.random()*math.cos(x) for x in range(num)]
		y_axis_not_zero = [random.randint(3,5)*random.random()*math.cos(x) for x in range(num)]

		LURG = Gesture(x_axis_not_zero, y_axis_not_zero)
		file.write(",".join(str(x) for x in (LURG.x_axis + LURG.y_axis + [0,0,0,1])) + "\n")
'''
plt.show()
