#coding:utf-8
from sklearn import tree


def readCSV(path):
	import csv
	X,Y = [],[]
	csvfile = file(path,'rb')
	dataset = csv.reader(csvfile)
	for line in dataset:
		X.append(line[0:len(line)-1])
		Y.append(line[len(line)-1])
	csvfile.close()
	return X[1:],Y[1:]

def preTreat():
	X,Y = readCSV('dataset.csv')
	Y = [int(i) for i in Y]
	#X = [[float(i) for i in j] for j in X]
	for i in xrange(len(X)):
		temp = X[i]
		for j in xrange(len(temp)):
			try:
				temp[j] = float(temp[j])
			except:
				temp[j] = 0.0
	return X,Y

def model():
	X,Y = preTreat()
	X = X[0:int(len(X)*0.8)]
	Y = Y[0:int(len(Y)*0.8)]
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(X,Y)
	return clf

def main():
	clf = model()
	X,Y = readCSV('dataset.csv')
	Xtest = X[int(len(X)*0.8):]
	Ytest = Y[int(len(Y)*0.8):]
	Ytrain = clf.predict(Xtest)
	#print "predict result:"
	#print Ytrain
	#print "real result:"
	#print Ytest
	precision = len([Ytrain[i] for i in range(len(Ytest)) if int(Ytrain[i]) == int(Ytest[i])])*1.0/len(Ytest)
	print precision

if __name__ == '__main__':
	main()