import numpy as np

def check(x):
    if float(x)>0.5:
        return ("B",float(x));
    return ("A",1-float(x));
def predict(data_input,W):
    import tools.myNumpyFun as myNumpyFunc
    data_input_mat = np.mat(data_input)
    h = myNumpyFunc.sigmoid(data_input_mat * W)
    result = [check(e) for e in h]
    return result
    pass
