import tools.dna2vec as dna

import numpy as np



def ng_log_likehood(pred_out , labels):
    return np.log(pred_out)[np.arange(labels.shape[0]), labels]

def gradDes(data_input,lables):
    import tools.myNumpyFun as myNumpyFunc

    data_input_mat = np.mat(data_input)
    lables_mat = np.mat(lables)
    input_m,input_n = np.shape(data_input_mat)
    W = np.ones((input_n,1))
    a = 0.01
    n_p = 5000
    for i in range(n_p):
        h = myNumpyFunc.sigmoid(data_input_mat*W)
        error =(h - lables_mat.transpose())
        grad = data_input_mat.transpose()*error
        W = W - a*grad
    return W
    pass
