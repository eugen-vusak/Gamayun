import neural_network as nn

l1 = nn.InputLayer(100, nn.predprocess, "L1")
l2 = nn.Layer(100,10,nn.ActivationFunctions.sigmoid, "L2")
l3 = nn.Layer(10,5, nn.ActivationFunctions.sigmoid, "L3")
l4 = nn.Layer(5,4, nn.ActivationFunctions.sigmoid, "L4")

net = nn.FeedForwardNeuralNetwork([l1,l2,l3,l4])

data = nn.Data("../Data/test_data.csv",100,4)

net.train(data, batch_size = 1, epochs = 150, learning_rate = 5)

nn.saveToFile(net, ".neuralnetwork.pkl")