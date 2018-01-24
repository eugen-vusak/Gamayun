import neural_network as nn
import numpy as np
import matplotlib.pyplot as plt

def plot_data(data):
	i1 = data[::6]
	i2 = data[1::6]
	i3 = data[2::6]
	i4 = data[3::6]
	i5 = data[4::6]
	i6 = data[5::6]

	plt.ylim([-15,15])

	#print(len(i1),len(i2),len(i3),len(i4),len(i5),len(i6));
	plt.plot(	[x for x in range(len(i1))],
				i1,
				label = "x_ac")
	plt.plot(	[x for x in range(len(i2))],
				i2,
				label = "y_ac")

	plt.plot(	[x for x in range(len(i3))],
				i3,
				label = "z_ac")

	plt.plot(	[x for x in range(len(i4))],
				i4,
				label = "x_gy")

	plt.plot(	[x for x in range(len(i5))],
				i5,
				label = "y_gy")

	plt.plot(	[x for x in range(len(i6))],
				i6,
				label = "z_gy")



net = nn.loadFromFile(".neuralnetwork2.pkl")

testing_data = nn.Data("../Data/s_legit_test_data.csv",600,4)

total_tests = 0
correct_tests = 0

for data in testing_data.data_set:

	input, desired_output = data
	total_tests += 1

	print(desired_output)

	#print("error")
	#print(net.feedforward(input))
	#print(np.around(net.feedforward(input)) - desired_output)

	if np.sum(np.abs(np.around(net.feedforward(input)) - desired_output)) == 0: 
		correct_tests += 1
		plot_data(input)
		plt.show()
	else:
		print("GRESKA!!!!!!")
		plot_data(input)
		plt.show()

	#print(np.around(net.feedforward(input)))

print(correct_tests/total_tests * 100, "% tocnih primjera")