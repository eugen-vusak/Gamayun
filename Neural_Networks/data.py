import numpy as np

class Data:

	def __init__(self, csv_file, input_size = 0, output_size = 0):

		self.data_set = []
		self.index = 0

		with open(csv_file, "r") as file:
			
			for line in file:
				line = line.strip()
				
				if not line:
					continue
				
				l = line.split(",")
				if input_size + output_size > len(l):
					print("ERROR: line doesn't have enough data", line)
					exit(1)
	
				try:
					input = np.asfarray(l[:input_size]).reshape(input_size,1)
					output = np.asfarray(l[input_size:output_size+input_size]).reshape(output_size,1)
				except:
					print("ERROR: not possible to make float array from", line)
					exit(1)

				data = (input, output)
				self.data_set.append(data)

	def __str__(self):
		string = ""
		first = True
		for data in self.data_set:
			if first:
				string += "\ninput\n{}\noutput\n{}".format(data[0], data[1])
				first = False
			else:
				string += "\n" + "\ninput\n{}\noutput\n{}".format(data[0], data[1])
		return string

	def getNextMiniBatch(self, batch_size):
		minibatch = self.data_set[self.index:self.index+batch_size]
		self.index += batch_size
		return minibatch

	def resetToBegining(self):
		self.index = 0

	def shuffle(self):
		np.random.shuffle(self.data_set)