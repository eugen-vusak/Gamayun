'''
import numpy as np

class Layer:

	A = None
	Z = None


	def __init__(self, size):
		self.size = size

	def output(self):
		self.Z = sigmoid(self.A)
		return self.Z

	@staticmethod
	def sigmoid(matrix):
		return 1/1+np.exp(-matrix)

class NeuralNetwork:

	def __init__(self, layers):
		self.layers = layers[1:]
		self.weights = []

		for i in range(len(layers)-1):
			self.weights.append(2*np.random.random((layers[i].size, layers[i+1].size))-1)



	def feedfarward(self, input):
		if not input.size() == self.layers[0].size:
			#error
			return
		layers[0].A = input

		for i in range(1,len(layers)):
			layers[i].Z = np.dot(layers[i-1].A, weights[i-1])
			layers[i].output()




	Z - input (1 x n)
	A - output (1 x n)
	W - weights (n x n+1)

	A^0 = X

	Z^l = A^l-1 * W^l + B^l

	A^l = sigmoid(Z^l)

2. backprop
	E^L = A^L - Y
	
	D^l = E^l dot sigmoid'(Z^l)

	E^l = D^l+1 * trnas(W^l+1)

	parcC/parcW^l = trans(A^l-1) * D^l

'''

import numpy as np

def sigmoid(x, deriv = False):
	return 1/(1+np.exp(-0.2*x))

	

class Layer:

	output = None

	def __init__(self, input_size, output_size, function):
		self.input_size = input_size
		self.output_size = output_size

		self.function = function

		self.weights = np.random.random((output_size, input_size))
		self.biases = np.random.random((input_size,1))

	def output(self, input):

		if(self.input_size == 0):
			output = input
			return output

		output = self.function(np.dot(self.weights, input))
		return output
	
	def __repr__(self):
		return str(self.weights)


class FeedForwardNeuralNetwork:

	def __init__(self, layers = []):
		self.layers = layers

	def addLayer(self, layer):
		self.layers.append(layer)

	def removeLayer(index):
		self.pop(index)

	def feedforward(self, input):

		for layer in self.layers:
			input = layer.output(input)

		return input

	def train(self, data, desired_output, batch_size = 10, epoch = 200):

		miniBatch = data.getNextMiniBatch(batch_size)


		for data in miniBatch:
			output = self.feedforward(data)
			
			outputLayer = True
			for layer in reversed(self.layers):

				if outputLayer:
					error = output - desired_output
					outputLayer = False
				else:
					pass


	def __str__(self):
		string = ""
		first = True
		for layer in self.layers:
			if first:
				string += str(layer.output_size)
				first = False
			else:
				string += "->" + str(layer.output_size)

		return string

class Data:

	data_set = []
	index = 0

	def __init__(self, csv_file):
		with open(csv_file, "r") as file:
			for line in file:
				self.data_set.append(np.array(line.strip().split(",")).astype(np.float))

	def __str__(self):
		string = ""
		first = True
		for data in self.data_set:
			if first:
				string += str(data.tolist())
				first = False
			else:
				string += "\n" + str(data.tolist())
		return string

	def getNextMiniBatch(self, batch_size):
		if self.index + batch_size >= len(self.data_set):
			return self.data_set[self.index:]
		return self.data_set[self.index:self.index+batch_size]


	def shuffle(self):
		np.random.shuffle(self.data_set)


np.random.seed(1)

def linear(x):
	return x

input_layer = Layer(0,4,linear)
hidden_layer = Layer(4,13, sigmoid)
output_layer = Layer(13,2,sigmoid)

'''
input = np.array([	[1],
					[3],
					[1],
					[3]])
'''

nn = FeedForwardNeuralNetwork([input_layer, hidden_layer, output_layer])

print(nn)

data = Data("test.csv")

nn.train(data, np.array([0,1]))