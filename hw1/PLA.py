import numpy as np
from future.utils import iteritems

datas = []
for line in open('./hw1/hw1_15_train.dat'):
	line = line.split()
	datas.append([float(line[0]), float(line[1]),
             float(line[2]), float(line[3]),float(line[4])])
datas = np.array(datas)

datasPocketTrain = []
datasPocketTest = []
for line in open('./hw1/hw1_18_train.dat'):
	line = line.split()
	datasPocketTrain.append([float(line[0]), float(line[1]),
               float(line[2]), float(line[3]), float(line[4])])

for line in open('./hw1/hw1_18_test.dat'):
	line = line.split()
	datasPocketTest.append([float(line[0]), float(line[1]),
               float(line[2]), float(line[3]), float(line[4])])

datasPocketTrain = np.array(datasPocketTrain)
datasPocketTest = np.array(datasPocketTest)

def sign(i):
	if i == 0.0:
		return -1.0
	else:
		return float(np.sign(i))

# code for hw1, question 15~17
def PLA(arr,r=1):
	X = []
	Y = []
	for data in arr:
		X.append([1,data[0],data[1],data[2],data[3]])
		Y.append(data[4])
	dataSize = len(X)
	startIdx = 0
	currIdx = 0
	updates = 0
	X = np.array(X)
	Y = np.array(Y)
	w = np.array([0, 0, 0, 0, 0])
	while currIdx - startIdx <= dataSize:
		if (sign(w.T.dot(X[currIdx % dataSize])) != Y[currIdx % dataSize]):
			w = w + r * Y[currIdx % dataSize] * X[currIdx % dataSize]
			updates += 1
			startIdx = currIdx
		currIdx += 1
	return (updates, w)

# code for hw1, question 16
def PLA_random(arr,r=1.0):
	total = 0.0
	arrCopy = arr[:]
	for _ in range(2000):
		np.random.shuffle(arrCopy)
		ans = PLA(arrCopy,r)
		total += ans[0]
	return total / 2000

# code for hw1, question 18~20
def Pocket(arr,arrTest,r=1):
	X = []
	Y = []
	for data in arr:
		X.append([1, data[0], data[1], data[2], data[3]])
		Y.append(data[4])
	X = np.array(X)
	Y = np.array(Y)

	XTest = []
	YTest = []
	for data in arrTest:
		XTest.append([1, data[0], data[1], data[2], data[3]])
		YTest.append(data[4])
	XTest = np.array(XTest)
	YTest = np.array(YTest)
	missRate = 0
	for _ in range(100):
		np.random.seed()
		dataSize = len(X)
		updates = 0
		wHat = np.array([0, 0, 0, 0, 0])
		w = np.array([0, 0, 0, 0, 0])
		minMistakes = dataSize + 1
		while updates < 100:
			idx = np.random.randint(dataSize)
			if (sign(w.T.dot(X[idx])) != Y[idx]):
				w = w + r * Y[idx] * X[idx]
				miss = verify(w, X, Y)
				if (miss < minMistakes):
					minMistakes = miss
					wHat = w
				updates += 1
		mr = verify(wHat, XTest, YTest) / len(XTest)
		missRate += mr
	
	return missRate /100

# code for hw1, question 19
def PLA_50(arr, arrTest, r=1):
	X = []
	Y = []
	for data in arr:
		X.append([1, data[0], data[1], data[2], data[3]])
		Y.append(data[4])
	X = np.array(X)
	Y = np.array(Y)

	XTest = []
	YTest = []
	for data in arrTest:
		XTest.append([1, data[0], data[1], data[2], data[3]])
		YTest.append(data[4])
	XTest = np.array(XTest)
	YTest = np.array(YTest)
	missRate = 0
	for _ in range(2000):
		np.random.seed()
		dataSize = len(X)
		updates = 0
		wHat = np.array([0, 0, 0, 0, 0])
		while updates < 50:
			idx = np.random.randint(0, dataSize)
			if (sign(wHat.T.dot(X[idx])) != Y[idx]):
				wHat = wHat + r * Y[idx] * X[idx]
				updates += 1
		missRate += verify(wHat, XTest, YTest) / dataSize

	return missRate / 2000
		
def verify(w,X,Y):
	mistakes = 0
	for idx in range(len(X)):
		if (sign(w.T.dot(X[idx])) != Y[idx]):
			mistakes += 1
	return mistakes

PLA(datas.copy())
rPo = Pocket(datasPocketTrain, datasPocketTest)
rPLA = PLA_50(datasPocketTrain, datasPocketTest)
