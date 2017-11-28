import numpy as np
import math

direction = 0.0 #совпадение курса и оса 0 или 1
level = 1.0
competency = 1.0 #

weight_d = 0.6
weight_l = 0.6
weight_c = 0.2


def activation(x):
	if x>=0.5:
		return True
	else:
		return False

def sigmoid(x):
	return(1/(1+math.exp(-x)))  

weights = np.array([weight_d, weight_l, weight_c])
inputs = np.array([direction, level, competency])
x = np.dot(inputs, weights)

decision = activation(x)
print ("Result: " + str(decision))
