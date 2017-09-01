#encoding=utf-8
import numpy

#得到某个类别的数据

def getData(data_type = "A"):
    '''
    :param data_type: string A,B,O
    :return:
    '''
    if data_type!="182":
        file = open("data/art-model-data.txt", "r")
        dataAll = [line[line.find(".") + 1:].strip() for line in file.readlines()[1:]]

        if data_type== "A":
           return dataAll[:10]
        if data_type== "B":
            return  dataAll[11:21]
        if data_type=="U":
            return dataAll[22:-1]
    else:
        file = open("data/Nat-model-data.txt", "r")
        text = file.read();
        index_start = 1;
        index_end = 0;
        lines = []

        while(index_start!=183):
            line = ""
            find_start = text.find(str(index_start)+":>")
            find_end = text.find(str(index_start+1) + ":>")-3
            line=text[find_start:find_end]
            line = line[line.find(">")+1:]
            line_sub = ""
            for w in line:
                line_sub+=w.strip()
            lines.append(line_sub)
            index_start+=1
        return lines
    pass

