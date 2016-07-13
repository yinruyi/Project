#coding:utf-8
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

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


def model():
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
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(X,Y)
	return clf

def main():
	clf = model()
	dot_data = StringIO() 
	tree.export_graphviz(clf, out_file=dot_data) 
	graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
	graph.write_pdf("model.pdf") 

if __name__ == '__main__':
	main()