from math import exp
from logistic import logistic_fn

# CODE HERE

def inner_neuron(weight, input_):
	return weight[0]+sum(weight[i+1]*input_[i] for i in range(len(input_)))

def sigmoid_neuron(weight, input_):
	return logistic_fn(inner_neuron(weight, input_))

def feedforward(network, input_vector, hidden_neuron=sigmoid_neuron, output_neuron=inner_neuron):
	if len(network)>1:
#hidden_layer =[network[i] for i in range(len(network)-1)]
		hidden_layer = network[:-1]
		for i in range(len(hidden_layer)) :
			hidden_result = [hidden_neuron(hidden_layer[i][j],input_vector) for j in range(len(hidden_layer[i]))]
			input_vector = hidden_result
			print(input_vector)
	output_layer = network[-1]
	out_result = []
	for output in output_layer:
		out_result.append(output_neuron(output,input_vector))
	return out_result





# Example of a neural network. There is one hidden layer of two nodes,
# and an output layer. It computes the XNOR (NOT XOR) of the 2 inputs
xnor = [ [[10, -20, -20], [-30, 20, 20]], # hidden layer
         [[0, 1, 1]] # output layer
]
# Find a neural network that works as a XOR gate!
xor = [[[10,-20,-20],[-30,20,20]],[[1,-1,-1]]]
