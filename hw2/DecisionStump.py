import numpy as np
from future.utils import iteritems

def DScorrect(tha, signs, num):
	return np.sign(num) == (np.sign(num - tha) * signs)

def FindDS(size):
	Ein = 0
	Eout = 0
	times = 5000
	for _ in range(times):
		datas = []
		y = []
		for _ in range(size):
			num = np.random.uniform(-1.0, 1.0)
			datas.append(num)
			if (np.random.random_sample() < 0.2):
				y.append(-1 * num)
			else:
				y.append(num)
		
		#positive
		minMis = size + 1
		minTha = 0
		minSign = 1
		sign = 1
		for i in datas:
			tha = i + 0.0000001
			mistake = 0
			for j in y:
				if (not DScorrect(tha,sign,j)):
					mistake += 1
			if (minMis > mistake):
				minMis = mistake
				minTha = tha
				minSign = sign
		
		sign = -1
		for i in datas:
			tha = i + 0.0000001
			mistake = 0
			for j in y:
				if (not DScorrect(tha, sign, j)):
					mistake += 1
			if (minMis > mistake):
				minMis = mistake
				minTha = tha
				minSign = sign
		Ein += minMis / size
		Eout += np.abs(0.3 + 0.5 * minSign * (np.abs(minTha) - 1))
	print("Ein = ", Ein / times, " Eout = ", Eout / times)

FindDS(20)				


def TrainDS(train,test):
	Ein = 0
	Eout = 0
	size = len(train)
	for 
	for _ in range(times):
		datas = []
		y = []

		#positive
		minMis = size + 1
		minTha = 0
		minSign = 1
		sign = 1
		for i in datas:
			tha = i + 0.0000001
			mistake = 0
			for j in y:
				if (not DScorrect(tha, sign, j)):
					mistake += 1
			if (minMis > mistake):
				minMis = mistake
				minTha = tha
				minSign = sign

		sign = -1
		for i in datas:
			tha = i + 0.0000001
			mistake = 0
			for j in y:
				if (not DScorrect(tha, sign, j)):
					mistake += 1
			if (minMis > mistake):
				minMis = mistake
				minTha = tha
				minSign = sign
		Ein += minMis / size
		Eout += np.abs(0.3 + 0.5 * minSign * (np.abs(minTha) - 1))
	print("Ein = ", Ein / times, " Eout = ", Eout / times)

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


