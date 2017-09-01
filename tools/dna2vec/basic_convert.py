#encoding=utf-8
# dna序列

#a、t、g、c分别代表数字0,1,2,3
def j2d(j=""):
    if j=="a":return 0
    elif j=="t":return 1
    elif j=="g":return 2
    elif j=="c":return 3
    pass

def d2j(j=63):
    if j==0:return "a"
    elif j==1:return "t"
    elif j==2:return "g"
    elif j==3:return "c"
    pass

#核苷酸转代表值
def nucle2digital(nucle = ""):
    try:
        return j2d(nucle[0])*16+j2d(nucle[1])*4+j2d(nucle[2])
    except:
        import random
        return random.choice(xrange(64))
    pass
def digital2nucle(d):
    return d2j(d / 16)+d2j((d-d/16*16)/4)+d2j((d - d/4*4))

def data2vec(data,startcutfrom=0):
    '''
    得到切分DNA序列 ------------------（还无法确定起始密码子）
    :param data:
    :return:
    '''
    if startcutfrom==0:tmp = data
    elif startcutfrom==1:tmp =data[1:]
    elif startcutfrom==2:tmp = data[2:]
    arr1 = []
    while(len(tmp)!=0):
        arr1.append(tmp[:3])
        tmp= tmp[3:]
    tmp=data[1:]

    return arr1[:-1]

def data2digitalVec(data,startcutfrom=0):
    '''
    得到序列的特征向量
    :param data:string DNA序列
    :return:
    '''

    digitalV = []

    for i in range(64):
        digitalV.append(0)
    for i in data2vec(data,startcutfrom):
        index = nucle2digital(i)
        digitalV[index]+=1
    return digitalV

def data2digitalVec16(data, startcutfrom=0):
        '''
        得到序列的特征向量,压缩后
        :param data:string DNA序列
        :return:
        '''
        partern = [40,
                   58,
                   43,
                   10,
                 0,
                   32,
                   34,
                   42,
                   2,
                   14,
                   23,
                   46,
                   44,
                3,
                5,
                   48,

                   21,
                   20,
                   16,
                   17,
                   1,
                   29,
                   37,
                   53,
                   4,
                   19,
                   13,
                   22,
                   41,
                   26
                   ]
        digitalV = []

        for i in range(len(partern)):
            digitalV.append(0)
        for i in data2vec(data, startcutfrom):
            index = nucle2digital(i)
            if partern.count(index)!=0:
                digitalV[partern.index(index)] += 1
        return digitalV


