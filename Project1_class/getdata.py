#coding:utf-8
import json
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
abspath = os.getcwd()

def writeMatrix(dataset, Path, coding = "utf-8"):
    for i in xrange(len(dataset)):
        temp = dataset[i]
        temp = [str(temp[j]) for j in xrange(len(temp))]
        temp = ",".join(temp)
        dataset[i] = temp
    string = "\n".join(dataset)
    f = open(Path, "a+")
    line = f.write(string+"\n")
    f.close()

def getData():
    file = open("data.json",'r')
    data = json.loads(file.read())
    file.close()
    data = data['data']
    # print type(data)
    y = ["C000008","C000022","C000010","C000016","C000007","C000014","C000024",
                "C000013","C000020","C000023"]#things_tag
    # print y
    X = []#to cluster
    Tag = []
    # print data[0],type(data[0])
    for i in range(len(data)):
        temp = []
        for j in range(len(y)):
            if data[i].has_key(y[j]):
                temp.append(data[i][y[j]])
            else:
                temp.append(0)
        X.append(temp)
        Tag.append(data[i]["user_crc"])
    return X

if __name__ == '__main__':
	X = getData()
	writeMatrix(X,'rawdata.txt')

