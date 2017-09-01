import numpy as np

def softmax(input):
    return np.exp(input)/np.sum(np.exp(input),axis=0)
def sigmoid(input):
    return 1.0/(1+np.exp(-input))