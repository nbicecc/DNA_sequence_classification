import tools.dna2vec as dna
import tools.loaddata as loaddata
import numpy as np
import logiticReg
# print loaddata.getData("U")
import tools.myNumpyFun as myNumpyFunc
import predict


filedygx = open("dataout/dna-index.txt","wb")
dygx = ""
for index,item in enumerate([dna.basic_convert.digital2nucle(x)for x in range(64)]):
    dygx+= "%s %s"%(index,item)
    if (index+1)%8 == 0:
        dygx+="\r\n"
    else:
        dygx+=","
filedygx.write(dygx)
filedygx.flush()
filedygx.close()

data = loaddata.getData("A")
data[len(data):len(data)] = loaddata.getData("B")
data_dgts = [myNumpyFunc.softmax(dna.basic_convert.data2digitalVec16(line,2)) for line in data]

labels = np.zeros((20,))
for i in range(10,20):
    labels[i] = 1

trained_w = logiticReg.gradDes(data_dgts, lables=labels)

filedygx = open("dataout/W-LR-result.txt","wb")
text=""
for i in trained_w:
    text+=str(i)+"\n"
filedygx.write(text)
filedygx.flush()
filedygx.close()



filedygx = open("dataout/Labeld_A_and_B_data-pred-result.txt","wb")
dygx = ""
for index,item in enumerate([x for x in predict.predict(data_dgts,trained_w)]):
    dygx+= "%s %s\t\t"%(index+21,item)
    if (index+1)%1 == 0:
        dygx+="\r\n"
    else:
        dygx+=","
filedygx.write(dygx)
filedygx.flush()
filedygx.close()

data = loaddata.getData("U")
data_dgts = [myNumpyFunc.softmax(dna.basic_convert.data2digitalVec16(line,1)) for line in data]

filedygx = open("dataout/Ulabeleddata-pred-result.txt","wb")
dygx = ""
for index,item in enumerate([x for x in predict.predict(data_dgts,trained_w)]):
    dygx+= "%s %s\t\t"%(index+1,item)
    if (index+1)%1 == 0:
        dygx+="\r\n"
    else:
        dygx+=","
filedygx.write(dygx)
filedygx.flush()
filedygx.close()

data = loaddata.getData("182")
data_dgts = [myNumpyFunc.softmax(dna.basic_convert.data2digitalVec16(line,2)) for line in data]
index_pre = 1

filedygx = open("dataout/182-pred-result.txt","wb")
dygx = ""
for index,item in enumerate([x for x in predict.predict(data_dgts,trained_w)]):
    dygx+= "%s %s\t\t\t"%(index+1,item)
    if (index+1)%3 == 0:
        dygx+="\r\n"
    else:
        dygx+=","
filedygx.write(dygx)
filedygx.flush()
filedygx.close()


print "----------------Seeing results from path: ./dataout/*!---------------------"