#encoding=utf-8
import tools.dna2vec.basic_convert as dna
import tools.myNumpyFun as myNumpyFunc
import numpy as np
#本文档计算
def tfidf():
    tfs = []
    lines = getlines()
    lines_np = np.asarray(lines)
    # print lines_np
    line_np_y = np.sum(lines_np,axis=0)
    tfs= 1.0*line_np_y/(np.sum(lines_np)+1)
    lines_np_x = np.sum(lines_np)
    idf = 1.0*lines_np_x/(line_np_y+1)
    tfidfs = []
    tfidfs_np=idf * tfs

    for item,index in enumerate(tfidfs_np):
        tfidfs.append([item,index])
    tfidfs_sorted = np.asarray(tfidfs)
    for x in sorted(tfidfs,key=lambda x: x[1],reverse=True)[:16]:
        print x[0],","

    pass

def getlines():
    import tools.loaddata as loaddata
    # dataA = loaddata.getData("A")
    dataA = loaddata.getData("B")
    dataU = loaddata.getData("U")
    data = [dna.data2digitalVec(line,2)for line in dataA]
    # data[len(data):len(data)] = [dna.data2digitalVec(line,2) for line in dataB]
    # data[len(data):len(data)] = [dna.data2digitalVec(line,1) for line in dataU]
    return data
tfidf()