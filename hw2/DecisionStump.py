import numpy as np
from future.utils import iteritems


def DScorrect(tha, signs, num, y):
	return np.sign(y) == (np.sign(num - tha) * signs)

def mutliDScorrect(tha,signs,num,y):
    return y == (np.sign(num - tha) * signs)

def trainDS(train,test):
    minEin = 1.0
    Eout = 0.0
    minminTha = 0.0
    minminSign = 1.0
    size = len(train)
    yTrain = train[:,-1]
    yTest = test[:,-1]
    for i in range(len(train[0]) - 1):
        #positive
        minMis = size + 1
        minTha = 0
        minSign = 1
        sign = 1
        for x in train[:,i]:
            tha = x + 0.0000001
            mistake = 0
            for n in range(len(train)):
                if (not mutliDScorrect(tha, sign,train[n][i],yTrain[n])):
                    mistake += 1
            if (minMis > mistake):
                minMis = mistake
                minTha = tha
                minSign = sign
        sign = -1
        for x in train[:,i]:
            tha = x + 0.0000001
            mistake = 0
            for n in range(len(train)):
                if (not mutliDScorrect(tha, sign, train[n][i], yTrain[n])):
                    mistake += 1
            if (minMis > mistake):
                minMis = mistake
                minTha = tha
                minSign = sign
        Ein = minMis / size
        if (Ein < minEin):
            minminTha = minTha
            minminSign = minSign
            minEin = Ein
    mistake = 0
    ele = 0
    for i in range(len(test[0]) - 1):
        for x in range(len(test)):
            if (not mutliDScorrect(minminTha, minminSign,test[x][i], yTest[x])):
                mistake += 1
            ele += 1
    Eout = mistake / ele
    print("Ein =",minEin,"Eout =",Eout)

def FindMutliDimenDS():
    datasTrain = []
    datasTest = []
    for line in open('./hw2/hw2_train.dat'):
        line = line.split()
        arr = []
        for num in line:
            arr.append(float(num))
        datasTrain.append(arr)
    
    for line in open('./hw2/hw2_test.dat'):
        line = line.split()
        arr = []
        for num in line:
            arr.append(float(num))
        datasTest.append(arr)
    datasTrain = np.array(datasTrain)
    datasTest = np.array(datasTest)
    trainDS(datasTrain,datasTest)

FindMutliDimenDS()

def FindDS(size):
    Ein = 0
    Eout = 0
    times = 500
    for _ in range(times):
        datas = []
        y = []
        for _ in range(size):
            num = np.random.uniform(-1.0, 1.0)
            datas.append(num)
        datas = np.array(datas)
        datas.sort()
        for data in datas:
            if (np.random.random_sample() < 0.2):
                y.append(-1 * data)
            else:
	            y.append(data)
        y = np.array(y)
        #positive
        minMis = size + 1
        minTha = 0.0
        minSign = 1
        sign = 1
        for i in range(size + 1):
            tha = 0.0
            if (i == 0):
                tha = datas[i] - 1.0
            elif (i == size):
                tha = datas[i-1] + 1.0
            else:
                tha = (datas[i] + datas[i-1]) / 2
            mistake = 0
            for i in range(size):
                if (not DScorrect(tha, sign, datas[i], y[i])):
                    mistake += 1
            if (minMis > mistake):
                minMis = mistake
                minTha = tha
                minSign = sign
        sign = -1
        for i in range(size + 1):
            tha = 0.0
            if (i == 0):
                tha = datas[i] - 1.0
            elif (i == size):
                tha = datas[i-1] + 1.0
            else:
                tha = (datas[i] + datas[i-1]) / 2.0
            mistake = 0
            for i in range(size):
                if (not DScorrect(tha, sign,datas[i], y[i])):
                    mistake += 1
            if (minMis > mistake):
                minMis = mistake
                minTha = tha
                minSign = sign
        Ein += minMis / size
        Eout += np.abs(0.5 + 0.3 * minSign * (np.abs(minTha) - 1))
    print("Ein = ",Ein / times," Eout =",Eout / times)

FindDS(20)
