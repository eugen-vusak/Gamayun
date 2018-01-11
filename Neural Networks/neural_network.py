import numpy as np
import ActivationFunctions
from data import Data
from layers import Layer, InputLayer
import matplotlib.pyplot as plt
import pickle

def predprocess(layer):
	return layer.Z/4

class FeedForwardNeuralNetwork:

	def __init__(self, layers = []):
		self.layers = layers
		self.ErrorAxis = []
		self.E = 0

	def addLayer(self, layer):
		self.layers.append(layer)

	def removeLayer(index):
		self.pop(index)

	def feedforward(self, input):
		for layer in self.layers:
			input = layer.output(input)
		return input

	def backpropagate(self,output, desired_output):

		#calculate for the last layer first
		output_layer = self.layers[-1]
		output_layer.error = output - desired_output


		self.E += (output_layer.error**2 / 2).sum()

		deriv = np.multiply(output_layer.A, 1-output_layer.A)

		output_layer.delta = np.multiply(output_layer.error, deriv)

		#from penultimate layer to second layer
		for l in reversed(range(1,len(self.layers)-1)):

				layer = self.layers[l]
			
				layer_plus_one = self.layers[l+1]
				layer.error = np.dot(layer_plus_one.weights.T,layer_plus_one.delta)
				
				
				deriv = layer.function(layer, deriv = True)

				layer.delta = np.multiply(layer.error, deriv)

	def gradientDescent(self):
		
		for l in range(1,len(self.layers)):

			layer = self.layers[l]
			layer_minus_one = self.layers[l-1]

			layer.pC_pW += np.dot(layer.delta, layer_minus_one.A.T)
			layer.pC_pB += layer.delta

			#layer.weights = layer.weights - self.learning_rate * layer.pC_pW
			#layer.biases = layer.biases - self.learning_rate * layer.pC_pB

	def train(self, training_data, batch_size = 32, epochs = 200, learning_rate = 0.5):

		iter_num = 0
		for i in range(epochs):
			#print(i)

			training_data.resetToBegining()
			miniBatch = training_data.getNextMiniBatch(batch_size)

			while(miniBatch):

				for data in miniBatch:

					input, desired_output = data
					#1. FeedForwardNeuralNetwork
					output = self.feedforward(input)
					print("num of iterations", iter_num)
					iter_num += 1
					#2. backpropagation
					self.backpropagate(output, desired_output)
					#3. gradientDescent
					self.gradientDescent()

				#update parametars for each layer
				#after every mini batch 
				for layer in self.layers:
					if type(layer) is InputLayer:
						continue
					layer.updateParametars(batch_size, learning_rate)

				miniBatch = training_data.getNextMiniBatch(batch_size)
				self.ErrorAxis.append(self.E/batch_size)
				self.E = 0
					
	def plotCostFunction(self):
		plt.plot([x for x in range(len(self.ErrorAxis))], self.ErrorAxis)
		plt.show()
		
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

########################################### main #######################################

def saveToFile(o, file):
	with open(file, "wb") as output_file:
		pickle.dump(o, output_file, pickle.HIGHEST_PROTOCOL)

def loadFromFile(file):
	with open(file, "rb") as input_file:
		return pickle.load(input_file)

np.random.seed()
'''
input_layer = InputLayer(2, ActivationFunctions.linear, "L1")

hidden_layer = Layer(2,2,ActivationFunctions.sigmoid, "L2")
hidden_layer.weights = np.array([	[0.15, 0.20],
									[0.25, 0.30]])

hidden_layer.biases = np.array([	[0.35],
									[0.35]])

output_layer = Layer(2,2,ActivationFunctions.sigmoid, "L3")
output_layer.weights = np.array([	[0.40,0.45],
									[0.50,0.55]])

output_layer.biases = np.array([	[0.60],
									[0.60]])

nn = FeedForwardNeuralNetwork([input_layer, hidden_layer, output_layer])
print(nn)
#data = Data("../Data/test.csv", 2,2)
data = Data("../Data/shuffled_data.csv",100,4)
#print(data)


l1 = InputLayer(100, predprocess, "L1")
l2 = Layer(100,10,ActivationFunctions.sigmoid, "L2")
l3 = Layer(10,5, ActivationFunctions.sigmoid, "L3")
l4 = Layer(5,4, ActivationFunctions.sigmoid, "L4")

nn = FeedForwardNeuralNetwork([l1,l2,l3,l4])

nn.train(data, batch_size = 1, epochs = 150, learning_rate = 5)

#saveToFile(nn, ".neuralnetwork.pkl")

nn = loadFromFile(".neuralnetwork.pkl")

#print(nn.ErrorAxis[-1])

#nn.plotCostFunction()

testing_data = Data("../Data/testing_data.csv", 100, 4)

total_tests = 0
correct_tests = 0
for data in testing_data.data_set:
	input, desired_output = data
	total_tests += 1
	if np.sum(np.around(nn.feedforward(input)) - desired_output) == 0: 
		correct_tests += 1

print(correct_tests/total_tests * 100, "% tocnih primjera")

'''