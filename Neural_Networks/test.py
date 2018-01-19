import neural_network as nn
import numpy as np

net = nn.loadFromFile(".neuralnetwork.pkl")

testing_data = nn.Data("../Data/testing_data.csv",100,4)

total_tests = 0
correct_tests = 0

for data in testing_data.data_set:

	input, desired_output = data
	total_tests += 1

	if np.sum(np.around(net.feedforward(input)) - desired_output) == 0: 
		correct_tests += 1

print(correct_tests/total_tests * 100, "% tocnih primjera")
