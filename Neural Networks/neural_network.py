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



d
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
d





